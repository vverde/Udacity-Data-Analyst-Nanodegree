#!/usr/bin/env python
# -*- coding: utf-8 -*-

# users.py
# Data Wrangling with MongoDB (Udacity.com)
# Project 3: OpenStreetMap Data Case Study
#
# Amodiovalerio Verde
# amodiovalerio.verde@gmail.com

import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return element.get('uid')

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
			users.add(get_user(element))
    return users

def test():
    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6

if __name__ == "__main__":
    test()