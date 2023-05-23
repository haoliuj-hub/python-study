"""
全国疫情案例
"""
import json

from pyecharts.charts import Map
from pyecharts.options import LabelOpts, TitleOpts, ToolboxOpts, VisualMapOpts

# 省份对应名称
PROVINCE_NAMES = {
    "广东省": "广东",
    "安徽省": "安徽",
    "福建省": "福建",
    "甘肃省": "甘肃",
    "广西壮族自治区": "广西",
    "贵州省": "贵州",
    "海南省": "海南",
    "河北省": "河北",
    "黑龙江省": "黑龙江",
    "河南省": "河南",
    "湖北省": "湖北",
    "湖南省": "湖南",
    "江苏省": "江苏",
    "江西省": "江西",
    "吉林省": "吉林",
    "辽宁省": "辽宁",
    "内蒙古自治区": "内蒙古",
    "宁夏回族自治区": "宁夏",
    "青海省": "青海",
    "山东省": "山东",
    "山西省": "山西",
    "陕西省": "陕西",
    "四川省": "四川",
    "台湾省": "台湾",
    "新疆维吾尔自治区": "新疆",
    "西藏自治区": "西藏",
    "云南省": "云南",
    "浙江省": "浙江",
    "重庆市": "重庆",
    "香港特别行政区": "香港",
    "澳门特别行政区": "澳门",
    "南海诸岛": "南海诸岛",
    "北京市": "北京",
    "天津市": "天津",
    "上海市": "上海"
}

f = open('../../resource/可视化案例数据/地图数据/疫情.txt', 'r', encoding='utf-8')
data = f.read()
f.close()

data_json = json.loads(data)

data_list = data_json['areaTree'][0]['children']

map_list = list()
for child_data in data_list:
    province_name = child_data['name']
    province_total = child_data['total']['confirm']
    map_list.append((province_name, province_total))

map1 = Map()

map1.add('各省份确诊人数', map_list, maptype='china', label_opts=LabelOpts(is_show=False), name_map=PROVINCE_NAMES)

# 设置全局配置项
map1.set_global_opts(
    title_opts=TitleOpts(title='全国疫情地图', pos_left='center', pos_bottom='bottom'),
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
map1.render('../../resource/html/全国疫情地图.html')
