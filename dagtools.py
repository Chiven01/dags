#!/usr/bin/env python

import sys
import re

def alter(file):
    new_str = 'bash_command =\'sleep 10\''
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = re.sub(r'bash_command = \'sh .*\.sh {{tomorrow_ds_nodash}}\'', new_str ,line)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

file_path = sys.argv[1]
if file_path is None or len(file_path) == 0:
    print('there is no file_path')
    sys.exit()
# file_path = '..\\datas\\dag-example'
alter(file_path)
