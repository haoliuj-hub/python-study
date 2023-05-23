"""
河南省疫情地图
"""
import json

from pyecharts.charts import Map
from pyecharts.options import LabelOpts, TitleOpts, ToolboxOpts, VisualMapOpts

# 河南省地市映射关系
city_map = {
    "郑州市": "郑州",
    "开封市": "开封",
    "洛阳市": "洛阳",
    "平顶山市": "平顶山",
    "安阳市": "安阳",
    "鹤壁市": "鹤壁",
    "新乡市": "新乡",
    "焦作市": "焦作",
    "濮阳市": "濮阳",
    "许昌市": "许昌",
    "漯河市": "漯河",
    "三门峡市": "三门峡",
    "南阳市": "南阳",
    "商丘市": "商丘",
    "信阳市": "信阳",
    "周口市": "周口",
    "驻马店市": "驻马店",
    "济源市": "济源示范区"
}

f = open('../../resource/可视化案例数据/地图数据/疫情.txt', 'r', encoding='utf-8')
data = f.read()
f.close()

data_json = json.loads(data)

data_list = data_json['areaTree'][0]['children'][3]['children']

map_list = list()
for child_data in data_list:
    city_name = child_data['name']
    city_total = child_data['total']['confirm']
    map_list.append((city_name, city_total))

map1 = Map()

map1.add('河南各地市确诊人数', map_list, maptype='河南', label_opts=LabelOpts(is_show=False), name_map=city_map)

# 设置全局配置项
map1.set_global_opts(
    title_opts=TitleOpts(title='河南疫情地图', pos_left='center', pos_bottom='bottom'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 0, 'max': 99, 'label': '0-99人', 'color': '#CCFFFF'},
            {'min': 100, 'max': 999, 'label': '100-999人', 'color': '#FFFF99'},
            {'min': 1000, 'max': 4999, 'label': '1000-4999人', 'color': '#FF9966'},
            {'min': 5000, 'max': 9999, 'label': '5000-9999人', 'color': '#FF6666'},
            {'min': 10000, 'max': 99999, 'label': '10000-99999人', 'color': '#CC3333'},
            {'min': 100000, 'label': '100000+人', 'color': '#990033'},
        ]
    )
)

# 渲染数据
map1.render('../../resource/html/河南疫情地图.html')

