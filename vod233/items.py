#!/usr/bin/env Python
# coding=utf-8

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy


class Vod233Item(scrapy.Item):
    # define the fields for your item here like:
    #vod的标题
    vodTitle = scrapy.Field()
    #vod的gif图片
    vodGif = scrapy.Field()
    #vod的分类
    vodFolder = scrapy.Field()
    #vod的视频地址
    vodUrl = scrapy.Field()
    #vod的发布日期
    vodCreateDate = scrapy.Field()
    #vod的编号
    vodId = scrapy.Field()
    # vod的网页地址
    vodUrlAddress = scrapy.Field()



