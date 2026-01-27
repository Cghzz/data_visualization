import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import axis

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
# fig表示整张图片,ax表示图片中的各个图标

plt.style.use('seaborn-v0_8-white')

fig, ax = plt.subplots()
# 根据给定的数据以有意义的方式绘制图表
# 向plot提供一些列数时,它假设第一个数据点对应的X坐标值为0,但这里第一个点对应值x为1
ax.plot(input_values, squares, linewidth=3)
# 设置图标标题并给坐标轴加上标签
# font_list = matplotlib.font_manager.fontManager.ttflist
# for font in font_list:
#     if ('Song' in font.name) or ('Hei' in font.name):
#         print(font.name)
ax.set_title("平方数", font={'family': 'STSong', 'size': '14'})
ax.set_xlabel("值", font={'family': 'STSong', 'size': '14'})
ax.set_ylabel('值得平方根', font={'family': 'STSong', 'size': '14'})
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 打开matplotlib查看器并显示绘制的图表
plt.show()
