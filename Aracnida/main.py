import requests
import re

file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']
file_list = []
# urls_list = {'https://www.cesif.es': 1}
max_lvl = 7
url_to_visit = set()
file_list = set()
visit_list = set()


def extract_urls(urls_list):
    aux = set()
    for e in urls_list:
        aux.add(e)
    return aux


def extract_files(urls_list):
    aux = set()
    for e in urls_list.copy():
        if re.search(r'\.[a-zA-Z0-9]{2,4}$', e):
            urls_list.pop(e)
            aux.add(e)

    return aux


def delete_no_accept_files(url, urls_list):
    for e in urls_list.copy():
        del_file = True
        if e.find('.', len(url)) != -1:  # check if file
            for f in file_include:  # check if include file
                if e.find(f) != -1:
                    del_file = False
                    break
            if del_file is True:  # delete if not include file
                urls_list.pop(e)


def recursive_get_partials_url(main_url, complete_url, lvl, urls_list):
    if lvl >= max_lvl or main_url[:-1] == complete_url:
        return
    else:
        aux = complete_url[len(main_url):]
        add_str = aux.split('/')[0]
        urls_list[main_url + add_str] = lvl + 1
        recursive_get_partials_url(main_url + add_str + '/',
                                   complete_url, lvl + 1, urls_list)


def clean_up_urls(url, urls):
    for e in urls:
        if url != e[0:len(url)]:
            urls.remove(e)
    for e in urls:
        if e.find(url) == -1:
            urls.remove(e)


def get_one_url(url, lvl=0):
    urls_list = {}
    if url not in visit_list:
        visit_list.add(url)
        r = requests.get(url)
        urls = re.findall(
            'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
        urls = set(urls)
        urls = list(urls)
        clean_up_urls(url, urls)
        for e in urls:
            recursive_get_partials_url(url, e, lvl, urls_list)
        delete_no_accept_files(url, urls_list)
        # extract_files(urls_list)
        # extract_urls(urls_list)
        return urls_list


if __name__ == '__main__':
    temp = get_one_url('https://www.cesif.es')
    file_list = extract_files(temp)
    url_to_visit = extract_urls(temp)
    while True:
        for e in url_to_visit:
            if e not in visit_list:
                temp = get_one_url(e)
                file_list.difference(extract_files(temp))
                tmp_visit = extract_urls(temp)
                break
        prev = len(url_to_visit)
        url_to_visit.difference(tmp_visit)
        second = len(url_to_visit)
        if prev == second:
            break

    # for e in urls_list.copy():
    #    get_one_url(e, urls_list[e])
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres/cuatro/cinco', 1)
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres', 1)
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres/kk.gif', 0)
    # print(urls_list)
    print(file_list)
    print("URLS: ")
    print()
    print()
    print()
    print(url_to_visit)
