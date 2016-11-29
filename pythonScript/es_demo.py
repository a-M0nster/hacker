#!/usr/bin/env python
# coding:utf-8

import json
import urllib2
from elasticsearch import Elasticsearch, helpers

url = "xxxx"
es = Elasticsearch(['xxx:9200'])

try:
    data = urllib2.urlopen(url).read()
except Exception, e:
    print e

values = json.loads(data)

ind = 0
doces = []
for mid, tag in values['result'].items():
    ind += 1
    doc = {
        "_op_type": "index",
        "_index": "xxx",
        "_type": "xxx1",
        "_source": {
            "mid": xxx,
            "tag": xxx
        }
    }
    doces.append(doc)
    if ind % 1000 == 0:
        helpers.bulk(es, doces)
        doces = []


helpers.bulk(es, doces)
doces = []
# es.index(index="mid-tag", doc_type="201611", body=body)

# res = es.search(index="mid-tag", doc_type="201611",
#                body = {"query": {"match_all": {}}})
# print res
