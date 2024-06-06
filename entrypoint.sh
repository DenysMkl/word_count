#!/bin/sh

echo "Running tests"

pytest --cov=. -v

echo "Ending tests"
