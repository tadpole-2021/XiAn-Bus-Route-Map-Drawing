#爬取网站  m.8684.cn/bus_switch 公交线路  郑州
import requests
import time
from lxml import etree

#列表保存所有线路信息
items = []

#添加头部  作为全局
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


#爬取第一页所有导航的链接
def parse_navigation():
    #在这里可以换你想要的爬的城市网址
    url = "https://xian.8684.cn/"
    r = requests.get(url=url,headers=headers)
    # print(r.text)
    # exit()
    #解析内容，获取所有导航链接
    tree = etree.HTML(r.text)
    #过滤  获取链接
    #查找以数字、字母开头的所有链接返回   使用过滤标签值的方法寻找
    number_href_list = tree.xpath('//a[starts-with(@href,"/list")]/@href')
    # print(number_href_list)
    # exit()
    return number_href_list


#三级route回传数据解析  获取每一路公交的详细信息  最后一级
def parse_sanji_route(content):
    tree = etree.HTML(content)
    #依次过滤获取各个内容
    #线路名称
    bus_number = tree.xpath('//div[@class ="info"]/h1[@class ="title"]/span/text()')
    # print(bus_number)
    # exit()
    #获取运行时间
    run_time = tree.xpath('//ul[@class="bus-desc"]/li[1]/text()')
    # print(run_time)
    # exit()
    #获取票价信息
    ticket_info = tree.xpath('//ul[@class="bus-desc"]/li[2]/text()')
    # print(ticket_info)
    # exit()
    #获取更新时间
    gxsj = tree.xpath('//ul[@class="bus-desc"]/li[4]/span/text()')
    # print(gxsj)
    # exit()
    #获取上行总站数
    up_total = tree.xpath('//div[@class="total"]/text()')[0]
    #print(up_total)
    # exit()
    #获取上行所有站名
    up_name_list = tree.xpath('//div[@class="bus-lzlist mb15"][1]/ol/li/a/text()')
    print(up_name_list)
    # exit()


    try:
        #获取下行总站数
        down_total = tree.xpath('//div[@class="total"]/text()')[1]
        #print(down_total)
        # exit()
        #获取下行所有站名
        down_name_list = tree.xpath('//div[@class="bus-lzlist mb15"][2]/ol/li/a/text()')
        # print(down_name_list)
        # exit()
    except Exception as e:
        down_total = []
        down_name_list="环形公交，与上行一致"
    #将每一条线路信息写入字典
    item = {
        '线路名称':bus_number,
        '运行时间':run_time,
        '票价信息':ticket_info,
        '更新时间':gxsj,
        '上行总站数':up_total,
        '上行所有站名':up_name_list,
        '下行总站数':down_total,
        '下行所有站名':down_name_list
    }
    items.append(item)

#解析二级爬取url的内容  获取每一路公交的详细url
def parse_erji_route(content):
    tree = etree.HTML(content)
    #写xpath获取每一个线路
    route_list = tree.xpath('//div[@class ="list clearfix"]//a/@href')
    route_name = tree.xpath('//div[@class ="list clearfix"]//a/text()')
    i=0
    # print(route_list)
    # exit()
    #遍历 发送请求
    for route in route_list:
        print("开始爬取%s线路" %route_name[i])
        route = "https://xian.8684.cn" + route
        r = requests.get(url=route,headers=headers)
        # time.sleep(1)
        # print(r.text)
        # exit()
        #解析内容 获取每一路公交的详细信息
        parse_sanji_route(r.text)
        print("结束爬取%s线路" %route_name[i])
        i+=1

#二级url爬取
def parse_erji(navi_list):
    #便利上面的列表，依次发送请求，解析内容  获取每一个页面所有的公交路线
    for end_url in navi_list:
        end_url = "https://xian.8684.cn" + end_url
        print("开始爬取 %s 所有的公交信息" %end_url)
        #print(end_url)
        #exit()
        r = requests.get(url=end_url,headers=headers)
        #解析内容，获取每一路公交的详细url
        parse_erji_route(r.text)
        print("结束爬取 %s 所有的公交信息" %end_url)

#定义主函数
def main():
    #爬取第一页所有导航链接
    navi_list = parse_navigation()
    #爬取二级页面，找到所有公交线路的url
    parse_erji(navi_list)
    #爬取完毕 写入
    fp = open('xian00.txt', 'w', encoding="utf8")
    for item in items:
        fp.write(str(item)+'\n')
    fp.close()

if __name__ == '__main__':
    main()