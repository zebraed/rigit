import sys
import os

__path__.append(os.path.join(__path__[0], 'python'))
__CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__CURRENT_DIR + '/submodules')

def reload():
    for k in sys.modules.keys():
        if k.find("rigit") > -1:
            del sys.modules[k]
    print("# Reload: rigit modules")