#!/usr/bin/env python

import requests

import sys, re

usage = "Usage: ytscrape.py URL1 [URL2 URL3 ...]\nExtract the YouTube links from a given page"

yturl_re = re.compile('"(http://(www\.)?(youtube.com|youtu.be)/[^"]+)"')

def main():
  if len(sys.argv) < 2:
    sys.stderr.write("%s\n" % (usage,))
    sys.exit(1)

  for urlbase in sys.argv[1:]:
    get_and_output(urlbase)

  sys.exit(0)


def get_and_output(url):
  sys.stderr.write("getting %s..." % (url,))
  r = requests.get(url)
  sys.stderr.write("%d\n" % (r.status_code,))

  if not r:
    return False

  for yturl_m in yturl_re.finditer(r.content):
    print yturl_m.group(1)

  return True


if __name__ == '__main__': main()
