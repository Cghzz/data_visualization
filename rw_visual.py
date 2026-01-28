import matplotlib.pyplot as plt
from randomwalk import RandomWalk

while True:
    rw=RandomWalk(num_points=50_000)
    rw.fill_walk()
    x_values=rw.x_values
    y_values=rw.y_values
    flg,ax=plt.subplots(figsize=(15,9),dpi=256)
    ponit_numbers=range(rw.num_points)
    ax.scatter(x_values,y_values,c=ponit_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(x_values[-1],y_values[-1],c='red',edgecolors='none',s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running=input("是否开启另外一次随机漫步(y/n)")
    if keep_running=='n':
        break

