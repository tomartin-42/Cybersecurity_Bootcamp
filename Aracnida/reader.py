import os
import pyexiv2

class Reader:
    
    graphic_files = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    def __init__(self, file_list):
        self.info_list = []
        for file in file_list:
            file_type = os.path.splitext(file)[1]
            if file_type in self.graphic_files:
                self.read_graphic_file(file)
            elif file_type == '.docx':
                print(f'{file} is a docx file')
            elif file_type == '.pdf':
                print(f'{file} is a pdf file')
            else:
                print(f'{file} is not a correct file type')
                exit(1)

    def read_graphic_file(self, file):
        print(file)
        metadata = pyexiv2.ImageMetadata(file)
        metadata.read()

        for key in metadata.exif_keys:
            print(key, metadata[key].value)

