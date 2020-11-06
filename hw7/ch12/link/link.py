#!/usr/bin/env python3
''' Link Verification

Author: Kirk Walker
'''

import argparse
import requests
import bs4
from urllib.parse import urlparse, urljoin

url = set()

def verify_links(url):

    parsed = urlparse(url)

    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website links(url):

    urls = set()

    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
            
            continue

            href = urljoin(url, href)
            parsed_href = urlparse(href)

            href = parsed_href.scheme + "://" +parsed_href.netloc + parsed_href.path

            if not is_valid(href):
            
                continue

            if href in internal_urls:
                
                continue
            if domain_name not in href:
            
                if href not in external_urls:
                    print(f"{GRAY}[!] External link: {href}{RESET}")
                    external_urls.add(href)
                continue
            print(f"{GREEN}[*] Internal link: {href}{RESET}")
            urls.add(href)
            internal_urls.add(href)
        return urls

