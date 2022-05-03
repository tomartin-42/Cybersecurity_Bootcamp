from argparse import ArgumentParser
import os
import sys
from os import scandir, getcwd

all_files = [None]
files = []

def list_files(dir_scan, files_extension):
    for nombre_directorio, dirs, ficheros in os.walk(dir_scan[0]):
        for nombre_fichero in ficheros:
            root, extension = os.path.splitext(nombre_fichero)
            if files_extension[0] == None: 
                files.append(nombre_directorio + '/' + nombre_fichero)
            else:
                if extension in files_extension:
                    files.append(nombre_directorio + '/' + nombre_fichero)

def main():
    parser = ArgumentParser()
    parser.add_argument("folder", nargs='+', type=str) 
    args = parser.parse_args()
    #Busca todos los files in folder
    if len(sys.argv) == 2:
        list_files(args.folder, all_files)
    else:
        all_files.pop(0)
        for extension in args.folder[1:]:
            all_files.append(extension)
        list_files(args.folder, all_files)

if __name__ == '__main__':
    main()
