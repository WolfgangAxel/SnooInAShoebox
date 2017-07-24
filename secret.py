#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  secret.py
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

# Get your eBay ID here:
# https://developer.ebay.com/join/
# After registering, create a new keyset for production
# Copy the App ID value between the quotes
ebayID = ""

# Your personal account
# Only used for the user agent
# Do not include "/u/" or "u/"
botMasterRedditUsername = ""

# Follow these instructions if you don't have these already
# https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
redditUsername = ""
redditPassword = ""
redditClientID = ""
redditSecret = ""

# Do not include "/r/" or "r/"
mySubreddit = ""

numberOfItemsToFind = "10"

# Set up for /r/WondersOfChina
#
# Get the flair IDs for your sub by using the following in the
# python console after creating a `reddit` instance:
#
# for flair in reddit.subreddit('mysubreddit').flair.link_templates:
#     print(flair['text'], flair['id'])
#
# Get the eBay categoryIDs by making a request to:
# http://open.api.ebay.com/Shopping?callname=GetCategoryInfo&appid=YourAppID&version=967&siteid=0&CategoryID=-1&IncludeSelector=ChildCategories
#                                                           ^---------------^
# To allow for easy creation of hybrid categories, they
# should be formatted as an HTML request as follows:
# &categoryId=IDGoesHere
# The API allows for up to 3 category IDs to be specified
# To search more than one filter, simply add another to 
# the request:
# &categoryId=IDGoesHere&categoryId=IDGoesHere&categoryId=IDGoesHere
#               category ID                    flair ID
categories = (('&categoryId=1&categoryId=550','b9ad4746-674c-11e7-b145-0e7be617fce8'),  # collec. & art
              ('&categoryId=11700',           '3de826a2-674d-11e7-92e0-0e4bbfcf7e44'),  # home & garden
              ('&categoryId=888',             '64efb4fe-674d-11e7-b59d-0e71cfe1fcd6'),  # sport. eq.
              ('&categoryId=293',             '9256801e-674b-11e7-af65-0e2db3f4a38a'),  # cons. elec.
              ('&categoryId=281',             '23281b60-674d-11e7-ae96-0ee27ce3e272'),  # jewel & watch
              ('&categoryId=220',             'f03f5664-674c-11e7-a71a-0e6aef238bc8'),  # toy & hobby
              ('&categoryId=99',              '8c615844-674d-11e7-9c0b-0e809f8daee0'))  # everything else

# Set up for /r/WondersOfChina
#
# The URL filters you wish to pass through to the eBay API
# Learn about the formatting here:
# http://developer.ebay.com/devzone/finding/concepts/MakingACall.html#nvsyntax
#
# Learn about all available filters here:
# http://developer.ebay.com/devzone/finding/CallRef/types/ItemFilterType.html
filters = "&itemFilter(0).name=FreeShippingOnly&itemFilter(0).value=true&itemFilter(1).name=MaxPrice&itemFilter(1).value=3.00&itemFilter(2).name=LocatedIn&itemFilter(2).value=CN&itemFilter(2).value=SG&itemFilter(2).value=HK&itemFilter(2).value=MY"

# Change the bot's "signature", a la forums. It'd be appreciated to keep the GitHub link,
# but how am I to stop you from taking it out?
botSignature = (
"""

Happy shopping!

****

[^(I'm open source!)](https://github.com/WolfgangAxel/SnooInAShoebox)
""")
