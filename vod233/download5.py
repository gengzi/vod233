#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言
import re
import random
import requests
import uuid
import json
from Queue import Queue
import threading
import time
# 使用 lxml 的 etree 库
from lxml import etree
import os
from MysqlHelper import MysqlHelper
from DateUtils import getNewFormatTime

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

filepath = "J:\\ziyuan\\vod233\\"

# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="1024",port=3306)

def selectNoDownloadVod():
    """
    查询没有下载的视频
    :return:
    """
    sql = "select vodtitle,vodgifurl,vodfolder,vodurl,id from vod233 where isdownload is null and vodurl != '-' limit 2999,88"
    params = []
    list = mysql.get_all(sql=sql,params=params)
    if len(list) >0 :
        for item in list:
            loadPage(item)

def updateDownInfo(name,vodid):
    """
    更新下载信息
    :param name:
    :return:
    """
    sql = "update vod233 set isdownload = %s,downloadaddress=%s,downdate=%s where id =%s"
    params = [str('yes'),str(name),str(getNewFormatTime('%Y-%m-%d %H:%M:%S')),str(vodid)]
    num = mysql.update(sql=sql,params=params)
    if num > 0:
        print "插入成功"





def loadPage(item):
    vodtitle = item[0]
    vodgifurl = item[1]
    vodfolder = item[2]
    vodurl = item[3]
    #更新链接
    vodurl = str(vodurl).replace("https://d.9xxav.com","https://d.33wp.me")
    print vodurl

    vodid = item[4]
    try:
        start_time = time.time()
        req = requests.get(vodurl,headers=headers,timeout=10)
        spcontent = req.content
        vodfolder =unicode(str(vodfolder).encode('utf-8'), "utf-8")
        vodtitle = unicode(str(vodtitle).encode('utf-8'), "utf-8")
        dirname = filepath+vodfolder+"\\"
        name = filepath+vodfolder+"\\"+vodtitle+'.mp4'
        isExists = os.path.exists(dirname)
        if not isExists:
            os.makedirs(dirname)
            print dirname + ' 创建成功'
        with open(name, "wb") as code:
            code.write(spcontent)
        end_time = time.time() - start_time
        print("耗时："+str(end_time))

        # 将下载信息写入数据库
        updateDownInfo(name,vodid)

    except Exception, e:
        print(e)
    print("end")


if __name__ == "__main__":
    for i in range(0,10):
        selectNoDownloadVod()