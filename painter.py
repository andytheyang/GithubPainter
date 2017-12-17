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

# load configuration
config_file = os.path.join(os.path.dirname(sys.argv[0]), "config.json")     # default config absolute path
config = json.load(open(config_file))
repo_dir = config["repo_dir"];
weights = config["num_commit_weights"]

# generate required values
target_file = os.path.join(repo_dir, "testfile");
num_commits = weighted_choice(weights)

# subprocess.call(["git", "pull"])

log = open(os.path.join(os.path.dirname(sys.argv[0]), "debug.log"), "a+")
testfile = open(target_file, "a+")

for i in range(0, num_commits):
    time = str(datetime.datetime.now())
    testfile.write(str(time) + "\r\n")
    testfile.flush()

    commit_msg = "Dummy commit " + str(time)
    subprocess.call(["git", "-C", repo_dir, "add", "."])    # add all changes
    subprocess.call(["git", "-C", repo_dir, "commit", "-m", commit_msg])    # create commit

testfile.close()
log.write(str(datetime.datetime.now()) + " - " + str(num_commits) + " commits made\r\n")
log.close()

subprocess.call(["git", "-C", repo_dir, "push", "origin", "master"])
sys.exit(0)