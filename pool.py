# -*- coding: utf-8 -*-

import requests
from lxml import etree
import click
import re

HEADER = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

URLS = {
    'xila':'http://www.xiladaili.com', 
    'xici':'https://www.xicidaili.com',
    'kuai':'https://www.kuaidaili.com/ops/',
} 


class ProxyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k in attrs.keys():
            if k.startswith('proxy'):
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount'] = count
        #click.echo('proxmete class is called')
        #click.echo(attrs)
        return type.__new__(cls, name, bases, attrs)

    def other(self):
        pass

def isIPPORT(string):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)\:')
    if p.match(string):
        return True
    else:
        return False

def isIP(string):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)')
    if p.match(string):
        return True
    else:
        return False

def isIPType(string):
    string_c = 'abc'
    string_c.startswith
    if string.startswith('http') or string.startswith('https'):
        pass

class ProxyGetter(object, metaclass=ProxyMetaClass):

    def __init__(self):
        #click.echo('new proxy getter')
        proxies = []
        pass

    def parse_url(self, url):
        try:
            res = requests.get(url, headers=HEADER)
            if res.status_code == 200:
                return res.content.decode()
        except Exception as e:
            raise e

    def proxy_ip66(self):
        #click.echo('ip66')
        return None

    def proxy_xici(self):
        return None
        content = self.parse_url('http://www.xicidaili.com')
        html = etree.HTML(content)
        all_tags = html.xpath('//table/tbody/tr/td/text()')
        all_tags += html.xpath('//table/tr/td/text()')
        all_tags = self.parse_tags_IP_Port(all_tags)
        return all_tags

    def parse_ip(self, tags):
        ip = ''
        port = ''
        ret = []
        for tag in tags:
            if isIP(tag) is True:
                ip = tag
            if ip != '' and tag.isdigit():
                port = tag
                ret.append(ip+':'+port)
                ip = ''

        return ret

    def parse_xila_tags(self, tags):
        res = []
        port_dict = {'ip':'',
                     'type':'',
                     'position':'',
        }
        for tag in tags:
#            click.echo(tag)
            if isIPPORT(tag) is True:
                port_dict['ip'] = tag
                res.append(tag)
            if isIPType(tag) is True:


        return res

    def proxy_xila(self):
        content = self.parse_url('http://www.xiladaili.com')
        html = etree.HTML(content)
        all_tags = html.xpath('//table/tbody/tr/td/text()')
        all_tags += html.xpath('//table/tr/td/text()')
        all_tags = self.parse_xila_tags(all_tags)
        return all_tags

    def proxy_kuai(self):
        return None
        content = self.parse_url('https://www.kuaidaili.com/free/inha/')
        html = etree.HTML(content)
        all_tags = html.xpath('//tbody/tr/td/text()')
#        all_tags += html.xpath('//table/tr/td/text()')
#        print('kuai all tags is', all_tags)
        all_tags = self.parse_ip(all_tags)
#        for tag in all_tags:
#            click.echo(tag)
        return all_tags

    def proxy_ihuan(self):
        #click.echo('ihuan')
        return None

    def run_proxies(self, callback):
        x = "self.{}()".format(callback)
        click.echo(x)
        tags = eval(x)
        return tags

