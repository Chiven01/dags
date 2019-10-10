#!/usr/bin/env python

import sys
import re

def alter(file):
    new_str = 'bash_command =\'sleep 120\''
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
#            line = re.sub(r'bash_command = \'sh .*\.sh {{tomorrow_ds_nodash}}\'', new_str ,line)
            line = re.sub(r'bash_command =\'sleep 10\'', new_str ,line)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def copydag(num=1):
    file='thour10.py'
    for i in range(num):
        new_str = 'thour%s' % (10+1+i)
        newFile = new_str + '.py'
        print("new_str=%s, newFile=%s" % (new_str, newFile))
        file_data = ""
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line = re.sub(r'thour10', new_str ,line)
                file_data += line
        with open(newFile,"w",encoding="utf-8") as f:
            f.write(file_data)

#file_path = sys.argv[1]
#if file_path is None or len(file_path) == 0:
#    print('there is no file_path')
#    sys.exit()
#alter(file_path)
copydag(50)
