# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import os
def get_file_name(dir):
    file_name = []
    for i in os.listdir(dir):
        if os.path.isdir(i):
            get_file_name()
        else:
            file_name.append(i)
    return file_name


dir = '/Users/gravel'
print(get_file_name(dir))
