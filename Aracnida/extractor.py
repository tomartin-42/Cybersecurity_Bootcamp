import requests
import re
from pwn import *
import os


class Extractor:
    file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']

    def  __init__(self, url, deep_lvl=99):
        self.url = url
        self.max_lvl = deep_lvl + 1
        self.url_to_visit = set()
        self.file_list = set()
        self.visit_list = set()
        self.url_to_visit.add(self.url)
        self.p1 = log.progress('Spider') 
        self._extract_urls(self.url_to_visit)
        
    def _extract_urls(self, list_to_scan):
        if len(list_to_scan) == 0 or self.max_lvl <= 0:
            return
        else:
            for e in list_to_scan:
                urls_in_text = []
                self.p1.status('Scanning: ' + e)
                self.visit_list.add(e)
                try:
                    r = requests.get(e)
                    urls_in_text = re.findall(
                        'https?://(?:[-\w.@#%]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,@-])', r.text)
                except:
                    print("[!] Error: Fail load " + e)
                    pass
                self._extract_files(urls_in_text)
            self.max_lvl -= 1
            self._extract_urls(urls_in_text)

    def _extract_files(self, list_):
        for e in list_.copy():
            if e.find(self.url) == -1:
                list_.remove(e)
                continue
            if os.path.splitext(e)[1] in self.file_include:
                self.file_list.add(e)
                list_.remove(e)

    def get_list_file(self):
        for e in self.file_list.copy():
            if not len(e):
                self.file_list.remove(e)
        return self.file_list

    def get_visit_list(self):
        return self.visit_list

    def get_url_to_visit(self):
        return self.url_to_visit
