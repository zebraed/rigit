#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
# developing in python3x
import sys
import os
import importlib
import subprocess
import re
import threading
import logging
from functools import partial

from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools

#from rigit.ui import rigit_log
#from rigit.ui import rigit_diffView
from rigit.cmd import gitCmd
from rigit.ui.widget import(
IconProvider,
CustomFileSystemModel,
CustomDelegate,
CustomListModel,
ProgressStatusBar
)
importlib.reload(gitCmd)


TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.split(__file__)[-1]


class RiGitMainUI(QtCore.QObject):
    gcmd = None
    def __init__(self, gcmd: gitCmd.RigitCmd):
        super(RiGitMainUI, self).__init__()
        self.setObjectName('RiGitMainUI')

        self.__summary = ""
        self.__comment = ""

        # TODO
        self.rootPath = "../../testLocalRepo"
        self.setGitPath(gcmd, self.rootPath)

        # set operator class
        self.Commit = Commit(self.gcmd)

        loader = QtUiTools.QUiLoader()
        ui_path = FILENAME.replace('.py', '.ui')
        self.ui = loader.load(ui_path, None)

        # set main QMainWindow .ui file
        self.setWidgets(self.ui)

        self.setupUi()

        self.setCallBack()

    def setupUi(self):
        self.initFileColumnView()
        self.summaryChanged()

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

        self.comment_textEdit  = ui.findChild(QtWidgets.QPlainTextEdit,
                                              "comment_textEdit")

        self.commit_pushButton = ui.findChild(QtWidgets.QPushButton,
                                              "commit_pushButton")

    def initMenuBar(self):
        pass

    def initStatusBar(self):
        pass

    def initFileColumnView(self):
        self.fileSys_model = CustomFileSystemModel()
        self.fileSys_model.setRootPath(self.rootPath)
        self.iconProvider = IconProvider()
        self.fileSys_model.setIconProvider(self.iconProvider)

        self.file_columnView.setModel(self.fileSys_model)
        self.file_columnView.setRootIndex(self.fileSys_model.index(self.rootPath))

        self.fileSys_delegate = CustomDelegate()
        self.file_columnView.setItemDelegate(self.fileSys_delegate)

        self.file_columnView.slectionModel()
        QtWidgets.QColumnView.selection

    def initFileLogListView(self):
        pass

    def setLineEdit2Summary(self):
        if not self.summary_lineEdit.text():
            self.summary = ""
        else:
            self.summary = self.summary_lineEdit.text()

    @property
    def summary(self):
        return self.__summary


    @summary.setter
    def summary(self, summary):
        self.__summary = summary

    def setPlaneText2Comment(self):
        if not self.comment_textEdit.toPlainText():
            self.comment = ""
        else:
            self.comment = self.comment_textEdit.toPlainText()

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment

    def setGitPath(self, gcmd, path: str):
        # self.SetPath_lineEdit
        self.gcmd = gcmd(path)

    def log(self, text: str):
        pass

    def loadSettings(self):
        pass

    def setCallBack(self):
        self.commit_pushButton.clicked.connect(
            lambda:self.Commit.add_commit(self.summary, self.comment)
            )
        self.commit_pushButton.clicked.connect(
            lambda:self.commitButtonPressed(self.Commit.commit_status)
            )

        self.summary_lineEdit.textChanged[str].connect(
            self.summaryChanged
            )

        self.comment_textEdit.textChanged.connect(
            self.commentChanged
            )
        """
        self.file_columnView.clicked.connect(
            self.fileItemClicked
            )
        """
        self.file_columnView.doubleClicked.connect(
            self.fileItemDoubleClicked
            )

    def fileItemClicked(self, index):
        filePath = self.fileSys_model.filePath(index)
        if os.path.isdir(filePath):
            self.iconProvider.isSelected = True
        else:
            self.iconProvider.isSelected = False
        self.fileSys_model.setIconProvider(self.iconProvider)

    def fileItemDoubleClicked(self, index):
        filePath = self.fileSys_model.filePath(index)
        if os.path.isfile(filePath):
            self.openFile(filePath)
        elif os.path.isdir(filePath):
            self.openDir(filePath)

    def fileItemSelectionChanged(self, selected, deselected):
        index =  ""

    def summaryChanged(self, *args):
        self.setLineEdit2Summary()
        summary = self.summary
        if summary == "":
            self.commit_pushButton.setEnabled(False)
        else:
            self.commit_pushButton.setEnabled(True)

    def commentChanged(self, *args):
        self.setPlaneText2Comment()

    def commitButtonPressed(self, *args):
        if args[0]:
            self.summary_lineEdit.clear()
            self.comment_textEdit.clear()

    def openFile(self, filePath):
        if os.name == 'nt':
            os.startfile(filePath)
        else:
            subprocess.call(['xdg-open', filePath])

    def openDir(self, dirpath):
        if os.name == 'nt':
            fileManager = 'explorer'
            path = re.sub('/', '\\\\', dirpath)
        elif os.name == 'posix':
            fileManager = 'nautilus'
            path = re.sub('\\\\', '/', dirpath)
        elif os.name == "mac":
            fileManager = 'open'
            path = re.sub('\\\\', '/', dirpath)
        subprocess.Popen([fileManager, path])

    def show(self):
        self.ui.show()


class Commit:
    def __init__(self, gcmd):
        self.gcmd = gcmd
        self.commit_status = False

    @staticmethod
    def connect_message(summary: str, comment: str) -> str:
        return summary + '\n' + comment

    def add_commit(self, summary: str, comment: str):
        message = self.connect_message(summary, comment)
        res_add_untracked  = self.gcmd.do_add_untracked()
        res_add_unstaged   = self.gcmd.do_add_unstaged()
        self.commit_status = self.gcmd.do_commit(message)
        print(res_add_untracked)
        print(res_add_unstaged)

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    RiGit = RiGitMainUI(gitCmd.RigitCmd)
    RiGit.show()
    sys.exit(app.exec_())