# coding:utf-8

import requests
import urllib2
import re
import time


def UpFun(Article_Id):
    url = 'https://blog.csdn.net/qq_28817739/article/digg?ArticleId=%s' % str(Article_Id)
    ReferUrl = 'https://blog.csdn.net/qq_28817739/article/details/%s' % str(Article_Id)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': """bdshare_firstime=1432804476444; uuid_tt_dd=5874665987725545185_20150528; __gads=ID=6dbe976f1091e0da:T=1432804509:S=ALNI_Ma63fnYTAMrtpIQLGTDWFf-V6ZC3w; __qca=P0-1924203405-1432804512723; CloudGuest=AKLRitQ5PsB15aH5SW7bSBsYURfFqOgge6ORO2QV4EUqDw+gnKXXMYKF78PeMcFwrqF02vQYkMcNxxWDCt6PMn7itnc2JpOZ4vtQmrTAXkZVoZ6odI9hV3SKm26L7oF6ABT7F5Y8sFlqWHpV8Nwmc9Om52vSXdiRWMWM+SmSF7cM/3eqFJWcBzVSQBY4AsCH; UserName=u013018721; UserInfo=ILoGS%2FFKM8uT98%2F4tRSWZceYS3U6x7sg81CKDaKPgULoWdBwIN0RDSG7kKJ9%2BjvZo8PHr6Q6Vf%2BkmEcn9fk64XshqHUskkKdk%2BLIJ2wHGfF2mfOz%2FzhwkPxW3ny359eJg3MWVn4GGworZ8KOM7LAXw%3D%3D; UserNick=poetliu; AU=20B; UN=u013018721; UE="1507026255@qq.com"; access-token=c1575c35-1129-414d-a864-6899eb18b274; _JQCMT_ifcookie=1; _JQCMT_browser=20b1c0690840df900086ad8af0cec07b; __message_district_code=510000; lzstat_uv=37708960411757802909|2671462@3016791@2955225@3587820@854@3595736@2675686@2819552@2939462@2942182@3496353@3560230@3429585@3525517; FullCookie=1; uuid=9ac219b6-c952-4127-bab4-1472ceca5c52; route=; __utmt=1; avh=46652285%2c46610115%2c41985309; __utma=17226283.539248632.1435383498.1435481685.1435484556.12; __utmb=17226283.6.10.1435484556; __utmc=17226283; __utmz=17226283.1435481685.11.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dc_tos=nqnf3t; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; dc_session_id=1435484556110""",
        'Host': 'blog.csdn.net',
        'Referer': ReferUrl,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    r = requests.get(url=url, headers=headers)
    print "ID为:" + str(Article_Id) + "...已操作!\n"
    time.sleep(2)


def PagePuFun(BlogPageUrl):
    request = urllib2.Request(BlogPageUrl)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    fblog = opener.open(request)
    htm = fblog.read()
    Patt = r'<a href="https://blog.csdn.net/qq_28817739/article/details/(\d+)">'
    ArticleNums = re.findall(Patt, htm)
    for ArticleNum in ArticleNums:
        UpFun(ArticleNum)


if __name__ == "__main__":
    for i in range(0, 6):
        BlogPageUrl = "https://blog.csdn.net/qq_28817739/article/list/%s" % str(i + 1);
        print "开始第:" + str(i + 1) + "页\n"
        PagePuFun(BlogPageUrl)
        print "第:" + str(i + 1) + "页结束\n"
    print "完!!!\n"