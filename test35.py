"""
疫情折线图案例
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts, LabelOpts


def load_file(file_name):
    # 读取文件
    f = open(file_name, 'r', encoding='utf-8')
    data = f.read()
    f.close()
    # 数据处理，去除头部jsonp_XXXXXX
    # 数据处理，去除尾部)
    data = data[26:-2]
    # 转换为字典
    data_json = json.loads(data)
    # 获取数据
    data_update = data_json['data'][0]['trend']['updateDate']
    data_confirm = data_json['data'][0]['trend']['list'][0]['data']
    data_x = list()
    data_y = list()
    for i in range(len(data_update)):
        if data_update[i] == '1.1':
            break
        data_x.append(data_update[i])
        data_y.append(data_confirm[i])
    return data_x, data_y


yd_data_x, yd_data_y = load_file('resource/可视化案例数据/折线图数据/印度.txt')

jp_data_x, jp_data_y = load_file('resource/可视化案例数据/折线图数据/日本.txt')

us_data_x, us_data_y = load_file('resource/可视化案例数据/折线图数据/美国.txt')

# 折线图
line = Line()

# 添加x轴数据
line.add_xaxis(yd_data_x)

# 添加y轴数据
line.add_yaxis('印度确诊人数', yd_data_y, label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数', jp_data_y, label_opts=LabelOpts(is_show=False))
line.add_yaxis('美国确诊人数', us_data_y, label_opts=LabelOpts(is_show=False))

line.set_colors(['red', 'blue', 'green'])
# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title='世界疫情折线图', pos_left='center', pos_bottom='bottom'),
    legend_opts=LegendOpts(is_show=True, pos_top='top'),
    toolbox_opts=ToolboxOpts(is_show=True)
)

# 渲染数据
line.render('resource/html/疫情.html')
