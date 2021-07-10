#!/bin/bash

echo "Running security tests..."
for FILE in $(git status --short | cut -d" " -f3)
do
    if [[ "$FILE" =~ \.py$ ]]; then
        pipenv run bandit "$FILE"
        pipenv run pylint "$FILE"
    fi
done
echo "Done."