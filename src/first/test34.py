"""
pyecharts
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 折线图
line = Line()

# 添加x轴数据
line.add_xaxis(['中国', '美国', '日本', '韩国', '俄罗斯'])

# 添加y轴数据
line.add_yaxis('GDP', [14.2, 20.5, 4.5, 5.5, 3.2])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title='世界各国GDP', subtitle='单位：亿美元', pos_left='center'),
    legend_opts=LegendOpts(is_show=True, pos_top='bottom'),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 渲染数据
line.render('../../resource/html/line.html')
