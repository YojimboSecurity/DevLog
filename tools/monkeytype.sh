#!/bin/bash

pipenv run monkeytype run devlog.py
for FILE in $(pipenv run monkeytype list-modules)
do
    pipenv run monkeytype apply "$FILE"
done