# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rigit_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RigitWindow(object):
    def setupUi(self, RigitWindow):
        if not RigitWindow.objectName():
            RigitWindow.setObjectName(u"RigitWindow")
        RigitWindow.resize(302, 136)
        RigitWindow.setDocumentMode(False)
        self.centralwidget = QWidget(RigitWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.topLayout = QVBoxLayout(self.centralwidget)
        self.topLayout.setSpacing(5)
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setContentsMargins(5, 5, 5, 5)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.commit_pushButton = QPushButton(self.groupBox)
        self.commit_pushButton.setObjectName(u"commit_pushButton")
        self.commit_pushButton.setGeometry(QRect(10, 40, 271, 36))

        self.topLayout.addWidget(self.groupBox)

        RigitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RigitWindow)

        QMetaObject.connectSlotsByName(RigitWindow)
    # setupUi

    def retranslateUi(self, RigitWindow):
        RigitWindow.setWindowTitle(QCoreApplication.translate("RigitWindow", u"Rigit", None))
        self.groupBox.setTitle("")
        self.commit_pushButton.setText(QCoreApplication.translate("RigitWindow", u"Commit", None))
    # retranslateUi

