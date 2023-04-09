import os
import json
import subprocess

class Reader:
    file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']

    def __init__(self, file_list):
        self.info_list = []
        for file in file_list:
            file_type = os.path.splitext(file)[1]
            file_complet = os.getcwd() + '/' + file
            if not os.path.exists(file_complet):
                print(f'[!] {file} does not exist')
            elif file_type in self.file_include:
                self.info_list.append(self.read_graphic_file(file_complet))
            else:
                print(f'{file} is not a correct file type')
        print("Info list: ", self.info_list)

    def read_graphic_file(self, file):
        output = subprocess.check_output(['exiftool', '-j', file])
        tmp = output.decode()[1:-2]
        return json.loads(tmp)
    
    def get_info_list(self):
        return self.info_list

class Alterator:
    pass