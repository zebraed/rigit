import sys
import os
import signal
import time


try:
    import rigit.qtpy as qtpy
    #from rigit.qtpy import QtGui, QtWidgets, QtCore
    from PySide2 import QtGui, QtWidgets, QtCore
except ImportError:
    sys.stderr.write("")
    sys.exit(1)
import sys

# style note: we use camelCase here since we're masquerading a Qt class

# styleごとのカラー宣言わけ

class RigitQApplication(QtWidgets.QApplication):
    """
    QApplication implementation for handling custom events
    """
    def __init__(self, context, argv):
        super(RigitQApplication, self).__init__(argv)
        self.context = context

    def event(self, e):
        if e.type() == QtCore.QEvent.ApplicationActivate:
            context = self.context
            if context:
                cfg = context.cfg
                if context.git.is_valid() and cfg.get(
                    ""
                ):
                    pass
        return super(RigitQApplication, self).event(e)

    def commitData(self, session_mgr):
        """
        save session data
        """
        if not self.context or not self.context.view:
            return
        view = self.context.KeysView
        if not hasattr(view, "save_state"):
            return

        s_id = session_mgr.sessionId()
        s_key = session_mgr.sessionKey()
        session_id = "{0}_{1}".format(s_id, s_key)
        session = Session(session_id, repo=core.getcwd())
        session.update()
        view.save_state(settings=settion)


def new_context(args):
    """
    create top level applicationContext objects.
    """
    context = ApplicationContext(args)
    context.settings = args.settings or settings.read()
    context.git = git.create()


def create_qApp():
    if qtpy.__binding__ in ("PySide2", "PyQt5"):
        QtWidgets.QApplication.setStyle("Fusion")
        return QtWidgets.QApplication(sys.argv)
    else:
        QtWidgets.QApplication.setStyle("")


if __name__ == '__main__':
    gi = run()
    gi.show()
