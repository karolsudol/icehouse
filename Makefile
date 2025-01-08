.PHONY: venv install clean

venv:
	python -m venv .venv


activate: source .venv/bin/activate
install: pip install -r requirements.txs
	

clean:
	rm -rf dbt_venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

all: install clean