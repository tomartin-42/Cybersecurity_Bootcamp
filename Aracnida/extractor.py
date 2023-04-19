import requests
import re
from pwn import *
import os


class Extractor:
    file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']

    def __init__(self, url, deep_lvl=99):
        self.url = url
        self.max_lvl = deep_lvl + 1
        self.url_to_visit = set()
        self.file_list = set()
        self.visit_list = set()
        self.url_to_visit.add(self.url)
        p1 = log.progress('Spider') 
        flag = True
        while flag:
            prev = len(self.url_to_visit)
            for e in self.url_to_visit.copy():
                p1.status('Scaning URL: ' + e + '')
                tmp = self._get_one_url(e)
                if tmp != None:
                    self.file_list.update(self._extract_files(tmp))
                    for r in tmp:
                        self._extract_urls(r, e)
            post = len(self.url_to_visit)
            if prev == post:
                flag = False
        for e in self.file_list.copy():
            aux = os.path.splitext(e)[1]
            if aux not in self.file_include:
                self.file_list.remove(e)
        

    def _get_one_url(self, url, lvl=99):
        if url not in self.visit_list:
            self.visit_list.add(url)
            r = requests.get(url)
            urls = re.findall(
                'https?://(?:[-\w.@#%]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,@-])', r.text)
                #'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
            urls = set(urls)
            self._clean_up_urls(urls)
            for e in urls.copy(): # remove element if not in range
                if not self.in_range(e):
                    urls.remove(e)
            return urls 

    def _clean_up_urls(self, urls):
        for e in urls.copy():
            if e.find(self.url) == -1:
                urls.remove(e)


    def in_range(self, element):
        aux = element[len(self.url):]
        if aux.count('/') < self.max_lvl and aux.count('/') != -1:
            return True
        else:  # if not in range, delete
            return False

    def _extract_urls(self, element, head_str):
        if element == head_str:
            return 
        else:
            aux = element[len(head_str):]
            num = aux[1:].find('/')
            if num != -1:
                self.url_to_visit.add(element[:len(head_str) + len(aux[:num + 1])])
                self._extract_urls(element, element[:len(head_str) + len(aux[:num + 1])])

    def _extract_files(self, list_):
        aux = set()
        for e in list_.copy():
            tmp = e[len(self.url):]
            if re.search(r'\.[a-zA-Z0-9]{2,4}$', tmp):
                aux.add(e)
        return aux

    def get_list_file(self):
        for e in self.file_list.copy():
            if not len(e):
                self.file_list.remove(e)
        return self.file_list

    def get_visit_list(self):
        return self.visit_list

    def get_url_to_visit(self):
        return self.url_to_visit