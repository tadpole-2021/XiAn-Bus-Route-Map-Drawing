## index.html【最终的效果展示】

![效果图](.\效果图.png)

### 3dmap.html / 第1块结果
	
 1.需要使用Driver进行数据爬取【chromedriver.exe】
下载与自己电脑版本匹配的ChromeDrive：https://googlechromelabs.github.io/chrome-for-testing/
	
2.使用【code.py】爬取（https://xian.8684.cn/）西安的公交站信息保存到文件【xian_bus_info.csv】
	
3.使用【bus_data.py】对【index.html】进行爬取公交站点的经纬度保存到文件【bus_stations_lines.xlsx】
	
4.使用【3D.py】进行公交线路的绘制，保存结果到【3dmap.html】

### 经纬度散点图.png / 第3块结果

将第一块中所获取的公交数据进行经纬度的散点图的绘制【经纬度image.py】，查看公交站点的分布情况，生成图像为【经纬度散点图.png】

### 公交网络地图.html / 第4块结果

利用百度的AK进行动态的图像绘制公交线路图【公交网络地图.html】

### 优化

通过网上的学习实现了分离公交后的单色的3D地图。
再接着实现出了各公交线路颜色的区别的多色的3D地图。
根据这个设计思路修改第4块的代码，实现了公交线路分离【公交网络地图公交线路分离.html】（并没有放在效果页去展示，加载页面数据比较慢）

在最终的index.html显示时我在3dmap.html中手动加了一段js让显示更清晰直观

```
<script>
	// 为了在放入四分之一的窗口时，公交线路完全显示在窗口的正中央
	// 当文档加载完毕时执行滚动
	document.addEventListener('DOMContentLoaded', function() {
		// 获取文档的宽度和高度
		var docWidth = document.documentElement.scrollWidth;
		var docHeight = document.documentElement.scrollHeight;
		
		// 滚动到的水平位置（60%）
		var scrollXPosition = docWidth * 0.6;
		// 滚动到的垂直位置（10%）
		var scrollYPosition = docHeight * 0.1;
		
		// 执行滚动
		window.scrollTo(scrollXPosition, scrollYPosition);
	});
</script>
```



参考的博客文章网站：

[百度地图--api--获取经纬度 - 简书 (jianshu.com)](https://www.jianshu.com/p/bbc21257079a)

[百度地图 (baidu.com)](https://map.baidu.com)

[jspopularGL | 百度地图API SDK (baidu.com)](https://lbs.baidu.com/index.php?title=jspopularGL/guide/getkey)

[通过百度API获取城市公交线路坐标点及站点信息 - 热心市民陈同学 - 博客园 (cnblogs.com)](https://www.cnblogs.com/console-chan/p/12399020.html)

[Bmap - Hiking_trail_in_hangzhou - Document (pyecharts.org)](https://gallery.pyecharts.org/#/BMap/hiking_trail_in_hangzhou)

[jspopularGL | 百度地图API SDK (baidu.com)](https://lbs.baidu.com/index.php?title=jspopularGL/guide/getkey)

[分类路径-线 LineLayer-示例中心-Loca API 示例 | 高德地图API (amap.com)](https://lbs.amap.com/demo/loca-api/demos/line/bj_busline_colors)

[北京公交线路-线图层-示例详情-Loca API 2.0 | 高德地图API (amap.com)](https://lbs.amap.com/demo/loca-v2/demos/cat-line/bj-bus)
