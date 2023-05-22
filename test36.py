"""
地图可视化构建
"""
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts, ToolboxOpts, LabelOpts, MapItem

# 地图
map1 = Map()

# 添加数据
data = [
    ('广东省', 499),
    ('北京市', 399),
    ('上海市', 299),
    ('江西省', 199),
    ('湖南省', 99),
    ('浙江省', 89),
    ('江苏省', 49),
    ('福建省', 39),
    ('山东省', 1),
]
map1.add('热力图', data, maptype='china', label_opts=LabelOpts(is_show=False))

# 设置全局配置项
map1.set_global_opts(
    title_opts=TitleOpts(title='全国疫情热力图', pos_left='center', pos_bottom='bottom'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min': 0, 'max': 100, 'label': '0-100人', 'color': '#FFE4E1'},
            {'min': 100, 'max': 200, 'label': '100-200人', 'color': '#FFC0CB'},
            {'min': 200, 'max': 300, 'label': '200-300人', 'color': '#FFB6C1'},
            {'min': 300, 'max': 400, 'label': '300-400人', 'color': '#FF69B4'},
            {'min': 400, 'max': 500, 'label': '400-500人', 'color': '#FF1493'},
        ]
    )
)

# 渲染数据
map1.render('resource/html/疫情热力图.html')
