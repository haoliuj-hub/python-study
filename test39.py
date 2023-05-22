"""
柱状图
"""
from pyecharts.charts import Bar

bar = Bar()

# 添加数据
data = ['中国', '美国', '日本', '韩国', '英国', '法国', '德国']
bar.add_xaxis(data)

# 添加数据
data1 = [80, 90, 76, 60, 75, 40, 57]
bar.add_yaxis('GPD', data1)

# 绘图
bar.render('resource/html/基础柱状图.html')

# 反转坐标轴
bar.reversal_axis()

# 绘图
bar.render('resource/html/反转坐标轴.html')
