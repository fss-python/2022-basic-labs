#!/bin/bash

export PYTHONPATH="$(pwd)/lab_1:$(pwd)/lab_2:$(pwd)/lab_3:$(pwd):${PYTHONPATH}"
echo "Running tests..."

python3 -m unittest
