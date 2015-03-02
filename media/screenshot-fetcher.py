#!/usr/bin/python
# -*- coding: utf-8 -*-

# screenshot-fetcher.py: fetch android/ios app screenshots from app stores
#
# Author: Tomi.Mickelsson@iki.fi

import os, sys
from lxml.html import parse
from urllib2 import urlopen

def fetch_ios_top_list(free_apps=True):
    " Fetch list of top ios apps "

    if free_apps:
        url = "http://www.apple.com/itunes/charts/free-apps/"
    else:
        url = "http://www.apple.com/itunes/charts/paid-apps/"

    doc = parse(url).getroot()
    grid = doc.get_element_by_id("grid")
    return [x.find("a").get("href") for x in grid.iter("li")]

def fetch_ios_app_shots(rank, url):
    " Fetch all screenshots of this iphone/ipad app "

    print "fetch app page", url

    doc = parse(urlopen(url)).getroot()

    # get title
    title = doc.xpath("//div[@id='title']//h1")[0].text
    print "TITLE", title

    # get iphone shots
    iphoneimg = doc.xpath("//div[contains(@class, 'iphone-screen-shots')]//img")
    for i, img in enumerate(iphoneimg):
        url = img.get("src")
#         if "landscape" in img.get("class"):
#             fname = "L-"+fname
        save_img(url, "iphone", rank, title, i)

    # get ipad shots
    ipadimg = doc.xpath("//div[contains(@class, 'ipad-screen-shots')]//img")
    for i, img in enumerate(ipadimg):
        url = img.get("src")
        save_img(url, "ipad", rank, title, i)


def fetch_android_top_list(free_apps=True):
    " Fetch list of app urls of top android apps "

    if free_apps:
        url = "https://play.google.com/store/apps/collection/topselling_free"
    else:
        url = "https://play.google.com/store/apps/collection/topselling_paid"

    # 2nd page:
    # https://play.google.com/store/apps/collection/topselling_free?start=24&num=24

    doc = parse(urlopen(url)).getroot()
    li = doc.xpath("//ul[contains(@class, 'snippet-list')]//li//a[contains(@class, 'thumbnail')]")
    return [x.get("href") for x in li]


def fetch_android_app_shots(rank, url):
    " Fetch all screenshots of this iphone/ipad app "

    if not url.startswith("http"):
        url = "https://play.google.com/" + url

    doc = parse(urlopen(url)).getroot()

    # get title
    title = doc.xpath("//h1[contains(@class, 'doc-banner-title')]")
    if title:
        title = title[0].text
    print "TITLE", title

    # get shots
    li = doc.xpath("//img[contains(@class, 'doc-screenshot-img')]")
    imglist = [x.get("src") for x in li]

    for i, url in enumerate(imglist):
        url = url.replace("h230", "h2000") # height of image
        save_img(url, "android", rank, title, i)


def save_img(url, dir, rank, title, imgindex):
    " Fetch an image from the url to a file "

    fname = "%s/%03d.%s_%d.jpg" % (dir, rank, title[:20], imgindex)
    fname = fname.replace(" ", "_")
    print "  ",fname

    f = urlopen(url)
    data = f.read()
    f.close()

    dest = file(fname, "wb")
    dest.write(data)
    dest.close()


def main():
    ostype = sys.argv[-1] # last arg

    # create dirs for downloaded screenshots
    dirs = ["android", "iphone", "ipad"]
    for d in dirs:
        if not os.path.exists(d):
            os.mkdir(d)

    free_apps = True

    if ostype == "android":
        # fetch android shots
        urllist = fetch_android_top_list(free_apps)
        print "android app count:", len(urllist)

        for i, url in enumerate(urllist):
            fetch_android_app_shots(i+1, url)
    elif ostype == "ios":
        # fetch ios shots
        urllist = fetch_ios_top_list(free_apps)[:50]
        print "ios app count:", len(urllist)

        for i, url in enumerate(urllist):
            fetch_ios_app_shots(i+1, url)
    else:
        print "unknown os"


if __name__ == '__main__':
    main()

