# -*- coding: utf-8 -*-

import pymongo
import click
from test import proxy_test, proxy_tests


class myDB(object):

    def __init__(self, dbname):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db_name = dbname

        client_list = self.client.list_database_names()
        print(client_list)
        self.db = self.client[dbname]
        collist = self.db.list_collection_names()
        print(collist)
        self.col = self.db["sites"]
#        self.col.insert_one(mydict)  

    def db_insert_targets(self, targets):
        #tars = proxy_tests(targets)
        for tar in targets:
            mydict = {'proxy': tar}
            self.col.insert_one(mydict)    

    def db_insert(self, target):
        click.echo(target)
        mydict = {'proxy':target}
        #mydict = self.col.find_one()
        #print(mydict)
        self.col.insert_one(mydict)

