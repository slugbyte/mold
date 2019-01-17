#!/usr/bin/env bash
pipenv run pip freeze > requirements.txt 
python3 ./setup.py install
