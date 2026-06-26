#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:44:09 2026

@author: eray
"""

import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "gemma4:e4b",
    "prompt": "Write a haiku about the ocean.",
    "stream": False
}

r = requests.post(url, json=payload, timeout=120)
r.raise_for_status()
data = r.json()

print(data["response"])