# -*- coding:utf-8 -*-
import os.path
import os

def search(x):
    for x in os.listdir('.'):
        if os.path.isfile(x):
            print os.path.split(x)
        elif os.path.isdir(x):
            search(./x)

search()
