#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
from __future__ import annotations
import sys
import os
import logging

from PySide2 import QtCore, QtGui, QtWidgets

ICON_DIR = os.path.abspath(os.path.join(__file__, '../icons'))


class CustomFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, *args):
        super(CustomFileSystemModel, self).__init__(*args)

        global ICON_DIR

        self.fbx_icon = QtGui.QPixmap(ICON_DIR + 'fbx.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.mb_icon = QtGui.QPixmap(ICON_DIR + 'mb24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.ma_icon = QtGui.QPixmap(ICON_DIR + 'ma24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.mel_icon = QtGui.QPixmap(ICON_DIR + 'mel24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.py_icon  = QtGui.QPixmap(ICON_DIR + 'python24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.dir_icon  = QtGui.QPixmap(ICON_DIR + 'folder24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

    def data(self, index, role):
        if role == QtCore.Qt.DecorationRole:
            fileInfo = QtCore.QFileInfo(index.data())
            # if fileInfo.isDir():
            #    return self.dir_icon
            ext = fileInfo.suffix()
            if ext == 'py':
                return self.py_icon
            elif ext == 'mel':
                return self.mel_icon
            elif ext == 'ma':
                return self.ma_icon
            elif ext == 'mb':
                return self.mb_icon
            elif ext == 'fbx':
                return self.fbx_icon
        return super(CustomFileSystemModel, self).data(index, role)

class CustomDelegate(QtWidgets.QStyledItemDelegate):
    pass

class CustomListModel(QtCore.QAbstractItemModel):
    pass

class ProgressStatusBar(QtWidgets.QProgressBar):
    pass