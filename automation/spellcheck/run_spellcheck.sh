set -ex

source venv/bin/activate

python -m pyspelling -c automation/spellcheck/.spellcheck.yaml
