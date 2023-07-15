VENV_DIR = .venv
VERSION := $(shell python3 -c 'from cthulhucli.cthulhucli import __version__; print(__version__)')

dist:
	${VENV_DIR}/bin/python3 setup.py bdist_wheel

version:
	git add cthulhucli/cthulhucli.py
	git commit -m'Version ${VERSION}'
	git tag v${VERSION}
	git push --tags origin master

clean:
	rm -rf build
	rm -rf dist
	rm -rf cthulhucli.egg-info
	rm -rf cthulhucli/__pycache__

upload:
	${VENV_DIR}/bin/twine upload dist/*

release: clean version dist upload

format:
	black cthulhucli

lint:
	black --check cthulhucli

venv:
	python3 -m venv ${VENV_DIR}
	${VENV_DIR}/bin/pip install black twine
