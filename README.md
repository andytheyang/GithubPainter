GithubPainter
=============

GithubPainter is an automated utility that, when used with `cron`, can automatically a random number of commit every day and paint your GitHub contribution grid green! It accomplishes this by making edits to a dummy private GitHub repo and pushing changes daily.

Go from this:

![enter image description here](https://i.imgur.com/OMdf5yf.png)

To this:

![enter image description here](https://i.imgur.com/4wqCbfG.png)

Setup
=====

By default, `painter.py` accesses a configuration in `config.json` located in the same directory. `config.json` should look something like this:
```
{
    "repo_dir": "/home/andy/dummydir",
    "num_commit_weights":[1,3,2,1]
}
```

 1. Create an empty repository in GitHub and clone it locally via ssh. You may need to set up an [ssh key](https://help.github.com/articles/connecting-to-github-with-ssh/).
 2. Edit `config.json` or create a new `.json` configuration with the same keys.
 3. Set `repo_dir` to the absolute path of the empty repo.
 4. Set `num_commit_weights` to the weight of each possible number of commits. In the example above, the chance of 1 commit is 1/7, 2 commits is 3/7, 3 commits is 2/7, 4 commits is 1/7.
 5. At this point, you can test your connection by running `./painter.py` (to use `config.json`) or `./painter.py newconfig.json` to specify a custom configuration to use
 6. Run `crontab -e` to edit your cron configuration, and add the following line:  `5 0 * * * /home/user/GithubPainter/painter.py` at the end, replacing the path with the absolute path to your `painter.py` command tested in step 5.
 7. Now, whenever this machine is on at 12:05 AM every morning, it will attempt to make a random number of commits and push to your GitHub! Time to wait a couple months.
