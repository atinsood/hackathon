#!/usr/bin/python

import urllib2
import json

def getTwitterSearchResults(url='http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd&rpp=100&page=1', hashtags=['galaxy', 'samsung', 's4']):
    response = urllib2.urlopen(url)
    jsonResponse = json.loads(response.read())
    return jsonResponse['results']


def printResutsToFile(result):
    myFile = open('/Users/asood/work/opensource/play/bostonHackathon/hackathon/twitter.txt', 'w')
    for item in result:
        myFile.write(item['text'].encode('ascii', errors='ignore'))
        myFile.write("\n")
    myFile.close() 

if __name__ == "__main__":
    url = 'http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd&rpp=100&page='
    for i in range(1,10):
        query = url + str(i)
        twitterResult = getTwitterSearchResults(query)
        printResutsToFile(twitterResult)
