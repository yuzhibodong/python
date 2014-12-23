import os
import sys
import re

def search(string):
    for dirpath, dirnames, filenames in os.walk(os.path.abspath('.'), True, None):
        for filename in filenames:
            if re.search(string, filename):
                print os.path.join(dirpath, filename)

search(sys.argv[1])
