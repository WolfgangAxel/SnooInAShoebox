#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  SIASB.py
#  
#  Copyright 2017 Keaton Brown <linux.keaton@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
########################################################################

myPath = __file__.replace("SIASB.py","")
from sys import path
path.append(myPath)

import secret
import praw
from requests import get
from bs4 import BeautifulSoup as BS
from time import strftime


def getEbayResults():
    s = BS(get(url).content,'html.parser')
    results = {}
    for r in s.find_all('item'):
        price = r.sellingstatus.currentprice.text
        while len(price) < 4:
            price += '0'
        results[r.title.text.replace("[","\\[").replace("]","\\]")] = {'price':"$"+price,'url':r.viewitemurl.text}
    return results

def makePost():
    reddit = praw.Reddit(client_id=secret.redditClientID,
            client_secret=secret.redditSecret,
            password=secret.redditPassword,
            user_agent="Providing eBay links to /r/{} by /u/{}".format(secret.mySubreddit,secret.botMasterRedditUsername),
            username=secret.redditUsername)
    results = getEbayResults()
    title = "[BOT] Automatically generated items for {}, come discuss/review them!".format(strftime("%m-%d"))
    selftext = "\n".join([ "* {price} [{title}]({url})".format(price=results[result]['price'],title=result,url=results[result]['url']) for result in results ])
    reddit.subreddit(secret.mySubreddit).submit(title,selftext=selftext,flair_id=flair_id,send_replies=False)


cat,flair_id = secret.categories[eval(strftime("%w"))]

url = "http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={ID}&\
RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD=true&paginationInput.entriesPerPage={NUM}{cat}{filters}".format(ID=secret.ebayID,NUM=secret.numberOfItemsToFind,cat=cat,filters=secret.filters)

makePost()
