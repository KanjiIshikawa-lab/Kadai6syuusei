# -*- coding: utf-8 -*-
 
import requests
import pandas as pd
import pytest
import urllib
import pprint

# 課題1
def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    print(get_api(url))


main()

# 課題2
url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
 
payload = {
    'applicationId': 1017762098426453356,
    'keyword': 'Python',
    'hits': 10,
    'sort': '+itemPrice',
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()

pprint.pprint(resp)
print ("num of kensaku =",resp['count'])
print ('-'*40)
 
for i in resp['Items']:
    item = i['Item']
    print (item['itemName'])
    print (item['itemPrice'], 'yen')

# 課題3
url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
 
payload = {
    'applicationId': 1017762098426453356,
    'keyword': 'rakuten',
    'hits': 10,
    'genreId': 560278,
    }
 
r = requests.get(url, params=payload)


resp = r.json()


a=[]
b=[]


for i in resp['Products']:
    item = i['Product']
    a.append(item['minPrice'])
    b.append(item['maxPrice'])
    print (item['minPrice'], 'yen')
    print(item['maxPrice'], 'yen')
print("最安値は、", min(a), "円です。")
print("最高値は、", max(b), "円です。")
 
#課題4
url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222'
 
payload = {
    'applicationId': 1017762098426453356,
    'keyword': 'Python',
    'hits': 10,
    'sort': '-itemPrice',
    'rankTargetProductCount':30485
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()


print ("num of kensaku =",resp['count'])
print ('-'*40)
a=[]
b=[]

for i in resp['Items']:
    item = i['Item']
    a.append(item['itemName'])
    b.append(item['itemPrice'])
    print (item['itemName'])
    print (item['itemPrice'], 'yen')
print(len(a), len(b))


df = pd.DataFrame({"Items":a,
                "Prices":b})
df.to_csv("/Users/ishikawakanji/Desktop/kadai6/item.csv", encoding="utf-8-sig")

#課題5
def test_get_rakutenAPI():
    price_list = list(item['itemName'])
    
    for i in price_list:
        print(i)

    assert len(i)>=1
    assert price_list[0].title