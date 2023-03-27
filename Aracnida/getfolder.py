import requests

class GetTargets:
    def __init__(url, deep_lvl, targets = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']):
        self.url = url
        self.deep_lvl = deep_lvl
        self.target = targets

    def __get_text_url(url):
        self.r = request.get(url)


