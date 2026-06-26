#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:21:13 2026

@author: eray
"""

from wiki_dump_extractor import WikiXmlDumpExtractor, WikiAvroDumpExtractor, page_utils
import pandas as pd
import json

avro_file = "/home/eray/Schreibtisch/wikiextract/enwiki/enwiki-pages-p10p1130124.avro"
redirects_dir = "/home/eray/Schreibtisch/wikiextract/enwiki/enwiki_redirects-p10p1130124.lmdb"
index_dir = "/home/eray/Schreibtisch/wikiextract/enwiki/indexes-p10p1130124.lmdb"

extractor = WikiAvroDumpExtractor(file_path=avro_file, index_dir=index_dir)

count = 0
short_description = 0

wiki_df = pd.DataFrame(columns=["id", "title", "short_description", "geodata", "categories", "infobox_categories", "infobox"])

pages = []
category_keys = {}
for page in extractor.iter_pages(10):
    t = page.text
    short_description = page_utils.get_short_description(t)
    geodata = page_utils.extract_geospatial_coordinates(t)
    categories = page_utils.extract_categories(t)
    infobox = page_utils.extract_infobox_category(t)
    parsed_infobox, _ = page_utils.parse_infobox(t)
    title = page.title
    index = page.page_id
    pages.append([index, title, short_description, geodata, categories, infobox, parsed_infobox])
    
    for key in parsed_infobox.keys():
        if category_keys.get(key) == None:
            category_keys[key] = 0
        else:
            category_keys[key] += 1

#with open("/home/eray/Schreibtisch/wikiextract/enwiki/pages_first_dataset.json", mode="w", encoding="utf-8") as write_file:
#    json.dump(pages, write_file)
#with open("/home/eray/Schreibtisch/wikiextract/enwiki/category_keys_first_dataset.json", mode="w", encoding="utf-8") as write_file:
#    json.dump(category_keys, write_file)
    
