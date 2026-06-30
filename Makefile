# Build a clean, print-ready HTML copy of the resume from README.md.
#
#   make html    regenerate resume.html (then open it and Print -> Save as PDF)
#   make clean   remove the generated resume.html
#
# The first run bootstraps a local Python venv (.venv/) and installs the only
# dependency (markdown). No Homebrew/Node/Chrome required.

PYTHON ?= python3
VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
STAMP := $(VENV)/.installed

.PHONY: html clean

html: $(STAMP)
	$(PY) tools/render.py README.md resume.html
	@echo "Open resume.html in a browser, then Print -> Save as PDF."

$(STAMP):
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --quiet --disable-pip-version-check markdown
	@touch $@

clean:
	rm -f resume.html
