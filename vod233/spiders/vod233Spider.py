#!/usr/bin/env Python
# coding=utf-8
import scrapy
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from vod233.items import Vod233Item


class Vod233spiderSpider(CrawlSpider):
    name = 'vod233Spider'
    allowed_domains = ['223vod.com','224vod.com']


    start_urls = ['https://www.224vod.com/Html/60/',
                  'https://www.224vod.com/Html/61/',
                  'https://www.224vod.com/Html/101/',
                  'https://www.224vod.com/Html/100/',
                  'https://www.224vod.com/Html/62/',
                  'https://www.224vod.com/Html/93/',
                  'https://www.224vod.com/Html/90/',
                  'https://www.224vod.com/Html/91/',
                  'https://www.224vod.com/Html/88/',
                  'https://www.224vod.com/Html/92/',
                  'https://www.224vod.com/Html/109/',
                  'https://www.224vod.com/Html/110/',
                  'https://www.224vod.com/Html/111/',
                  'https://www.224vod.com/Html/112/',
                  'https://www.224vod.com/Html/113/',
                  'https://www.224vod.com/Html/114/',
                  ]

    #[1] 所有的栏目
    #folder_le = LinkExtractor(allow=('/Html/\d+'))
    #[2]进入一个栏目
    vod_page_le = LinkExtractor(allow=('/Html/\d+/index-\d+'))
    #[3]视频链接
    vod_le = LinkExtractor(allow=('/Html/\d+/\d+'))

    rules = (
        #Rule(folder_le, process_links='folder_deal_links',follow=True),
        Rule(vod_page_le,follow=True),
        Rule(vod_le,callback='parse_item', follow=True),
    )

    def folder_deal_links(self,links):
        print "1111"
        """
        处理folder的链接信息
        :return:
        """
        for link in links:
            new_link = link.url.split("\\\\")
            link.url = 'https://www.224vod.com'+new_link[1]
            print link.url
        return links
            #https://www.223vod.com/Html/60/
            #'https://www.223vod.com/js/\\"/Html/60/\\"'

    def parse_item(self, response):
        """
        解析
        :param response:
        :return:
        """
        item = Vod233Item()
        #vod的标题
        item['vodTitle'] = response.xpath('//div[@class="box"]//dd[@class="film_title"]/h1/text()').extract()
        item['vodGif'] = response.xpath('//div[@class="box"]//dd/span/a/@href').extract()
        item['vodFolder'] = response.xpath('//div[@class="box"]//dd/span/text()').extract()
        #正则匹配
        try:
            vodaddressurl= re.search(r"var down_url = '(.*)';",response.body).group(1)
            item['vodUrl'] = str(vodaddressurl)
        except Exception,e:
            item['vodUrl'] ="-"
            print "正则匹配失败"

        #print vodaddressurl
        item['vodCreateDate'] = response.xpath('//div[@class="box"]//dd/span/a/@href').extract()[0].split("/")[5]
        item['vodId'] = response.url.split("/")[4]+"-"+response.url.split("/")[5].split(".")[0]
        item['vodUrlAddress'] = response.url
        yield item


        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
