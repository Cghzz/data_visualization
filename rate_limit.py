import requests

def rate_limit():
    url='https://api.github.com/rate_limit'
    headers = {'accept': 'application/vnd.github.v3+json'}
    response=requests.get(url,headers=headers)
    result_dict=response.json()
    print(result_dict)