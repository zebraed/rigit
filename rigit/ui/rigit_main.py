#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
# developing in python3x
from __future__ import (
print_function,
unicode_literals,
division,
absolute_import
)

import os
import sys

from functools import partial

try:
    import rigit
except:
    pass

import rigit.ui.qtApp
from rigit.ui import rigit_main
from rigit import gitCmd

from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRENT_DIR = os.path.dirname(__file__)
FILENAME = os.path.split(__file__)[-1]

MAX_RECENTLY_COMMIT_LOG = 5

class RigitMainUI(QtWidgets.QMainWindow):
    title = "Rigit"
    def __init__(self, parent=None):
        super(RigitMainUI, self).__init__(parent)

        self.width  = 400
        self.height = 200

        loader = QtUiTools.QUiLoader()
        ui_path = os.path.join(CURRENT_DIR, FILENAME + '.ui')
        self.ui = loader.load(ui_path)

        self.findUI(self.ui)

        self.setGitPath("")

        self.setWindowTitle(self.title)

    def findUI(self, ui):
        self.MainUI = ui.findChild(QtWidgets.QMainWindow,
                                  "RigitWindow")
        self.Commit_pushButton= ui.findChild(QtWidgets.QPushButton,
                                              "commit_pushButton")

    def setCallBack(self):
        self.Commit_pushButton.clicked.connect(
            lambda:self.gcmd.do_commit("test commit!"))

    def setGitPath(self, path: str):
        # self.SetPath_lineEdit
        self.gcmd = gitCmd.RigitCmd(path)

    def log(self, text: str):
        pass


if __name__ == '__main__':
app = QtWidgets.QApplication.instance()
if not app:
    app = QtWidgets.QApplication(sys.argv)
win = RigitMainUI()
win.show()
sys.exit(app.exec_())