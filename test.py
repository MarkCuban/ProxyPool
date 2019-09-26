# -*- coding: utf-8 -*-

import requests
import threading
import click
from pool import HEADER

MAX_THREADING_NUM = 8

TEST_URL = {
    'http': 'http://ping.chinaz.com/',
    'https':'https://ip.cn',
}

TEST_PROXY = {
    'http': '',
    'https': '',
}

TEST_TIMES = 3

def proxy_test(proxy):

    TEST_PROXY['http'] = proxy
    TEST_PROXY['https'] = proxy

    ret = False
    #print(TEST_URL, TEST_PROXY)
    try:
        
#        for i in range(0, TEST_TIMES):
            ret = False
            res = requests.get(TEST_URL['http'], headers=HEADER, proxies=TEST_PROXY, timeout=2)
            if res.status_code != 200:
                ret = False
#                break
            else:
                ret = True
            #res  = requests.get(TEST_URL['https'], headers=HEADER, proxies=TEST_PROXY, timeout=5)
            #if res.status_code != 200:
                #return False    
    except:
        ret = False

    return ret

def proxy_test_threading(proxy_slice):
    
    #print(proxy_slice)
#    if threading.current_thread().name == 'id7':
    #click.echo('parsing '+str(len(proxy_slice)))
    #click.echo(threading.current_thread().name + ' is running!')

    valid_proxy = []
    for proxy in proxy_slice:
        #click.echo('proxy '+proxy+' start to test...')
        res = proxy_test(proxy)
        if res == True:
            print('proxy '+proxy+' is tested!...successed!')
            valid_proxy.append(proxy)
        else:
            pass
            #print('proxy '+proxy+' is tested!...failed!')

    return valid_proxy

class testThread(threading.Thread):

    def __init__(self, target, args=(), name=None):
        super(testThread, self).__init__()
        self.target = target
        self.args = args

    def run(self):
        #print(self.args)
        self.result = self.target(*self.args)
        #print('result is ', self.result)

    def getResult(self):
        return self.result

def getResultFromThread(t_list):
    result = []

    for t in t_list:
        t.join()
        result += t.getResult()

    return result    

def proxy_tests(proxies):
    #print(len(proxies))
    click.echo(str(len(proxies))+' is going to tests')
    proxy_slice_num = len(proxies)//MAX_THREADING_NUM+1
    #click.echo('slice_num is '+str(proxy_slice_num))
    
    t_list = []
    
    for i in range(0, MAX_THREADING_NUM):
        proxy_slice = proxies[i*proxy_slice_num:(i+1)*proxy_slice_num]
        #click.echo(str(i*proxy_slice_num)+' '+str((i+1)*proxy_slice_num))
        #click.echo(proxy_slice)
        t = testThread(target=proxy_test_threading, args=(proxy_slice,), name='id:'+str(i))
        #click.echo('threading starts at...'+str(i))
        t.start()
        t_list.append(t)
        #t.join()

    result = getResultFromThread(t_list)
        
    return result



