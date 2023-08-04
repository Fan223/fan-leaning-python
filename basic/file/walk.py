import os

files = os.walk(os.getcwd())
for dirpath, dirname, filename in files:
    print(dirpath)
    print(dirname)
    print(filename)
