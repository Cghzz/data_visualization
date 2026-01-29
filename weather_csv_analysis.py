import csv
import matplotlib.pyplot as plt
from datetime import datetime

from PIL.PdfParser import decode_text

filename='./湖州2025年天气数据.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    print(header_row)
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    highs,dates,lows=[],[],[]

    for row in reader:
        try:
            high=float(row[1])
            low=float(row[2])
        except:
            print(f'{datetime.strptime(row[0],'%Y-%m-%d')},温度数据丢失')
        else:
            highs.append(high)
            lows.append(low)
            #将字符串解析为日期时间对象
            dates.append(datetime.strptime(row[0],'%Y-%m-%d'))
    print(highs)
    print(dates)

# 根据最高温度绘制图形
flg,ax=plt.subplots()
ax.set_title('湖州市2025年每日最高温度',font={'family':'STSong','size':'24'})
ax.set_xlabel('日期',font={'family':'STSong','size':'10'})
flg.autofmt_xdate()
ax.set_ylabel('最高温度',font={'family':'STSong','size':'10'})
ax.tick_params(axis='both',which='major',labelsize=10)
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='green',alpha=0.5)
# 给图表区域着色
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)
plt.show()