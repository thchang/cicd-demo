#!/bin/bash

## Check style
#flake8 ../src/*.py

cd .. && export PYTHONPATH=$PYTHONPATH:`pwd` && cd test

# Run tests
pytest -v --cov=../src --cov-report= . -W error::UserWarning

coverage report -m
