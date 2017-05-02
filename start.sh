#!/bin/bash

source venv/bin/activate
export MOCK=$1
export FLASK_APP=app.py
flask run
