#!/usr/bin/python

import json
import re
import time
import urllib

from xml.dom.minidom import parse, parseString

# data structure

stops = dict()
muni = "http://webservices.nextbus.com/service/publicXMLFeed"

# get list of routes and examine non-tram lines

print "Getting stops"
            
url = muni + "?command=routeList&a=sf-muni"

d1 = parse(urllib.urlopen(url))

for node in d1.getElementsByTagName('route'):
    r = node.getAttribute('tag')

    title = node.getAttribute('title')

    # get all stops for route
    print "Examining route %s" % r

    url = muni+"?command=routeConfig&a=sf-muni&r=%s" % r

    d2 = parse(urllib.urlopen(url))

    for s in d2.getElementsByTagName('stop'):
        stop_info = dict()
        for field in ('tag', 'title', 'lat', 'lon', 'stopId'):
            if s.getAttribute(field):
                stop_info[field] = s.getAttribute(field)
            else:
                print "Missing attribute: skipping"
                break
            print field, s.getAttribute(field), stop_info[field]

        if not ('title' in stop_info and 'lat' in stop_info and 'lon' in stop_info):
            continue

        # normalise to _ not camelcase
        stop_info['stop_id'] = stop_info['stopId']
        del stop_info['stopId']

        stop_info['route'] = r
        stop_info['route_name'] = title

        stops[stop_info['tag']] = stop_info

print json.dumps(stops)

f = open('muni-stops.json', 'w')
json.dump(stops, f)
f.close()

print "Wrote muni-stops.json"

# for route in sorted(ids.keys()):
#     print "%s: route %s at speed %02.f" % (route, ids[route]['routeTag'], float(ids[route]['speedKmHr']))