# -*- coding: utf-8 -*-

import json, collections, chardet
from functools import reduce
from pprint import pprint

### --- JSON --- ###

desc = []
with open('newsafr.json', 'rb') as jfile:
    jdata = jfile.read()
    enc = chardet.detect(jdata)
    data = jdata.decode(encoding=enc['encoding'])
    jdict = json.loads(data)
    for value in jdict.values():
        desc = value['channel']['items']
    res = []
    for dict in desc:
        res.append(dict['description'].split())
    res = reduce(lambda x, y: x + y, res)
    counter = collections.Counter()
    for word in res:
        if len(word) > 6:
            counter[word] += 1
    pprint(counter.most_common(10))

### --- XML --- ###

from bs4 import BeautifulSoup
xfile = open('newsafr.xml')
parser = BeautifulSoup(xfile, "lxml")
result = []
for item in parser.select("item description"):
    result.append(item.get_text().split())
result = reduce(lambda word1, word2: word1 + word2, result)
counterxml = collections.Counter()
for wordxml in result:
    if len(wordxml) > 6:
        counterxml[wordxml] += 1
pprint(counterxml.most_common(10))

