#! /usr/bin/ python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 2021 otani  <otani@T5810-065>
# Created: <2021-09-01>

import sys
import os
import time
import re

sys.dont_write_bytecode = True

app_name = os.path.splitext(os.path.basename(__file__))[0]

# style note: we use camelCase here since we're masquerading a Qt class
class RigitApplication(object):
    """
    Main rigit application class.
    """
    def __init__(self, qtApp, splash=None):
        super(RigitApplication, self).__init__()

        self.context = context

        self._qtApp = qtApp
        self._qtApp.setWindowIcon()


        if splash:
            #splash screen
            pass

    def activeWindow(self):
        return self._qApp.activeWindow()

    def desktop(self):
        return self._qtApp.desktop()

    def start(self):
        """
        wrap command for exec_() and start app
        """
        ctx = self.context
        monitor = ctx.fsmonitor
        monitor.files_canged.connect()

    def stop(self):
        """finalize app"""

        try:
            del self._qtApp
        except(AttributeError, RuntimeError):
            pass
        self._qtApp = None

    def exit(self, status):
        return self._qtApp.exit(status)
