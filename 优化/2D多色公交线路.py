import pandas as pd
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
import random

# 读取数据
df = pd.read_excel('bus_stations_lines.xlsx')

# 提取线路名称
name = list(df['线路'])

# 提取纬度和经度
longitude = list(df['纬度'])
latitude = list(df['经度'])

# 数据结构
datas = {}
line_colors = {}
a = []

# 颜色生成器
def generate_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# 分离每个公交路线并生成颜色
for i, j, n in zip(longitude, latitude, name):
    if n not in datas:
        datas[n] = []
        line_colors[n] = generate_color()
    datas[n].append([i, j])

# 引用本地js资源渲染
CurrentConfig.ONLINE_HOST = '../第4块/pyecharts-assets-master/assets/'

BAIDU_MAP_AK = "OVTMqUZGD4nHRIf8UVxr2aHdXqWs7rj7"

c = (
  BMap(init_opts=opts.InitOpts(width="1600px", height="900px"))
  .add_schema(
      baidu_ak=BAIDU_MAP_AK,     # 申请的BAIDU_MAP_AK
      center=[108.998814, 34.213642],    # 西安市经纬度中心
      zoom=12,
      is_roam=True,
  )
)

# 添加每条线路
for line_name, line_data in datas.items():
    c.add(
#         "",
        series_name=line_name,
        type_="lines",
        is_polyline=True,
        data_pair=[line_data],
        linestyle_opts=opts.LineStyleOpts(opacity=0.8, width=2, color=line_colors[line_name]),
        progressive=200,
        progressive_threshold=500,
    )

# 渲染地图
c.render('公交网络地图公交线路分离.html')
