import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

df = pd.read_excel("bus_stations_lines.xlsx")
x_data = df['经度']
y_data = df['纬度']
colors = ['#FF0000', '#0000CD', '#00BFFF', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970', '#9932CC']
colors = [random.choice(colors) for i in range(len(x_data))]
mpl.rcParams['font.family'] = 'SimHei'
plt.style.use('ggplot')
# 设置大小
plt.figure(figsize=(12, 6), dpi=200)
# 绘制散点图  经度  纬度  传进去   设置 颜色  点的大小
plt.scatter(x_data, y_data, marker="o", s=9., c=colors)

# 添加描述信息 x轴 y轴 标题
plt.xlabel("经度")
plt.ylabel("纬度")
plt.title("西安市公交站点分布情况")
plt.savefig('经纬度散点图.png')
plt.show()
