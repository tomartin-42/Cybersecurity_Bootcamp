from argparse import ArgumentParser
import os
import sys
from os import scandir, getcwd
import pathlib


all_files = [None]
files = []

def print_services():
    bin_path = pathlib.Path(__file__).parent.absolute()
    service_name = "/etc/systemd/system/irondome.service"
    arg_files = str()
    for part in files:
        arg_files += str(part)
        arg_files += " " 
    with open(service_name, "w") as archivo:
        archivo.write("[Unit]\nDescription=Irondome service\n\n")
        archivo.write("[Service]\nExecStart=" + str(bin_path) + "/irondome " + arg_files) 
    archivo.close()

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
    print_services()

if __name__ == '__main__':
    main()
