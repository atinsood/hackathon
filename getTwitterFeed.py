#!/usr/bin/python

import urllib2
import json


def getTwitterSearchResults(
        url='http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd&rpp=100&page=1',
        hashtags=('galaxy', 'samsung', 's4')):

    response = urllib2.urlopen(url)
    jsonResponse = json.loads(response.read())
    print len(jsonResponse['results'])
    return jsonResponse['results']


def printResultsToFile(result, myFile):
    for item in result:
        myFile.write("TWITTER : " + item['text'].encode('ascii', errors='ignore'))
        myFile.write("\n")


if __name__ == "__main__":
    myFile = open('/Users/asood/work/opensource/play/bostonHackathon/hackathon/twitter.txt', 'a')
    url = 'http://search.twitter.com/search.json?q=%23samsung%20OR%20%23galaxys4%20lang%3Aen&src=typd&rpp=100&page='

    for i in range(1, 15):
        query = url + str(i)
        twitterResult = getTwitterSearchResults(query)
        printResultsToFile(twitterResult, myFile)

    myFile.close() 
