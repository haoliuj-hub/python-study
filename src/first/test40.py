"""
时间线柱状图
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

data = ['中国', '美国', '日本', '韩国', '英国', '法国', '德国']

bar1 = Bar()
# 添加数据
bar1.add_xaxis(data)
bar1.add_yaxis('GPD', [80, 90, 76, 60, 75, 40, 57], label_opts=LabelOpts(position='right'))
# 反转坐标轴
bar1.reversal_axis()

bar2 = Bar()
# 添加数据
bar2.add_xaxis(data)
bar2.add_yaxis('GPD', [90, 95, 86, 70, 70, 50, 67], label_opts=LabelOpts(position='right'))
# 反转坐标轴
bar2.reversal_axis()

bar3 = Bar()
# 添加数据
bar3.add_xaxis(data)
bar3.add_yaxis('GPD', [102, 105, 76, 60, 75, 40, 57], label_opts=LabelOpts(position='right'))
# 反转坐标轴
bar3.reversal_axis()

timeline = Timeline({'theme': ThemeType.LIGHT})
# 添加数据
timeline.add(bar1, '2018年')
timeline.add(bar2, '2019年')
timeline.add(bar3, '2020年')

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 绘图
timeline.render('../../resource/html/时间线柱状图.html')
