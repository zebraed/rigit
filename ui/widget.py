#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>
import sys
import os
import logging

from PySide2 import QtCore, QtGui, QtWidgets

ICON_DIR = os.path.abspath(os.path.join(__file__, '../icons'))


class IconProvider(QtWidgets.QFileIconProvider):
    """
    custom icon provider settings for QFileSystemModel.
    """
    def __init__(self, *args):
        super(IconProvider, self).__init__()
        global ICON_DIR
        self.fbx_icon = QtGui.QPixmap(ICON_DIR + '/fbx.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.mb_icon = QtGui.QPixmap(ICON_DIR + '/mb24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.ma_icon = QtGui.QPixmap(ICON_DIR + '/ma24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.mel_icon = QtGui.QPixmap(ICON_DIR + '/mel24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.py_icon  = QtGui.QPixmap(ICON_DIR + '/python24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.dir_icon  = QtGui.QPixmap(ICON_DIR + '/folder24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.dirOpen_icon  = QtGui.QPixmap(ICON_DIR + '/folder_open24.png').scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)

        self.isSelected = False

    def icon(self, fileInfo):
        if fileInfo.isDir():
            if self.isSelected:
                return QtGui.QIcon(self.dirOpen_icon)
            else:
                return QtGui.QIcon(self.dir_icon)
        else:
            ext = fileInfo.suffix()
            if fileInfo.isFile():
                if ext == 'py':
                    return QtGui.QIcon(self.py_icon)
                elif ext == 'mel':
                    return QtGui.QIcon(self.mel_icon)
                elif ext == 'ma':
                    return QtGui.QIcon(self.ma_icon)
                elif ext == 'mb':
                    return QtGui.QIcon(self.mb_icon)
                elif ext == 'fbx':
                    return QtGui.QIcon(self.fbx_icon)
        return QtWidgets.QFileIconProvider.icon(self, fileInfo)


class CustomFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, *args):
        super(CustomFileSystemModel, self).__init__(*args)
        #self.setIconProvider(IconProvider())


class CustomDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(CustomDelegate, self).__init__(parent)

class CustomListModel(QtCore.QAbstractItemModel):
    pass

class ProgressStatusBar(QtWidgets.QProgressBar):
    pass

class PopupContext():
    pass