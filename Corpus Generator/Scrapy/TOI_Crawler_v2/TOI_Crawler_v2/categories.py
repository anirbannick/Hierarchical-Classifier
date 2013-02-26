# categories.py

import os

def init():
    global category
    category = {}
    cwd = os.getcwd()
    if cwd.find("spiders") == -1:
        cwd = cwd + "/" + "spiders" + "/"
    f = open(cwd+"categories","r")
    for i in f.readlines():
        if i not in category.keys():
            category[i[:-1]] = 0
    category.pop("")
