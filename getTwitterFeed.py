#!/usr/bin/python

import urllib2

def getTwitterSearchResults(hashtags=['galaxy', 'samsung', 's4']):
    response = urllib2.urlopen('http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd')
    print response.read()


if __name__ == "__main__":
    getTwitterSearchResults()

