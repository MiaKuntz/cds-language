#!/usr/bin/env bash

# create virtual enviroment
#python3 -m venv spacy_env

# activate virtual enviroment
#source ./spacy_env/bin/active

# then install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
#python3 -m spacy download en_core_web_md

# deactivate the env
#deactivate
# install hdbscan for BERTopic
sudo apt-get update
sudo apt-get install python3-dev

# requirements
pip install --upgrade pip
pip install --upgrade nbformat
python3 -m pip install -r requirements.txt
