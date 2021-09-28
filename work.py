#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
import sys
import os
import datetime
import time
import logging
import subprocess
import platform

import git

try:
    unicode
else:
    unicode = str

class RigitCmd(object):

    def __init__(self, path):
        self.__repo    = git.Repo(path)
        self.head      = self.__repo.head.commit
        self.path      = path
        self.parent = self.head.parents[0]

    def init_repo(self, directory):
        self.repository = git.Repo.init(directory)

    @property
    def repository(self):
        return self.__repo

    @repository.setter
    def repository(self, repo)
        self.__repo = repo

    def move_repository(self, path):
        os.chdir(path)
        return git.Repo()

    def pull(branch, mode):
        repo = self.repository
        orig = repo.remotes.origin
        orig.pull()

    def commit(self, comment):
        # head > commit
        repo = self.repository
        repo.index.commit(comment)

    def push(self, master):
        repo = self.repository
        orig = repo.remote(name=master)
        orig.push()

    def checkout(self):
        repo = self.repository
        repo.git.checkout()

    def diff(self, file=""):
        diffs = [ unicode(dif.diff)for dif in self.parent.diff(self.head,
                                                               creaste_patch=True)
        if file != "":
            if dif.b_blob.name == file ]
        return diffs

    # logをうまいこと活用したい。
    def get_log(log):
        pass

    def out_log(log):
        pass

    def get_commit_log(self, branch, max_count=10):
        repo = self.repository()
        for item in repo.iter_commits(branch, max_count=max_count):
            dt = datetime.datetime.fromtimestamp(item.ahthored_date).strftime("%Y-%m-%d %H:%M:%S")
            print("{0} {1} {2}".format(item.hexsha, item.author, dt))