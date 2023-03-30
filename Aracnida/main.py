import requests
import re

def get_one_url():
    url = 'https://www.cesif.es/'
    r = requests.get('https://www.cesif.es')
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*(?:\?[\w\d%&=]*)?(?:#[\w\d-]*)?(?<![\.,])', r.text)
    urls = set(urls)
    urls = list(urls)
    for e in urls: 
        if url not in e:
            urls.remove(e)
            continue
    print(urls)

if __name__ == '__main__':
    get_one_url()
