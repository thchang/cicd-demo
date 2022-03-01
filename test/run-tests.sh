#!/bin/bash

# Check style
flake8 ../src/*.py

# Run tests
pytest -v --cov=../src --cov-report= . -W error::UserWarning

coverage report -m
