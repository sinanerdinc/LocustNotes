from bs4 import BeautifulSoup
import requests


class Blog(object):

    @staticmethod
    def url():
        r = requests.get("https://www.sinanerdinc.com/sitemap.xml")
        if r.status_code != 200:
            return False
        else:
            source = BeautifulSoup(r.content, "lxml")
            links = source.findAll("loc")
            return [(link.text).replace('http://www.sinanerdinc.com','') for link in links]
