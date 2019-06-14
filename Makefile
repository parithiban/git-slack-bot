.PHONY: clean system-packages python-packages install run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	pip install virtualenv
	make venv

venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv -p python3 venv
	venv/bin/pip install -U setuptools
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

install: system-packages

print:
	@echo export MYVAR=$(FLASK_APP):otherstuff ";"

run-queue:
	flask rq worker

run:
	python manage.py

all: clean install