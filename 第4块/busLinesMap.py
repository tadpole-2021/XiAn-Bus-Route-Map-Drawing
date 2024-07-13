import pandas as pd
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig

df = pd.read_excel('bus_stations_lines.xlsx')
df.drop_duplicates(subset='站点', inplace=True)
longitude = list(df['纬度'])
latitude = list(df['经度'])
# print(longitude)
# print(latitude)

# 将经纬度组合
datas = []
a = []
for i, j in zip(longitude, latitude):
    a.append([i, j])
datas.append(a)
# print(datas)

# 引用本地js资源渲染
CurrentConfig.ONLINE_HOST = './pyecharts-assets-master/assets/'

BAIDU_MAP_AK = "OVTMqUZGD4nHRUVxr2aHdX" # 填你申请的百度地图的AK

c = (
  BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
  .add_schema(
      baidu_ak=BAIDU_MAP_AK,     # 申请的BAIDU_MAP_AK
      center=[108.998814, 34.213642],    # 西安市经纬度中心
      zoom=12,
      is_roam=True,
  )
  .add(
      "",
      type_="lines",
      is_polyline=True,
      data_pair=datas,
      linestyle_opts=opts.LineStyleOpts(opacity=0.2, width=0.5, color='red'),
      progressive=200,
      progressive_threshold=500,
  )
)

# c.render_notebook()
c.render('公交网络地图.html')