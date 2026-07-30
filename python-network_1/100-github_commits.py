#!/usr/bin/python3
"""
Script that lists 10 commits from most recent to oldest of a given repository.
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
