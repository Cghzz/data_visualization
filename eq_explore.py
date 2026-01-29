import json
import webbrowser
import pandas as pd
import plotly.express as px

from mpl_squares import fig

# 探索数据结构
filename = './data/eq_data_30_day_m1.json'
with open(filename) as f:
    # load 将数据转为Python能够处理的格式,这里是一个字典
    all_eq_data = json.load(f)
# print(all_eq_data)
# readable_file = './data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     # dump将JSON数据对象写入文件对象,
#     # indent=4让dump函数使用与数据结构匹配的缩进来设置数据格式
#     json.dump(all_eq_data, f, indent=4)

all_eq_dict = all_eq_data['features']
# print(len(all_eq_dict))
# print(all_eq_dict)
mags, coordinates, titles = [], [], []
lons, lats = [], []

for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    coord = eq_dict['geometry']['coordinates']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    coordinates.append(coord)
    titles.append(title)
data=pd.DataFrame(data=zip(lons, lats, mags, titles),
                  columns=['经度', '纬度', '震级', '位置'])
data.head()
# 绘制震级散点图
# fig = px.scatter(x=lons,
#                  y=lats,
#                  labels={'x': '经度', 'y': '纬度'},
#                  range_x=[min(lons), max(lons)],
#                  range_y=[min(lats), max(lats)],
#                  width=800,
#                  height=800,
#                  title='全球地震散点图', )
fig = px.scatter(data,
                 x='经度',
                 y='纬度',
                 labels={'x': '经度', 'y': '纬度'},
                 range_x=[min(lons), max(lons)],
                 range_y=[min(lats), max(lats)],
                 width=800,
                 height=800,
                 title='全球地震散点图',
                 size='震级',
                 size_max=10,
                 color='震级',
                 hover_name='位置')
fig.write_html('全球地震散点图.html')
webbrowser.open('全球地震散点图.html')
# fig.show()
