import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

df = pd.read_excel('bus_stations_lines.xlsx')

name = list(df['线路'])

longitude = list(df['纬度'])
latitude = list(df['经度'])
datas = []
a = []

A = 0
temp = "10"
start = []
stop = []
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

            datas.append(a)
            
    else:
        A = 0
        temp = str(n)
        # 分离每个公交路线
        
# print(datas)

c = (
    Map3D(init_opts=opts.InitOpts(width="2400px", height="1600px"))
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
        view_control_opts=opts.Map3DViewControlOpts(center=[-10, 0, 10], alpha=90),
        post_effect_opts=opts.Map3DPostEffectOpts(is_enable=False),
    )
    .add(
        series_name="",
        data_pair=datas,
        type_=ChartType.LINES3D,
        effect=opts.Lines3DEffectOpts(
            is_show=True,
            period=0.5,
            trail_width=3,
            trail_length=0.5,
            trail_color="#f00",
            trail_opacity=1,
        ),
        linestyle_opts=opts.LineStyleOpts(is_show=False, color="#fff", opacity=0),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Lines3D"))
        .render("3d单.html")
)