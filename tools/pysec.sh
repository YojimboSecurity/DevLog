#!/bin/bash

echo "Running security tests..."
for FILE in $(find . -type f -iname "*.py" | grep -v migrations)
do
    if [[ "$FILE" =~ \.py$ ]]; then
        pipenv run bandit "$FILE"
        pipenv run pylint "$FILE"
    fi
done
echo "Done."