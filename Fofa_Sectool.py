import base64
import os
import time
import requests
from lxml import etree
from datetime import datetime, timedelta
import sys

file_ip = 'ip'
folder_ip = './result/'
loop_max = 1000
headers={
    'cookie':'fofa_token=""'
}

# 统计目前提取的ip个数
def iter_count(file_name):
    from itertools import (takewhile, repeat)
    buffer = 1024 * 1024
    with open(file_name) as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer) for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)

# 去重和记算ip实际数量
def de_weight(file = folder_ip + file_ip):

    print('去重前ip数:' + str(iter_count(file)))
    with open(file, 'r') as f:
        lines = f.readlines()
    #将列表转化为集合去重
    unique_lines = set(lines)
    #去除空行
    try:
        unique_lines.remove("\n")
    except:
        print('没有空行!')
    # 设定去重后的文件名为原文件名加_new
    file_new = file + '_new'
    #去重后的ip写入新文件中
    with open(file_new, 'w') as f:
        for line in unique_lines:
            f.write(line)
    num_ip = len(unique_lines)
    print('去重后ip数:' + str(num_ip))
    print('去重完毕,已成功写入新文件:' + file_new)
    return num_ip

#确认路径存在性，若不存在则创建
def folder_exists():
    if not os.path.exists(folder_ip):
        os.makedirs(folder_ip)

#按页数爬取ip
def sec_ip(search_data,max_page):
    search_data_bs = base64.b64encode(search_data.encode("utf-8")).decode('ascii')
    for page in range(1,max_page+1):
        print('正在提取第' + str(page) + '页')
        url='https://fofa.info/result?page=' + str(page) + '&page_size=20' + '&qbase64='+search_data_bs
        print(url)
        try:
            result = requests.get(url,headers=headers,timeout=5).content
            html = etree.HTML(result)
            ip_data_x=html.xpath('//span[@class="hsxa-host"]/a[@target="_blank"]/@href')
            ip_data='\n'.join(ip_data_x)
            print(ip_data)
            with open(folder_ip + file_ip, 'a+') as f:
                f.write(ip_data + '\n')
            #冷却时间
            time.sleep(1)
        except:
            print('提取失败!')

def day_ip(search_data,all_page):
    folder_exists()
    all_num = all_page * 20
    max_page = 1
    #获取当前时间
    current_time = datetime.now()
    #间隔1天搜索
    one_day = timedelta(days=1)
    loop_time = 0
    while loop_time < loop_max:
        current_time = (current_time - one_day)
        current_time_new = current_time.strftime("%Y-%m-%d")
        print('正在提取' + current_time_new + '的内容')
        #构造按时间搜索语句
        search_data_time = search_data + '&&before=' + current_time_new
        sec_ip(search_data_time,max_page)
        loop_time += 1
        if loop_time >= int(all_page):
            de_weight_ips = de_weight()
            if de_weight_ips < all_num:
                print('还剩' + str(all_num - de_weight_ips) + '条没有提取！')
            break


if __name__ == '__main__':
    search_data = sys.argv[1]
    # max_page = int(sys.argv[2])
    all_page = sys.argv[2]
    # max_page = 3
    # all_page = 3
    # search_data = 'app=D_Link-DCS-4622'
    day_ip(search_data,all_page)
    # auto_ip(search_data,max_page)