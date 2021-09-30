#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
# developing in python3x
import sys
import os
import datetime
import time
import logging
import subprocess
import platform

import git
from git import GitCommandError
from git.exc import InvalidGitRepositoryError

try:
    unicode
else:
    unicode = str

class RigitCmd(object):
    """
    This class is git operation command class.
    Override the GitPython client and providers git operation commands.
    """
    path: string = None
    def __init__(self, path):
        self.path      = path
        self._repo     = None
        self.head      = None
        self.parent    = None
        self.branch    = None
        self.is_repo   = None

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, repo):
        self._repo = repo

    def init_repo(self, *args):
        """
        perform initialize git repository.
        """
        try:
            self.repo = git.Repo.init(self.path, mkdir=False)
            self.repo.index.commit('Init commit')
            self.is_repo = True
        except:
            print("Failed initialize repository.")
            return False
        else:
            return True

    def load_repo(self, path):
        self.path = path
        try:
            self.repo = git.Repo(path)
            self.is_repo = True
            branch = self.repo.active_branch.name
            self.dispatch('on_branch', branch)

        except InvalidGitRepositoryError:
            self.is_repo = False

    def validate_remote(self):
        pass

    def move_repo(self, path):
        os.chdir(path)
        return git.Repo()

    def pull(self, branch, mode):
        repo = self.repo
        orig = repo.remotes.origin
        orig.pull()

    def do_commit(self, comment):
        # head > commit
        repo = self.repo
        repo.index.commit(comment)
        return True

    def do_add(self, files):
        repo = self.repo
        un_files = repo.untracked_files
        if not un_files:
            return False
        try:
            self.repo.index.add(files)
        except GitCommandError as e:
            print(e)
            return False
        else:
            return True

    def push(self, master):
        repo = self.repo
        orig = repo.remote(name=master)
        orig.push()

    def checkout(self, branch):
        repo = self.repo
        if repo.is_dirtry():
            return False
        if not branch:
            return False

        try:
            if branch in repo.heads:
                repo.heads[branch].checkout()
            else:
                repo.create_head(branch)
                repo.heads[branch].checkout()
            branch = repo.active_branch.name
            self.dispatch('on_branch', branch)
        except GitCommandError as e:
            print(e)
            return False
        else:
            return True

    def diff(self, file=""):
        diffs = [ unicode(dif.diff)for dif in self.parent.diff(self.head,
                                                               creaste_patch=True)
        if file != "" and dif.b_blob.name == file ]
        return diffs

    # logをうまいこと活用したい。
    def get_log(log):
        pass

    def out_log(log):
        pass

    def get_commit_log(self, branch, max_count=10):
        repo = self.repo()
        for item in repo.iter_commits(branch, max_count=max_count):
            dt = datetime.datetime.fromtimestamp(item.ahthored_date).strftime("%Y-%m-%d %H:%M:%S")
            print("{0} {1} {2}".format(item.hexsha, item.author, dt))