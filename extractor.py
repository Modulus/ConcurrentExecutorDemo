# -*- coding: utf-8 -*-
import time

__author__ = 'Modulus'


class Extractor(object):

    @staticmethod
    def extract(start, end):
        time.sleep(5)
        return [x for x in range(start, end)]