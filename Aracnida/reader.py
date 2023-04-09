import os
import piexif
from PIL import Image

class Reader:
    
    graphic_files = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    def __init__(self, file_list):
        self.info_list = []
        for file in file_list:
            file_type = os.path.splitext(file)[1]
            file_complet = os.getcwd() + '/' + file
            if file_type in self.graphic_files:
                self.read_graphic_file(file_complet)
            elif file_type == '.docx':
                print(f'{file} is a docx file')
            elif file_type == '.pdf':
                print(f'{file} is a pdf file')
            else:
                print(f'{file} is not a correct file type')
                exit(1)

    def read_graphic_file(self, file):
        image = Image.open(file)
        exif = image._getexif()

        if exif is not None:
            for tag, value in exif.items():
                print(f"{tag}: {value}")
        else:
            print("La imagen no tiene datos exif.")

