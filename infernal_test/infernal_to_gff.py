#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: <26.10.20>
#@author: <Danil Zilov/Alexey Komissarov>
#@contact: <zilov@scamt-itmo.ru/akomissarov@scamt-itmo.ru>

import sys
import argparse
import os
import pymongo

headers = ["_id", "seqid", "source", "e_value", "score", "start", "stop", "strand", "description"]

def main():
    ''' Function description.
    '''
    is_inside = False
    for line in sys.stdin:
        line = line.strip()
        
        if line.startswith("Hit alignments"):
            break
        if line.startswith("Query"):
            query = line.split(":")[1].strip()
        if line.startswith("Accession"):
            accession = line.split(":")[1].strip()
        if line.startswith("Hit scores"):
            is_inside = True
        if is_inside and line.startswith("("):
            d = line.split()
#             print(line)
            values = [
                "%s:%s:%s:%s" % (d[5], d[6], d[7], query + " " + accession), 
                d[5], 
                query + ":" + accession, 
                float(d[2]), 
                float(d[3]), 
                int(d[6]), 
                int(d[7]), 
                d[8], 
                " ".join(d[12:]),
              ]
            mydict = dict(zip(headers, values))
            x = mycol.insert_one(mydict)
#             print(mydict)

            assert mycol.find({"_id": mydict["_id"]})

if __name__ == '__main__':

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ribozymes_db"]
    mycol = mydb["bacteria"]    

    main()