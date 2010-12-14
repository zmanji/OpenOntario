#!/usr/bin/env python
from __future__ import print_function
from lxml import html, etree
import urllib
import datetime


REQUEST_URL = "http://hansardindex.ontla.on.ca/H2vers2.asp"
#utility function to get hansard url given a date
def get_hansard_url_by_date(date):
    #build the request
    request = (("DateFrom", date.day),("MonthFrom", date.month),
            ("YearFrom", date.year),("stype",1))
    #execute the search via urlopen and get a response
    response = urllib.urlopen(REQUEST_URL,urllib.urlencode(request))
    #turn the response into html for parsing
    page = html.parse(response)
    
    root = page.getroot()

    noResult = False
    for b in root.cssselect('body'):
        if(b.text and b.text.find("No documents matched the query") != -1):
            noResult = True

    if(noResult):
        print("No Search result for " + date.isoformat())
        return None

    #everything important in this page is enclosed in the <p> tags
    oneResult = False
    for p in root.cssselect('p'):
        if(p.text and p.text.find("Documents 1 to 1 of 1 matching the query")):
            oneResult = True
    if(not oneResult):
        print("Many search results for " + date.isoformat())
        return None

    #if there is one result, lets get the url to return

    for a in root.cssselect('a'):
        if(a.get("href").find("hansardeissue") != -1):
            return "http://hansardindex.ontla.on.ca" + a.get("href")


if __name__ == '__main__':
    start = datetime.date(1981,04,20)

    for d in (start + datetime.timedelta(n) for n in range(10830)):
        r = get_hansard_url_by_date(d)
        if r:
            print("For " + d.isoformat() + ": " + r)

