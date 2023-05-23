"""
GDP柱状图案例
"""
from pyecharts.charts import Timeline, Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

f = open('../../resource/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv', 'r', encoding='gbk')

dict_data = dict()

for line in f:
    if line.startswith('year'):
        continue
    line = line.replace('\n', '')
    line_list = line.split(',')
    year = line_list[0]
    country = line_list[1]
    gdp = line_list[2]
    # gdp 单位转换为亿元
    gdp = round(float(gdp) / 100000000, 2)
    if year not in dict_data:
        dict_data[year] = list()
        dict_data[year].append([country, gdp])
    else:
        dict_data[year].append([country, gdp])

f.close()

timeline = Timeline({'theme': ThemeType.LIGHT})

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

for year in dict_data:
    bar = Bar()
    dict_data[year].sort(key=lambda x: x[1], reverse=True)
    temp = dict_data[year][0:8]
    bar.add_xaxis([i[0] for i in temp][::-1])
    bar.add_yaxis('GDP(亿元)', [i[1] for i in temp][::-1], label_opts=LabelOpts(position='right'))
    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title='{}年全球GDP排名'.format(year))
    )
    timeline.add(bar, year)

timeline.render('../../resource/html/GDP动态时间线柱状图.html')
