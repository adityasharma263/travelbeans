# -*- coding: utf-8 -*-
__author__ = 'aditya'

from flask_script import Command
from xlrd import open_workbook
import os
from cta.model.hotel import Website


class SeedData(Command):
    def run(self):
        wb = open_workbook(os.path.realpath("") + '/websites.xls')
        worksheet = wb.sheet_by_index(0)
        keys = [v.value for v in worksheet.row(0)]
        for row_number in range(worksheet.nrows):
            if row_number == 0:
                continue
            row_data = {}
            for col_number, cell in enumerate(worksheet.row(row_number)):
                row_data[keys[col_number]] = cell.value
                for k in row_data:
                    if row_data[k] is "":
                        row_data[k] = None
            post = Website(**row_data)
            post.save()