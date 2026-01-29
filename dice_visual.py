from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

results=[]
die=Die()
die2=Die(10)
for num in range(10000):
    result=die.roll()+die2.roll()
    results.append(result)
# print(results)

frequencies=[]
for value in range(2,die.num_sides*die2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果进行可视化
x_values=list(range(2,die.num_sides*die2.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]
# data=[Bar(x=x_values,y=frequencies),Bar(x=x_values,y=frequencies)]
x_axis_config={'title':'结果','dtick':'1','range':[0,18]}
# x_axis_config={'title':'结果','dtick':'1'}
y_axis_config={'title':'结果的频率'}
my_layout=Layout(title='掷一个D6和D10 10000次的结果',
                 xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6+d10.html')
