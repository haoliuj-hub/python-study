"""
案例分析
"""
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, LabelOpts

from second.test48_file_define import Record
from second.test48_file_reader import TxtReader, JSONReader

txt_reader = TxtReader('../../resource/2011年1月销售数据.txt')
data: list[Record] = txt_reader.read_data()

json_reader = JSONReader('../../resource/2011年2月销售数据JSON.txt')
data2: list[Record] = json_reader.read_data()

data_all = data + data2

# 求每天总销售额
day_dict = dict()
for record in data_all:
    if record.date in day_dict:
        day_dict[record.date] += record.money
    else:
        day_dict[record.date] = record.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(day_dict.keys()))

bar.add_yaxis('销售额', list(day_dict.values()), label_opts=LabelOpts(is_show=False))

bar.render('../../resource/html/每天总销售额.html')
