#! /usr/bin/ python
# -*- coding:utf-8 -*-
# vim:fenc=utf-8
# name: utils.py
# Copyright 2020 otani <otani@P5830-006>
# Created: <2020-11-11>
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
try:
    from future_builtins import map
    from future_builtins import filter
except:
    pass

import os
import textwrap
import logging

CURRENT_DIR = os.path.dirname(__file__)

logger   = logging.getLogger(__name__)
handler  = logging.StreamHandler()
FILE_LOGLEVEL    = logging.DEBUG
CONSOLE_LOGLEVEL = logging.INFO


def get_log_path():
    username = os.environ.get("USER")
    return CURRENT_DIR + "/.log/" + username


class LogFormatter(logging.Formatter):
    """
    Foramtter description : return with formatter class's instance object.
    The instance is initialized with a formatting string for the message as a whole,
    and a formatting string for the date/time part of the message.

    """
    log_formats = (
        ('%(asctime)s', 'time(readable human)'),
        ('%(created)f', 'time (time.time())'),
        ('%(filename)s', 'file name'),
        ('%(funcName)s', 'function name'),
        ('%(levelname)s', 'name of logging level'),
        ('%(levelno)s', 'int value of logging level'),
        ('%(lineno)d', 'num of line'),
        # ('%(message)s', 'log message'),
        ('%(module)s', 'module name'),
        ('%(msecs)d', 'millisecond part of time (milliseconds)'),
        ('%(name)s', 'logger name'),
        ('%(pathname)s', 'file path name'),
        ('%(process)d', 'process ID (PID)'),
        ('%(processName)s', 'process name'),
        ('%(relativeCreated)d', 'logging time since load (milliseconds)'),
        ('%(thread)d', 'thread ID'),
        ('%(threadName)s', 'thread name'),
        )

    def __init__(self, width=90, padding=10, fmt=None, datefmt=None):
        super(LogFormatter, self).__init__(fmt, datefmt)
        self.width   = width
        self.padding = padding

    def wrap(self, msg, pad):
        """
        Wrapped logging message.
        """
        wrapped = textwrap.wrap(msg, self.width - self.padding)
        return ['{0}{1}'.format(pad, ln) for ln in wrapped]

    def format(self, record):
        """
        custom format func.
        """
        if record.levelno < logging.WARNING:
            res = record.msg
        else:
            res = '{0} : [{1}] : {2}\n'.format(record.levelname,
                                              self.formatTime(record),
                                              record.pathname,
                                              )
            res += '{}\n'.format(record.msg)

        return res


class Logger(object):
    """
    Custom Logger.

    """
    global FILE_LOGLEVEL
    global CONSOLE_LOGLEVEL

    def __init__(self, name):
        self.path = get_log_path()

        # set main log lebel from global logging root.
        self.level = FILE_LOGLEVEL

        self.logger      = None
        self.console     = None
        self.log_file    = None
        self.fileHandler = None

        self.logger = logging.getLogger(name)
        self.set_file(self.path, name)

        if not self.logger.handlers:
            hdl = logging.StreamHandler()
            self.setHandler(hdl)

        self.logger.propagate = False


    def setHandler(self, handler):
        self.console = handler

        self.logger.setLevel(self.level)

        self.console.setFormatter(LogFormatter())

        self.console.setLevel(CONSOLE_LOGLEVEL)
        self.logger.addHandler(self.console)

        self.set_fileHandler()

    def getLogger(self):
        return self.logger

    def set_file(self, path, name):
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.access(path, os.W_OK):
            print('[Logging Error]: Can not write to directory {}'.format(path))
            return None

        self.log_file = path + "/" + name

    def set_fileHandler(self):
        """
        set fileHandler to logger.
        """
        if not self.log_file is None:
            self.fileHandler = logging.FileHandler('{}.log'.format(self.log_file))
            self.logger.addHandler(self.fileHandler)