#!/usr/bin/python

import urllib2
import json

def getTwitterSearchResults(hashtags=['galaxy', 'samsung', 's4']):
    response = urllib2.urlopen('http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd')
    jsonResponse = json.loads(response.read())
    return jsonResponse['results']


def printResutsToFile(result):
    myFile = open('/Users/asood/work/opensource/play/bostonHackathon/hackathon/twitter.txt', 'w')
    for item in result:
        myFile.write(item['text'])
        myFile.write("\n")
    myFile.close() 

if __name__ == "__main__":
    twitterResult = getTwitterSearchResults()
    printResutsToFile(twitterResult)
