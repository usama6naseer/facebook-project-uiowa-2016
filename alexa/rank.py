#!/usr/bin/env python
import urllib, sys, bs4
print (bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ "official-liker.net").read(), "xml").find("REACH")['RANK'])