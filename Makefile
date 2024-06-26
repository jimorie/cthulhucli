VENV_DIR = venv
VERSION_SRC = cthulhucli.py

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf __pycache__

venv:
	python3 -m venv ${VENV_DIR}
	${VENV_DIR}/bin/pip install --upgrade pip
	${VENV_DIR}/bin/pip install .[dev]

patch: venv
	@VERSION=$$(${VENV_DIR}/bin/bump --patch --reset ${VERSION_SRC}); git add -u && git commit -m"Version $${VERSION}" && git tag "v$${VERSION}"

minor: venv
	@VERSION=$$(${VENV_DIR}/bin/bump --minor --reset ${VERSION_SRC}); git add -u && git commit -m"Version $${VERSION}" && git tag "v$${VERSION}"

major: venv
	@VERSION=$$(${VENV_DIR}/bin/bump --major --reset ${VERSION_SRC}); git add -u && git commit -m"Version $${VERSION}" && git tag "v$${VERSION}"

clean-tags:
	git tag --no-merged master | grep -e '^v[0-9]' | xargs git tag -d

dist: venv
	${VENV_DIR}/bin/python -m build --no-isolation -o dist .

upload: venv
	${VENV_DIR}/bin/twine upload dist/*

release: clean dist upload

lint: venv
	${VENV_DIR}/bin/ruff check
	${VENV_DIR}/bin/black --check cthulhucli.py

format: venv
	${VENV_DIR}/bin/black cthulhucli.py

test: venv
	@# Redirect stderr to stdout
	@echo '>>> import sys; sys.stderr = sys.stdout' > README.md.test
	@# Automagically import everything
	@echo '>>> from cthulhucli import *' >> README.md.test
	@# Turn off standalone_mode so launching the command doesn't sys.exit
	@echo '>>> ModelBase._standalone_mode = False' >> README.md.test
	@# Copy the README.md content
	@echo '' >> README.md.test
	@cat README.md >> README.md.test
	@# Delete all lines between "[DOCTEST_BREAK]::" and "[DOCTEST_CONTINUE]::"
	@sed -i '' '/^\[DOCTEST_BREAK\]::$$/,/^\[DOCTEST_CONTINUE\]::$$/ d' README.md.test
	@# Replace cthulhucli commands with REPL equivalent
	@sed -ri '' '/^```console$$/,/^```$$/ s/^. cthulhucli (.*)$$/>>> CthulhuModel.cli('\''\1'\'', reader=CthulhuReader)/g' README.md.test
	@# Replace cthulhucli usage reference with doctest.py
	@sed -ri '' '/^```console$$/,/^```$$/ s/Usage: cthulhucli/Usage: doctest.py/g' README.md.test
	@# Replace empty lines in console code blocks with "<BLANKLINE>" (to match CLI output)
	@sed -i '' '/^```console$$/,/^```$$/ s/^\s*$$/<BLANKLINE>/g' README.md.test
	@# Remove empty lines in python code blocks (we don't expect output there)
	@sed -i '' '/^```python$$/,/^```$$/{/^$$/d;}' README.md.test
	@# Prepend lines in python code blocks with ">>>" or "..." (if indented)
	@sed -ri '' '/^```python$$/,/^```$$/{s/^([^` ])/>>> \1/g;s/^([ ])/\.\.\. \1/g;}' README.md.test
	@# Add an empty line at the end of code blocks for mark an end for doctest
	@sed -i '' 's/^```$$/\n```/g' README.md.test
	@# Run doctest!
	COLUMNS=80 ${VENV_DIR}/bin/python -m doctest -o NORMALIZE_WHITESPACE -o ELLIPSIS ${SRC} README.md.test
