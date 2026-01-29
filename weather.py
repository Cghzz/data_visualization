import webbrowser

import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

# 用pandas.read_csv()读取指定excel文件,选择编码格式gb18030
df = pd.read_csv('./湖州2025年天气数据.csv', encoding='gb18030')
print(df['日期'])
# 将日期一列的 字符串数据类型转为日期数据类型,如果不是datetime类型
# 没有办法做这个类型的相关操作
# apply函数的使用,pandas的apply()函数可以作用于Series或者整个DataFrame
# 功能也是自动遍历整个Series或者DataFrame,对每一个元素运行指定的函数
# 以及匿名函数的使用(lambda传入值:返回的表达式)
# 也就是说,把日期列的每一个数据传入到匿名函数表达式中,返回的数据是日期格式
df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))

df['月份'] = df['日期'].dt.month
print(df['月份'])

# 如果不重置索引,那么会默认把month列作为索引列,尔此时的索引已经不是连续索引了
# 所以需要reset_index()重置索引
df_agg = df.groupby(['月份', '天气']).size().reset_index()
print(df_agg)
# 设置下这三列的列名
df_agg.columns=['月份','天气','数量']
print(df_agg)
#天气数据的形成
#选择一月的所有数据,将里面的天气,数量2列数据拿出来排序
#以数量列为依据,逆序,因为目前取出来的是DataFrame的数据类型
# .value:拿出来的数据是一个numpy.ndarray数字,在用.tolist()转为列表
print(df_agg[df_agg['月份']==1][['天气','数量']]\
      .sort_values(by='数量',ascending=False).values.tolist())

#画图
#实例化一个时间序列对象
timeline=Timeline()
#播放参数:设置时间间隔1s 单位是ms
timeline.add_schema(play_interval=1000)
#循环遍历df['月份']里的唯一值
for month in df_agg['月份'].unique():
    data=(df_agg[df_agg['月份']==month][['天气','数量']]
    .sort_values(by='数量',ascending=False).values.tolist())
    print(data)
    #绘制柱状图
    bar=Bar()
    #x轴是天气
    bar.add_xaxis([x[0] for x in data])
    #y轴是出现次数
    bar.add_yaxis('',[x[1] for x in data])
    #让柱状图横着放
    bar.reversal_axis()
    #将计数表情放置在图像油泵
    bar.set_series_opts(label_opts=opts.LabelOpts(position='right'))
    #设置下图标名称
    bar.set_global_opts(title_opts=opts.TitleOpts(title='湖州市2025年每月天气变化'))
    #将设置好的bar对象放置到时间轮播图当中,并且标签选择月份
    timeline.add(bar,f'{month}月')
#将设置好的图表保存为'weather.html'
timeline.render('weather.html')
webbrowser.open('weather.html')
