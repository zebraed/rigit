import sys
import os

__path__.append(os.path.join(__path__[0], 'python'))

def reload():
    for k in sys.modules.keys():
        if k.find("rigit") > -1:
            del sys.modules[k]
    print("# Reload: rigit modules")

if __name__ == '__main__':
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    win = RigitMainUI(gitCmd.RigitCmd)
    win.show()
    sys.exit(app.exec_())