import csv
import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


def get_page_url(url):
    try:
        global url1
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
        html = requests.get(url,headers=headers).text
        print(html)
        # bs4解析
        soup = bs(html, 'lxml')
        lu = soup.find('div',class_='list clearfix')
        hrefs = lu.find_all('a')
        # 获取二级页面的详情页url
        url_list = []
        for k in hrefs[:6]:
            urls = url1 + k['href']
            url_list.append(urls)
        return url_list
    except:
        print("请求异常！")


# 请求分析页面
def get_page_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    html = requests.get(url, headers=headers).text
    soup = bs(html,'lxml')
    h1 = soup.find_all('h1',class_="title")
    # 公家路线
    bus_name = h1[0].span.string
    # 线路性质
    bus_type = h1[0].a.string
    # 运行时间
    h2 = soup.find_all('ul',class_="bus-desc")
    bus_time = h2[0].li.string
    # 参考票价
    ticket = h2[0].li.next_sibling.string
    print(ticket)
    # 公司信息
    gongsi = h2[0].find_all('a')[0].string
    print(gongsi)
    # 最后更新
    h3 = h2[0].li.next_sibling.next_sibling.next_sibling
    gengxin = h3.find('span',tabindex="0").string
    print(gengxin)
    try:
        wang_info = soup.find_all('div',class_="trip")[0].string
        print(wang_info)
    except:
        wang_info = None
    try:
        fan_info = soup.find_all('div',class_="trip")[1].string
        print(fan_info)
    except:
        fan_info = None
    try:
        wang_list_tag = soup.find_all('div',class_="bus-lzlist mb15")[0].find_all('a')
    except:
        wang_list_tag = None
    try:
        fan_list_tag = soup.find_all('div',class_="bus-lzlist mb15")[1].find_all('a')
    except:
        fan_list_tag = None
    wang_buff = ""
    fan_buff = ""
    for wang in wang_list_tag:
        wang_buff += wang.string+','
    print(wang_buff)
    if fan_list_tag:
        for fan in fan_list_tag:
            fan_buff += fan.string+','
    print(fan_buff)
    result_list = [bus_name,bus_type,bus_time,gongsi,gengxin,wang_info,wang_buff,fan_info,fan_buff]
    dic = {'bus_name':None,'bus_type':None,'bus_time':None,'gongsi':None,'gengxin':None,'wang_info':None,'wang_buff':None,'fan_info':None,'fan_buff':None}
    count = 0
    for k in dic.keys():
        dic[k] = result_list[count]
        count += 1
    print(dic)
    lst = []
    lst.append(dic)
    with open('xian_bus_info.csv','a+',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=header)
        writer.writerows(lst)


if __name__ == '__main__':
    header = ['bus_name','bus_type','bus_time','gongsi','gengxin','wang_info','wang_buff','fan_info','fan_buff']
    # 遍历得出每个一级页面的url
    url1 = "https://xian.8684.cn/"
    url_list = url1 + "/list{}"
    for i in range(1,10):
        url = url_list.format(i)
        print(url)
        a = get_page_url(url)
        for i in a:
            get_page_info(i)