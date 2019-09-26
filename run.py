# -*- coding: utf-8 -*-
from pool import ProxyGetter
from test import proxy_test, proxy_tests
from db import myDB
import click

def main():  
    proxgetter = ProxyGetter()
    db = myDB('crawlDB')
    
    result = []
    for fun in proxgetter.__CrawlFunc__:
        proxies = []
        tags = proxgetter.run_proxies(fun)
        if tags is not None:
            for tag in tags:
                proxies.append(tag)

            result += proxy_tests(proxies)
    
    db.db_insert_targets(result)
        

#            for tag in tags:
#                proxy_test(tag)
#                db.db_insert(tag)

    #while True:
#    one = db.col.count()
#    if one is not None:
#        print('one is ', one)

    

if __name__ == "__main__":
    main()