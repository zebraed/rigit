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
import threading
import logging
from functools import partial

from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools

from rigit.ui import rigit_main
from rigit.cmd import gitCmd
from rigit.ui.widget import(
CustomFileSystemModel,
CustomDelegate,
CustomListModel,
ProgressStatusBar
)
importlib.reload(gitCmd,
CustomFileSystemModel,
CustomDelegate,
CustomListModel,
ProgressStatusBar
)

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.split(__file__)[-1]


class RiGitMainUI(QtCore.QObject):
    gcmd = None
    def __init__(self, gcmd: gitCmd.RigitCmd):
        super(RiGitMainUI, self).__init__()
        self.setObjectName('RiGitMainUI')

        loader = QtUiTools.QUiLoader()
        ui_path = FILENAME.replace('.py', '.ui')
        self.ui = loader.load(ui_path, None)

        self.setupUi()

        # set main QMainWindow .ui file
        self.setWidgets(self.ui)

        # TODO
        self.setGitPath(gcmd, r"L:\tools\python\maya\testLocalRepo")

        # set operator class
        self.Commit = Commit(self.gcmd)

        self.setCallBack()

    def setupUi(self):
        pass

    def setWidgets(self, ui):
        self.mainUI_window     = ui.findChild(QtWidgets.QMainWindow,
                                              "RigitWindow")

        self.menuBar           = ui.findChild(QtWidgets.QMenuBar,
                                              "menuBar")

        self.statusBar         = ui.findChild(QtWidgets.QStatusBar,
                                              "statusBar")

        self.file_columnView   = ui.findChild(QtWidgets.QColumnView,
                                              "file_columnView")

        self.fileLog_listView  = ui.findChild(QtWidgets.QListView,
                                              "fileLog_listView")

        self.summary_lineEdit  = ui.findChild(QtWidgets.QLineEdit,
                                              "summary_lineEdit")

        self.comment_textEdit  = ui.findChild(QtWidgets.QTextEdit,
                                              "comment_textEdit")

        self.commit_pushButton = ui.findChild(QtWidgets.QPushButton,
                                              "commit_pushButton")

    def initMenuBar(self):
        pass

    def initStatusBar(self):
        pass

    def initFileColumnView(self):
        self.fileSys_model = CustomFileSystemModel()
        self.file_columnView.setModel(self.fileSys_model)

    def initFileLogListView(self):
        pass

    def setGitPath(self, gcmd, path: str):
        # self.SetPath_lineEdit
        self.gcmd = gcmd(path)

    def log(self, text: str):
        pass

    def setCallBack(self):
        comment = "doCommit"
        self.commit_pushButton.clicked.connect(
            partial(self.Commit.add_commit, comment)
        )

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
    win = RiGitMainUI(gitCmd.RigitCmd)
    win.show()
    sys.exit(app.exec_())