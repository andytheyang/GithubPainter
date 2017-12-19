#!/usr/bin/env python

# GithubPainter Python

import os
import sys
import json
import random
import subprocess
import datetime

# https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python
def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

# default configuration
config_file_path = "config.json"

# check arguments for new configuration
if len(sys.argv) > 2:
    print("too many arguments")
    sys.exit(1)
elif len(sys.argv) == 2:
    config_file_path = sys.argv[1];

# load configuration
config_file = os.path.join(os.path.dirname(sys.argv[0]), config_file_path)     # default config absolute path
config = json.load(open(config_file))
repo_dir = config["repo_dir"];
weights = config["num_commit_weights"]

# generate required values
target_file = os.path.join(repo_dir, "testfile");
num_commits = weighted_choice(weights)

# open log and test file
log = open(os.path.join(os.path.dirname(sys.argv[0]), "debug.log"), "a+")
testfile = open(target_file, "a+")

# make num_commits commits
for i in range(0, num_commits):
    time = str(datetime.datetime.now())
    testfile.write(str(time) + "\r\n")
    testfile.flush()

    commit_msg = "Dummy commit " + str(time) + " " + str(i + 1) + " of " + str(num_commits)
    subprocess.call(["git", "-C", repo_dir, "add", "."])    # add all changes
    subprocess.call(["git", "-C", repo_dir, "commit", "-m", commit_msg])    # create commit

# close outputs
testfile.close()
log.write(str(datetime.datetime.now()) + " - " + str(num_commits) + " commits made\r\n")
log.close()

# git -C repo_dir push origin master
subprocess.call(["git", "-C", repo_dir, "push", "origin", "master"])


sys.exit(0)