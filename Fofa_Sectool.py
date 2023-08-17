import base64
import time
import requests
from lxml import etree
import datetime
import sys

headers={
    'cookie':'fofa_token=""'
}
now_time=datetime.datetime.now()
def auto_ip(search_data,max_page):
    # search_data_bs = str(base64.b64encode(search_data.encode("utf-8")), "utf-8")
    search_data_bs = base64.b64encode(search_data.encode("utf-8")).decode('ascii')
    for page in range(1,max_page+1):
        print('正在提取第' + str(page) + '页')
        url='https://fofa.info/result?page='+str(page)+'&qbase64='+search_data_bs
        try:
            result = requests.get(url,headers=headers,timeout=3).content
            html = etree.HTML(result)
            ip_data=html.xpath('//span[@class="hsxa-host"]/a[@target="_blank"]/@href')
            ipdata='\n'.join(ip_data)
            with open(r'../ip.txt', 'a+') as f:
                f.write(ipdata+'\n')
            time.sleep(1)
        except:
            print("error")

def day_ip(search_data,max_page,early_day):
    for d in range(0,early_day+1):
        day = (now_time - datetime.timedelta(days=d)).strftime('%Y-%m-%d')
        print('正在提取' + day + '的内容')
        search_data = search_data + '&after=' + day + '&&before=' + day
        auto_ip(search_data,max_page)

if __name__ == '__main__':
    search_data=sys.argv[1]
    max_page=int(sys.argv[2])
    max_page=3
    search_data = 'app=D_Link-DCS-4622'
    # day_ip(search_data,6,10)
    auto_ip(search_data,max_page)