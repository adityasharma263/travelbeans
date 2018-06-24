# -*- coding: utf-8 -*-
__author__ = 'aditya'

from flask_script import Command
from cta.constants.website import Websites
from cta.model.hotel import Website


class SeedData(Command):

    def run(self):
        self.add_website()

    def add_website(self):
        for w in Websites:
            print(w)
            Website(website=w).save()
