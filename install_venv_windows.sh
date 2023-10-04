#!/bin/bash

py -m venv env

# Activate the virtual environment
.\env\Scripts\activate
# Install packages from requirements.txt
pip install -r requirements.txt
# Deactivate the virtual environment
deactivate


