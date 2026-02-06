#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r analysis/requirements.txt
echo ">> Environment Ready. Activate with: source venv/bin/activate"
