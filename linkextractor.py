#!/usr/bin/env python

import requests
import json

def extract_links():
    apikey = "LIVDSRZULELA"
    search_term = "excited"
    r = requests.get("http://ip172-18-0-32-cjudluksnmng00f2od1g-5200.direct.labs.play-with-docker.com/pizzainfo")
    links = []
    
    if r.status_code == 200:
        links = json.loads(r.content)
   
    return links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(sys.argv[-1]):
        print("[{}]({})".format(link["text"], link["href"]))
