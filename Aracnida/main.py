import requests
import re

file_include = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.docx', '.pdf']
file_list = []
# urls_list = {'https://www.cesif.es': 1}
urls_list = {}
max_lvl = 7


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


def recursive_get_partials_url(main_url, complete_url, lvl):
    if lvl >= max_lvl or main_url[:-1] == complete_url:
        return
    else:
        aux = complete_url[len(main_url):]
        add_str = aux.split('/')[0]
        urls_list[main_url + add_str] = lvl + 1
        recursive_get_partials_url(main_url + add_str + '/',
                                   complete_url, lvl + 1)


def get_one_url(url, lvl=0):
    r = requests.get('https://www.cesif.es')
    urls = re.findall(
        'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
    urls = set(urls)
    urls = list(urls)
    for e in urls:
        if url != e[0:len(url)]:
            urls.remove(e)
    for e in urls:
        if e.find(url) == -1:
            urls.remove(e)
    for e in urls:
        recursive_get_partials_url(url, e, lvl)
    delete_no_accept_files(url, urls_list)
    return urls


if __name__ == '__main__':
    x = get_one_url('https://www.cesif.es')
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres/cuatro/cinco', 1)
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres', 1)
    # recursive_get_partials_url('https://www.cesif.es', 'https://www.cesif.es/uno/dos/tres/kk.gif', 0)
    # print(urls_list)
    for e in urls_list:
        print(e, urls_list[e])
