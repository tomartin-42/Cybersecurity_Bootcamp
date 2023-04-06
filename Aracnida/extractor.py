import requests
import re
from pwn import *
import time


class Extractor:
    file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']

    def __init__(self, url, deep_lvl=5):
        self.url = url
        self.max_lvl = deep_lvl + 1
        self.url_to_visit = set()
        self.file_list = set()
        self.visit_list = set()
        #temp = self._get_one_url(self.url)
        #self.file_list.update(self._extract_files(temp))
        #self.visit_list.add(self.url)
        self.url_to_visit.add(self.url)
        p1 = log.progress('Spider') 
        #for e in temp:
        #   self._extract_urls(e, self.url)
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
            print((prev, post))
            if prev == post:
                flag = False
        """
        file_list = self._extract_files(temp, self.url)
        self.url_to_visit = self._extract_urls(temp)
        self.url_to_visit.add(self.url)
        while True:
            for e in self.url_to_visit:
                if e not in self.visit_list:
                    p1.status('Scaning URL: ' + e + '')
                    temp = self._get_one_url(e)
                    tmp_visit = self._extract_urls(temp)
                    file_tmp = self._extract_files(temp, self.url)
                    self.file_list.update(file_tmp)
                    #self.file_list.update(self._extract_files(
                    #    temp, self.url))
                    # print("filelist ", self.file_list)
                    break
            try:
                self.url_to_visit.update(tmp_visit)
                if self.visit_list == self.url_to_visit:
                    break
            except:
                break
        """

    def _get_one_url(self, url, lvl=0):
        if url not in self.visit_list:
            self.visit_list.add(url)
            r = requests.get(url)
            urls = re.findall(
                'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
            urls = set(urls)
            self._clean_up_urls(url, urls)
            for e in urls.copy(): # remove element if not in range
                if not self.in_range(e):
                    urls.remove(e)
            return urls 

    def _clean_up_urls(self, url, urls):
        for e in urls.copy():
            if e.find(url) == -1:
                urls.remove(e)


    def in_range(self, element):
        aux = element[len(self.url):]
        if aux.count('/') < self.max_lvl and aux.count('/') != -1:
            return True
        else:  # if not in range, delete
            return False
    """
    def _recursive_get_partials_url(self, main_url, complete_url, lvl, urls_list):
        if lvl >= self.max_lvl or main_url == complete_url:
            return
        else:
            slash = '/'
            aux = complete_url[len(main_url):]
            if aux.find('/') != -1:
                add_str = aux[aux.find('/') + 1:]
            else:
                add_str = ''
            urls_list[main_url + add_str] = lvl + 1
            self._recursive_get_partials_url(main_url + add_str, complete_url, lvl + 1, urls_list)
    """

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
        return self.file_list

    def get_visit_list(self):
        return self.visit_list

    def get_url_to_visit(self):
        return self.url_to_visit