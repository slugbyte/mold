#!/usr/bin/env bash
pipenv install
pipenv run pip freeze > requirements.txt
python3 ./setup.py install
