# -*- coding: utf-8 -*-

from flask_script import Command
from cta.model.stay import Stay
from bs4 import BeautifulSoup
import urllib.request
import re
# import os
# from selenium import webdriver
# from pyvirtualdisplay import Display
# import time


# class Driver:
#     _chrome_options = webdriver.ChromeOptions()
#     _chrome_options.add_argument("--disable-infobars")
#     _firefox_profile = webdriver.FirefoxProfile()
#     _firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
#
#     def __init__(self):
#         self.driver = webdriver.Chrome(os.path.realpath("") + '/chromedriver',
#                                        chrome_options=self._chrome_options)
#
#     def drive(self):
#         return self.driver
class Trivago(Command):
    def run(self):
        domain_url = "https://www.trivago.in/"
        page = urllib.request.urlopen(domain_url).read()
        soup = BeautifulSoup(page)
        soup = soup.find(id="js-homepage-cities-body").find('ul')
        for li in soup.find_all('li'):
            city = urllib.request.urlopen(domain_url + li.find("a")['href']).read()
            soup = BeautifulSoup(city)
            for a in soup.findAll("a", {"class": "top-category__link"}):
                star = a.find("div", {"class": "top-category__data top-category__data--rank"}).get_text()
                location = a.find("div", {"class": "top-category__data top-category__data--distance"}).get_text().strip()
                obj = {
                "details": a["href"],
                "image": "http:"+a.find('img')['src'],
                "title": a.find('h4')['title'],
                "star": re.findall(r"(\d+)star", star.replace(" ", ""))[0],
                "distance": location,
                "rating": a.find("div", {"class": "accommodation-rating__badge accommodation-rating__badge--index-color-5"}).get_text() if a.find("div", {"class": "accommodation-rating__badge accommodation-rating__badge--index-color-5"}) else None,
                "wifi": a.find("div", {"class": "top-category__data--wifi"}).find("span", {"class": "wifi-features__feature-text"}).get_text() if a.find("div", {"class": "top-category__data--wifi"}).find("span", {"class": "wifi-features__feature-text"}) else None,
                "price": a.find("span", {"class": "top-category__price"}).get_text(),
                "location" : location.split(",")[0],
                "rating_label": a.find("span", {"class": "accommodation-rating accommodation-rating__label"}).get_text()
                }
                print(obj)
                post = Stay(**obj)
                post.save()















