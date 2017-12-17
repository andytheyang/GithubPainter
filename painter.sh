#!/bin/bash

config_file="config.json"

if [ "$#" -eq 1 ]; then
    config_file=$1
    echo "using $config_file"
elif [[ "$#" -gt 1 ]]; then
    echo "too many arguments"
    exit 1  
fi

if [ ! -f "$config_file" ]; then
    echo "$config_file does not exist"
    exit 1
fi

repodir="$( jq -r '.repositorydir' "$config_file" )"
factor="$( jq -r '.commitfactor' "$config_file" )"

target=$repodir
target+="/testfile"

for i in `seq 1 $factor`;do
    touch $target
    date >> $target

    commitmsg="Dummy commit "
    commitmsg+="$(date)"

    git -C $repodir add .
    git -C $repodir commit -m "$commitmsg"
done

git -C $repodir push origin master

exit 0