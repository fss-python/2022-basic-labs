#!/bin/bash

set -ex

source venv/bin/activate

export PYTHONPATH="$(pwd)/lab_1:$(pwd)/lab_2:$(pwd)/lab_3:$(pwd):${PYTHONPATH}"

echo "Running tests..."

LABS=$(cat automation/labs.txt)

echo "Current scope: $LABS"

for lab in $LABS; do
	echo "Running tests for lab #${lab}"

	if [[ ${lab} == 1 ]]; then
    echo "Running tests for lab1"
    python -m pytest -m "lab1"
  elif [[ ${lab} == 2 ]]; then
    echo "Running tests for lab2"
    python -m pytest -m "lab2"
  elif [[ ${lab} == 3 ]]; then
    echo "Running tests for lab3"
    python -m pytest -m "lab3"
  else
    echo "Unsupported lab number: ${lab}"
    exit 1
  fi
done

echo "Tests passed."
