#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
# developing in python3x
from __future__ import annotations
import sys
import os
import importlib
from functools import partial

from rigit.ui import rigit_main
from rigit import gitCmd
importlib.reload(gitCmd)

from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.split(__file__)[-1]

MAX_RECENTLY_COMMIT_LOG = 5

class RigitMainUI(object):
    gcmd   = None
    def __init__(self, gcmd: gitCmd.RigitCmd):
        loader = QtUiTools.QUiLoader()
        ui_path = FILENAME.replace('.py', '.ui')
        self.ui = loader.load(ui_path, None)

        # set main QMainWindow .ui file.
        self.findUI(self.ui)
        self.setGitPath(gcmd, r"L:\tools\python\maya\testLocalRepo")

        self.Commit = Commit(self.gcmd)

        self.setCallBack()

    def findUI(self, ui):
        self.MainUI = ui.findChild(QtWidgets.QMainWindow,
                                  "RigitWindow")
        self.Commit_pushButton= ui.findChild(QtWidgets.QPushButton,
                                              "commit_pushButton")

    def setCallBack(self):
        #self.Commit_pushButton.clicked.connect(
        #    lambda:self.Commit.add_commit("test commit!"))
        comment = "doCommit"
        self.Commit_pushButton.clicked.connect(
            partial(self.Commit.add_commit, comment)
        )

    def setGitPath(self, gcmd, path: str):
        # self.SetPath_lineEdit
        self.gcmd = gcmd(path)

    def log(self, text: str):
        pass

    def loadSettings(self):
        pass

    def show(self):
        self.ui.show()



class Commit:
    def __init__(self, gcmd):
        self.gcmd = gcmd

    def add_commit(self, comment):
        res_add_untracked  = self.gcmd.do_add_untracked()
        res_add_unstaged   = self.gcmd.do_add_unstaged()
        res_commit         = self.gcmd.do_commit(comment)
        print(res_add_untracked)
        print(res_add_unstaged)


if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    win = RigitMainUI(gitCmd.RigitCmd)
    win.show()
    sys.exit(app.exec_())