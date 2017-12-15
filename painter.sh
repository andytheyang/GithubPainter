#!/bin/bash

config_file="config.json"

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