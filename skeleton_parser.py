"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import locale
import sys
from json import *
from pprint import pprint
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', \
          'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

"""
Returns true if a file ends in .json
"""


def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'


"""
Converts month to a number, e.g. 'Dec' to '12'
"""


def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon


"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""


def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]


"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""


def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)


def item_iterator(item, seller_set, bidder_set, bid_set, item_set):
    id = item.get("ItemID")
    name = item.get("Name")
    category = ''.join(item.get("Category"))
    buy = item.get("Buy_Price")
    if (buy is None):
        buy = "NULL"
    first = item.get("First_Bid")
    currently = item.get("Currently")
    seller_entry = item.get("Seller")
    num_bids = item.get("Number_of_Bids")
    location = item.get("Location")
    country = item.get("Country")
    started = item.get("Started")
    ends = item.get("Ends")
    description = item.get("Description")
    if description is None:
        description = "NULL"

    item_entry = (id + columnSeparator + name + columnSeparator + category + columnSeparator + transformDollar(currently)
                  + columnSeparator + transformDollar(buy) + columnSeparator + transformDollar(first) + columnSeparator + num_bids
                  + columnSeparator + seller_entry.get(
        "UserID") + columnSeparator + location + columnSeparator + country
                  + columnSeparator + transformDttm(started) + columnSeparator + transformDttm(ends) + columnSeparator + description)

    seller_entry = seller_entry.get("UserID") + columnSeparator + seller_entry.get("Rating")
    seller_set.add(seller_entry)
    bids = item.get("Bids", {})
    if bids is not None:
        for bid in bids:
            if bid is not None:

                for key, value in bid.items():
                    for key, value in bid.items():
                        bidder = value.get("Bidder").get("UserID")
                        time = value.get("Time")
                        amount = value.get("Amount")
                        entry = (bidder + columnSeparator + transformDttm(time) + columnSeparator
                                 + transformDollar(amount) + columnSeparator + id)
                        bid_set.add(entry)
                        bidder = value.get("Bidder")
                        rating = bidder.get("Rating")
                        location = bidder.get("Location")
                        if location is None:
                            location = "NULL"
                        bidder_id = bidder.get("UserID")

                        country = bidder.get("Country")
                        if country is None:
                            country = "NULL"
                        entry = location + columnSeparator + country + columnSeparator + bidder_id + columnSeparator + rating
                        bidder_set.add(entry)

    item_set.add(item_entry)


"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""


def parseJson(json_file, seller_set, bidder_set, bid_set, item_set):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items']  # creates a Python dictionary of Items for the supplied json file

        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            item_iterator(item, seller_set, bidder_set, bid_set, item_set)





"""
Loops through each json files provided on the command line and passes each file
to the parser
"""


def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    open('items.dat', 'w').close()
    open('sellers.dat', 'w').close()
    open('bidders.dat', 'w').close()
    open('bids.dat', 'w').close()
    items_file = open('items.dat', 'a')
    sellers_file = open('sellers.dat', 'a')
    bidders_file = open('bidders.dat', 'a')
    bids_file = open('bids.dat', 'a')
    bidder_set = set()
    seller_set = set()
    item_set = set()
    bid_set = set()
    for f in argv[1:]:
        if isJson(f):
            parseJson(f, seller_set, bidder_set, bid_set, item_set)
            print ("Success parsing " + f)
    for item1 in bidder_set:
        bidders_file.write(item1 + '\n')
        pass
    for item1 in seller_set:
        sellers_file.write(item1 + '\n')
        pass
    for item1 in bid_set:
        bids_file.write(item1 + '\n')
    for item1 in item_set:
        items_file.write(item1 + '\n')
        pass



if __name__ == '__main__':
    main(sys.argv)
