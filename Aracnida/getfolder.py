import requests
import re


class GetTargets:
    file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']

    def __init__(self, url, deep_lvl=5):
        self.url = url
        self.max_lvl = deep_lvl
        self.url_to_visit = set()
        self.file_list = set()
        self.visit_list = set()
        temp = self._get_one_url(self.url)
        file_list = self._extract_files(temp, self.url)
        self.url_to_visit = self._extract_urls(temp)
        self.url_to_visit.add(self.url)
        while True:
            for e in self.url_to_visit:
                if e not in self.visit_list:
                    temp = self._get_one_url(e)
                    file_list.difference(self._extract_files(
                        temp, 'https://www.cesif.es'))
                    tmp_visit = self._extract_urls(temp)
                    break
            self.url_to_visit.difference(tmp_visit)
            if self.visit_list == self.url_to_visit:
                break

    def _get_one_url(self, url, lvl=0):
        urls_list = {}
        if url not in self.visit_list:
            self.visit_list.add(url)
            r = requests.get(url)
            urls = re.findall(
                'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
            urls = set(urls)
            urls = list(urls)
            self._clean_up_urls(url, urls)
            for e in urls:
                self._recursive_get_partials_url(url, e, lvl, urls_list)
            self._delete_no_accept_files(url, urls_list)
            return urls_list

    def _clean_up_urls(self, url, urls):
        for e in urls:
            if url != e[0:len(url)]:
                urls.remove(e)
        for e in urls:
            if e.find(url) == -1:
                urls.remove(e)

    def _recursive_get_partials_url(self, main_url, complete_url, lvl, urls_list):
        if lvl >= self.max_lvl or main_url[:-1] == complete_url:
            return
        else:
            aux = complete_url[len(main_url):]
            add_str = aux.split('/')[0]
            urls_list[main_url + add_str] = lvl + 1
            self._recursive_get_partials_url(main_url + add_str + '/',
                                             complete_url, lvl + 1, urls_list)

    def _delete_no_accept_files(self, url, urls_list):
        for e in urls_list.copy():
            del_file = True
            if e.find('.', len(url)) != -1:  # check if file
                for f in self.file_include:  # check if include file
                    if e.find(f) != -1:
                        del_file = False
                        break
                if del_file is True:  # delete if not include file
                    urls_list.pop(e)

    def _extract_urls(self, urls_list):
        aux = set()
        for e in urls_list:
            aux.add(e)
        return aux

    def _extract_files(self, urls_list, url):
        aux = set()
        for e in urls_list.copy():
            if re.search(r'\.[a-zA-Z0-9]{2,4}$', e) and e != url:
                urls_list.pop(e)
                aux.add(e)
        return aux

    def get_list_file(self):
        return self.file_list
