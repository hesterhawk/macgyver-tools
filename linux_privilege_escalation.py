# Linux Password Finder v 1.0
#
#

import os

dirs = ['etc', 'home', 'var/log', 'var/www', 'opt']
files = ['cfg', 'php', 'inc', 'log', 'txt', 'ini']

command = "grep -Ri password $(find /{} -name '*.{}' 2>/dev/null)"

for dir in dirs:
    for file in files:
        t_command = command.format(dir, file)
        print("-----------\r\nDIRECTORY: {}\r\nFILE: {}\r\nCOMMAND: {}\r\n".format(dir, file, t_command))

        os.system(t_command)
