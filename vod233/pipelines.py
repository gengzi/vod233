#!/usr/bin/env Python
# coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from MysqlHelper import MysqlHelper
from vod233.items import Vod233Item
import time

# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="1024",port=3306)

class Vod233Pipeline(object):


    def selectNum(self,item):
        selectsql = "select id from vod233 where vodid = %s"
        selectparam = [str(item['vodId'])]
        list = mysql.get_all(sql=selectsql, params=selectparam)
        if len(list) > 0:
            return True
        return False


    def process_item(self, item, spider):
        #写入数据库
        if isinstance(item,Vod233Item):
            #[1]先查询id是否存在
            if self.selectNum(item):
                pass
            else :
                sql = 'insert into vod233(vodtitle,vodgifurl,vodfolder,vodurl,vodcreatedate,vodid,vodurladdress) values(%s,%s,%s,%s,%s,%s,%s)'
                params = [str(item['vodTitle'][0]),str(item['vodGif'][0]),str(item['vodFolder'][0]),str(item['vodUrl']),str(item['vodCreateDate']),
                          str(item['vodId']),str(item['vodUrlAddress'])]
                num = mysql.insert(sql=sql,params=params)
                if num > 0:
                    print "success"
        else:
            print "error"
        #print str(item['vodTitle'].encode('utf-8'))
        #return item





