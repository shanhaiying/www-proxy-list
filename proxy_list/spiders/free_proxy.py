# -*- coding: utf-8 -*-
import scrapy

from proxy_list.items import ProxyItem

class FreeProxySpider(scrapy.Spider):
    name = "free_proxy"
    allowed_domains = ["free-proxy-list.net"]
    start_urls = (
        'http://free-proxy-list.net',
    )

    def __init__(self, *pargs, **kwargs):
        #print(pargs)
        #print(kwargs)
        self.results = kwargs['res']
        scrapy.Spider.__init__(self, *pargs, **kwargs)

    def parse(self, response):
        table = response.xpath("//table/tbody")
        trs = table.xpath("tr")

        for tr in trs:
            cur_proxy = ProxyItem()

            cur_proxy['address'] = tr.xpath("td[1]/text()").extract()[0]
            cur_proxy['port'] = tr.xpath("td[2]/text()").extract()[0]
            cur_proxy['country'] = tr.xpath("td[4]/text()").extract()[0]

            # get protocol "http/https"
            protocol = tr.xpath("td[7]/text()").extract()[0]
            cur_proxy['protocol'] = "https" if protocol == "yes" else "http"
            
            self.results.append(cur_proxy)
            #yield cur_proxy

