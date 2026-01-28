import matplotlib.pyplot as plt

x_values = range(1, 1001)
# y_values = range(1, 1001)
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values,c='red', s=10)
# ax.scatter(x_values, y_values,c=(0,0.8,0), s=10)
ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues, s=10)
# 设置图标标题并给坐标轴加上标签
ax.set_title('散点图', font={'family': 'STSong', 'size': '24'})
ax.set_xlabel('值', font={'family': 'STSong', 'size': '10'})
ax.set_ylabel('平方数', font={'family': 'STSong', 'size': '10'})
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=10)
# 设置坐标轴的取值范围
ax.axis([0, 1001, 0, 1001**2])
plt.ticklabel_format(style='plain')

plt.savefig('catter_squares.png',bbox_inches='tight')
plt.show()
