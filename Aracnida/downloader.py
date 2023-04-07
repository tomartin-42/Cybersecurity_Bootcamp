import requests

class Downloader:

    def __init__(self, file_list, path):
        self.download_list = {f"{path}{i:04}{file}": file for i, file in enumerate(file_list)}
        print(self.download_list)