import os

dir = os.environ['HOME']
dir += '/infection'

files = []
"""with os.scandir(dir) as ficheros:
    subdirectorios = [fichero.name for fichero in ficheros if fichero.is_dir()]
"""
if not os.path.exists(dir):
    print("[🚨] Folder /infection not found!!!")
    quit(1)

for elem in os.walk(dir):
    for fichero in elem[0].iterdir():
        files.append(fichero)       
print (files)
