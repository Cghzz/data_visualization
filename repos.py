import webbrowser

import requests
from plotly.graph_objs import Bar
import plotly.offline as offline


from rate_limit import rate_limit
# 执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers={'Accept':'application/vnd.github.v3+json'}
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7'}
response=requests.get(url,headers=headers)
print(response.status_code)
#将API响应赋值给一个变量
response_dict=response.json()
#处理结果
print(response_dict.keys())
total_count=response_dict['total_count']
print(total_count)
#探索有关仓库的信息
repo_dicts=response_dict['items']
#研究第一个仓库
repo_dict=repo_dicts[0]
print(f'keys:{len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#     print(key)

print(f'打印仓库信息')
repo_links,repo_names,stars,labels=[],[],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    owner=repo_dict['owner']['login']
    description=str(repo_dict['description'])
    label=owner+'<br />'+description
    labels.append(label)
    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
# for repo in repo_dict:
#     repo_names.append(repo['name'])
# for i in range (len(repo_dict)):
#     print (f'仓库名字:{repo_dicts[0]["name"]}')
#     print (f'所有者:{repo_dicts[0]["owner"]['login']}')
#     print (f'Stars:{repo_dicts[0]["stargazers_count"]}')
#     print (f'仓库地址:{repo_dicts[0]["html_url"]}')
#     print (f'创建时间:{repo_dicts[0]["created_at"]}')
#     print (f'更新时间:{repo_dicts[0]["updated_at"]}')
#     print (f'描述:{repo_dicts[0]["description"]}')
#     print('\n')
# rate_limit()
# 可视化
data=[{'type':'bar',
        'x':repo_links,
        'y':stars,
        'marker':{'color':'rgb(60,100,150)','line':{'width':1.5,'color':'rgb(25,25,25)'}},
       'opacity':0.5,
       'hovertext':labels,
       }]
my_layout={
    'title':'GitHub上最受欢迎的Python项目',

    'xaxis': {'title':'仓库名'},
    'yaxis': {'title':'点赞数'}
}
fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='GitHub上最受欢迎的Python项目.html')
# webbrowser.open('GitHub上最受欢迎的Python项目.html')
