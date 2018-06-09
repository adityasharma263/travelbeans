# -*- coding: utf-8 -*-

from flask_script import Command
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import os
from selenium import webdriver
from pyvirtualdisplay import Display
import time


class Driver:
    _chrome_options = webdriver.ChromeOptions()
    _chrome_options.add_argument("--disable-infobars")
    _firefox_profile = webdriver.FirefoxProfile()
    _firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

    def __init__(self):
        self.driver = webdriver.Chrome(os.path.realpath("") + '/chromedriver',
                                       chrome_options=self._chrome_options)

    def drive(self):
        return self.driver

class Trivago(Command):
    def run(self):
        urls = []
        domain_url = "https://www.trivago.in/"
        page = urllib.request.urlopen(domain_url).read()
        soup = BeautifulSoup(page)
        soup = soup.find(id="js-homepage-cities-body").find('ul')
        for li in soup.find_all('li'):
            urls.append(domain_url + li.find("a")['href'])
        # display = Display(visible=0, size=(1024, 768))
        # display.start()
        # browser = Driver().drive()
        # browser.get(urls[0])
        # time.sleep(6)
        city = urllib.request.urlopen(urls[0]).read()
        soup = BeautifulSoup(page)








