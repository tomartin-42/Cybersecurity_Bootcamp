import requests
from multiprocessing.pool import ThreadPool
from pwn import *
import os
from tqdm import tqdm

class Downloader:

    def __init__(self, file_list, visit_list, path):
        self.path = os.getcwd() + '/' + path
        self.download_list = {f"{self.path}{i:04}_{self.extract_file_name(file)}": file for i, file in enumerate(file_list)}
        try:
            os.makedirs(self.path, exist_ok=True)
            with open(path + "download.txt", 'w') as f:
                for e in file_list:
                    f.write(e + '\n')
            with open(path + "visit.txt", 'w') as f:
                for e in visit_list:
                    f.write(e + '\n')
            self.multi_download()
        except:
            print('Error in download')
            exit(1)

    def extract_file_name(self, url):
        return url.split('/')[-1]

    def download(self, path_file, url_file):
        p1 = log.progress('Download')
        r = requests.get(url_file)
        with open(path_file, 'wb') as f:
            p1.status(f'Downloading {path_file}')
            f.write(r.content)

    def multi_download(self, tread=20):
        pool = ThreadPool(tread)
        pool.starmap(self.download, self.download_list.items())
        pool.close()
        pool.join()