#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide a commit message."
    exit 1
fi

git add .


commit_message="$1"
git commit -m "$commit_message"


git push
