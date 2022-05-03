from argparse import ArgumentParser
import os
import sys
from os import scandir, getcwd

all_files = ('.*')
files = []
dirs = []

def ls(exten, ruta = getcwd()):
    aux = [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
    for a in aux:
        a = str(a)
        if os.path.splitext(a)[1] in exten:
            files.append(a)

def main():
    parser = ArgumentParser()
    parser.add_argument("folder", nargs='+', type=str) 
    args = parser.parse_args()
    if len(sys.argv) == 2:
        for elem in os.walk(args.folder[0]):
            dirs.append(elem)
        print(dirs)
        for sub_d in dirs:
            #print(type(sub_d))
            ls(all_files, str(sub_d))
        #Busca todos los files in folder
    else:
        print("more than one")
        #print(args)
        #Busca solo los files con le extensión

if __name__ == '__main__':
    main()
