#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:22:00 2026

@author: eray
"""

from wiki_dump_extractor import WikiXmlDumpExtractor, WikiAvroDumpExtractor

file = "/home/eray/Schreibtisch/wikiextract/enwiki/enwiki-2026-06-01-p10p1130124.xml"
out = "/home/eray/Schreibtisch/wikiextract/enwiki/enwiki-pages-p10p1130124.avro"
redirects_dir = "/home/eray/Schreibtisch/wikiextract/enwiki/enwiki_redirects-p10p1130124.lmdb"
index_dir="/home/eray/Schreibtisch/wikiextract/enwiki/indexes-p10p1130124.lmdb"


extractor = WikiXmlDumpExtractor(file_path=file)
ignored_fields = ["timestamp", "revision_id", "redirect_title"]
extractor.extract_pages_to_avro(
    output_file=out,
    redirects_db_path=redirects_dir,  # LMDB database for fast redirect lookups
    ignored_fields=ignored_fields,
)

# Create extractor
extractor = WikiAvroDumpExtractor(file_path=out)
extractor.index_pages(index_dir= index_dir)

extractor = WikiAvroDumpExtractor(file_path=out, index_dir=index_dir)


for page in extractor.iter_pages(500):
    print(page.title)