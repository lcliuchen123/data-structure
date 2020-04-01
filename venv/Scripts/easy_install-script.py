<<<<<<< HEAD
#!D:\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install'
__requires__ = 'setuptools==40.8.0'
=======
#!C:\Users\root\PycharmProjects\ML\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install'
__requires__ = 'setuptools==39.1.0'
>>>>>>> 81cfc891a3ffb45d34165a9d753bd467b7938854
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
<<<<<<< HEAD
        load_entry_point('setuptools==40.8.0', 'console_scripts', 'easy_install')()
=======
        load_entry_point('setuptools==39.1.0', 'console_scripts', 'easy_install')()
>>>>>>> 81cfc891a3ffb45d34165a9d753bd467b7938854
    )
