import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
import random

# 读取数据
df = pd.read_excel('bus_stations_lines.xlsx')

# 提取线路名称
name = list(df['线路'])

# 提取纬度和经度
longitude = list(df['纬度'])
latitude = list(df['经度'])

# 数据结构
datas = []
line_colors = {}
a = []

# 初始化参数
A = 0
temp = "10"
start = []
stop = []

# 颜色生成器
def generate_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# 分离每个公交路线并生成颜色
for i, j, n in zip(longitude, latitude, name):
    if str(n) == temp:
        if A == 0:
            start = [i, j]
            A += 1
        elif A == 1:
            stop = [i, j]
            A += 1
        else:
            a = [start, stop]
            start = stop
            stop = [i, j]
            datas.append((temp, a))
            line_colors[temp] = generate_color()
    else:
        A = 0
        temp = str(n)
        

# 初始化Map3D
c = (
    Map3D(init_opts=opts.InitOpts(width="3200px", height="1800px"))
    .add_schema(
        maptype="西安",
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            is_main_shadow=False,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3,
        ),
        view_control_opts=opts.Map3DViewControlOpts(center=[-10, 0, 10], distance=50, alpha=90),
        post_effect_opts=opts.Map3DPostEffectOpts(is_enable=False),
    )
)

# print(datas)

# 添加线路
for line_name, line_data in datas:
    c.add(
        series_name=line_name,
        data_pair=[line_data],
        type_=ChartType.LINES3D,
        effect=opts.Lines3DEffectOpts(
            is_show=True,
            period=5, # 时间
            trail_width=3,
            trail_length=0.5,
            trail_color=line_colors[line_name],
            trail_opacity=1,
        ),
        linestyle_opts=opts.LineStyleOpts(
            is_show=True,
            color=line_colors[line_name],
            opacity=1,
        ),
    )

# 设置全局选项并渲染
c.set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Lines3D"))
c.render("3d多.html")
