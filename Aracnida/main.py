import requests
import re


def unmount_url(url, lvl):
    pass


def get_urls(url, urls, lvl=1):
    dic_urls = {url: lvl}
    for e in urls:
        if '/' in e[len(url):]:
            dic_urls[url + e[len(url):].split('/')[1]] = 2
  #  print(dic_urls)


def get_one_url(url):
    r = requests.get('https://www.cesif.es')
    regex = re.compile(
        r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])')
    urls = re.findall(regex, r.text)
    urls = set(urls)
    urls = list(urls)
    for e in urls:
        if url != e[0:len(url)]:
            urls.remove(e)
            continue
        print(e)
    return urls


if __name__ == '__main__':
    x = get_one_url('https://www.cesif.es/')
#    print(x)
    get_urls('https://www.cesif.es/', x)
