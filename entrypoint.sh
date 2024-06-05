#!/bin/sh

echo "Running tests"

pytest --cov=. --cov-fail-under=90

echo "Ending tests"
