#!/bin/bash

echo "Formatting..."
for FILE in $(git status --short | cut -d" " -f3)
do
    if [[ "$FILE" =~ \.py$ ]]; then
    echo "Formatting $FILE"
        pipenv run black -l 120 -t py39 "$FILE"
        pipenv run isort --py 39 "$FILE"
    fi
done
echo "Done."
