# # -*- coding: utf-8 -*-
# __author__ = 'aditya'
# from flask_script import Command
# from bs4 import BeautifulSoup
# import urllib.request
# import re
#
# # proxy = "YOUR_PROXY_GOES_HERE"
# # proxies = {"http": "http://%s" % proxy}
# # headers = {'User-agent': 'Mozilla/5.0'}
# # proxy_support = urllib2.ProxyHandler(proxies)
# # opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
# # urllib2.install_opener(opener)
# #
# # req = urllib2.Request(url, None, headers)
# # html = urllib2.urlopen(req).read()
# # print html
#
# class Trivago(Command):
#     def run(self):
#         domain_url = "https://www.trivago.in/"
#         page = urllib.request.urlopen(domain_url).read()
#         soup = BeautifulSoup(page)
#         soup = soup.find(id="js-homepage-cities-body").find('ul')
#         for li in soup.find_all('li'):
#             city = urllib.request.urlopen(domain_url + li.find("a")['href']).read()
#             soup = BeautifulSoup(city)
#             for a in soup.findAll("a", {"class": "top-category__link"}):
#                 star = a.find("div", {"class": "top-category__data top-category__data--rank"}).get_text()
#                 location = a.find("div", {"class": "top-category__data top-category__data--distance"}).get_text().strip()
#                 rating = a.find("div", {"class": "accommodation-rating__badge accommodation-rating__badge--index-color-5"}).get_text()
#                 wifi = a.find("div", {"class": "top-category__data--wifi"}).find("span", {"class": "wifi-features__feature-text"}).get_text()
#                 rating_lable = a.find("span", {"class": "accommodation-rating accommodation-rating__label"}).get_text()
#                 price = a.find("span", {"class": "top-category__price"}).get_text()
#                 obj = {
#                 "details": a["href"],
#                 "image": "http:"+a.find('img')['src'],
#                 "title": a.find('h4')['title'],
#                 "star": re.findall(r"(\d+)star", star.replace(" ", ""))[0],
#                 "distance": location if location else None,
#                 "rating": rating if rating else None,
#                 "wifi": wifi if wifi else None,
#                 "price": price if price else None,
#                 "location" : location.split(",")[0] if location else None,
#                 "rating_label": rating_lable if rating_lable else None
#                 }
#                 print(obj["title"])
#                 post = Stay(**obj)
#                 post.save()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
