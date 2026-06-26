#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:40:21 2026

@author: eray
"""

import json

st1 = "/home/eray/Schreibtisch/wikiextract/enwiki/pages_first_dataset.json"
st2 = "/home/eray/Schreibtisch/wikiextract/enwiki/category_keys_first_dataset.json"

with open(st1, mode="r", encoding="utf-8") as read_file:
     pages = json.load(read_file)[::1000]