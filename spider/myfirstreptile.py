#!/usr/bin/env python
# coding=UTF-8
'''
@Description: In User Settings Edit
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-14 00:07:00
@LastEditTime: 2019-03-14 20:59:30
'''
import requests
from PIL import Image
from io import BytesIO
import json
# url = 'Request URL'
# url = 'https://search.jd.com/search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%94%B5%E8%84%91&cid2=671&cid3=672&ev=exbrand_%E5%8D%8E%E7%A1%95%EF%BC%88ASUS%EF%BC%89%5E&uc=0'

# url = 'https://api.github.com/events'
# res = requests.get(url)

# res = requests.post('http://httpbin.org/post', data = {'key':'value'})

# res = requests.put('http://httpbin.org/put', data = {'key':'value'})
# res = requests.delete('http://httpbin.org/delete')
# res = requests.head('http://httpbin.org/get')
# res = requests.options('http://httpbin.org/get')

# payload = {'key1':'value1', 'key2':'value2'}
# res = requests.get("http://httpbin.org/get", params=payload)

# payload = {'key1':'value1', 'key2':['value2','value3']}
# res = requests.get('http://httpbin.org/get', params = payload)

# res = requests.get('https://api.github.com/events')
# res.encoding = 'utf-8'
# res.encoding = 'ISO-8859-1'
# print(res.text)

# i = Image.open(BytesIO(res.content))
# res = requests.get('https://api.github.com/events')

# res.encoding = 'utf-8'
# print(res.json())
# print(res.raise_for_status())
# print(res.status_code)

# res = requests.get('http://api.github.com/events', stream=True)
# print(res.raw)
# print(res.raw.read(10))

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# res = requests.get(url, headers=headers)
# print(res.headers)


# payload = {'key1': 'value1', 'key2': 'value2'}
# res = requests.post("http://httpbin.org/post", data=payload)
# print(res.text)
# print(res.headers)

# payload = (('key1', 'value1'),('key1', 'value2'))
# res = requests.post('http://httpbin.org/post', data=payload)
# print(res.text)
# print(res.url)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# res = requests.post(url, data=json.dumps(payload))
# res = requests.post(url, json=payload)
# print(res.text)

# url = 'http://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
# res = requests.post(url, files=files)
# print(res.text)


# res = requests.get('http://httpbin.org/get')
# print(res.status_code)
# print(res.status_code == requests.codes.ok)
# bad_res = requests.get('http://httpbin.org/status/404')
# print(bad_res.status_code)
# bad_res.raise_for_status()
# res.raise_for_status()
# print(res.headers)
# print(res.headers['Content-Type'])
# print(res.headers['Content-Encoding'])
# print(res.headers['Access-Control-Allow-Credentials'])
# print(res.headers['Server'])
# print(res.headers['Date'])

# print(res.headers.get('content-type'))
# print(res.headers.get('content-encoding'))
# print(res.headers.get('Content-Type'))
# print(res.headers.get('Content-Encoding'))
# print(res.headers.get('Server'))
# print(res.headers.get('server'))
# print(res.headers.get('Date'))
# print(res.headers.get('date'))

'''
Cookie
'''

# url = 'http://example.com/some/cookie/setting/url'
# res = requests.get(url)
# print(res.text)
# print(res.cookies)
# print(res.cookies['example_cookie_name'])

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# res = requests.get(url, cookies=cookies)
# print(res.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# res = requests.get(url, cookies=jar)
# print(res.text)
# print(res.url)

'''
history
'''

# res = requests.get('http://github.com', timeout=0.001)
# print(res.url)
# print(res.status_code)
# print(res.history)
