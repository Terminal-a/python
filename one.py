import requests
import re
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'
}
response = requests.get('https://www.tupianzj.com/meinv/xiezhen/', headers=headers)
response.ancoding = "utf-8"
html = response.text
# print(html)
# 解析网页,正则匹配图片地址
urls = re.findall('src="(.*?)"', html)
print(urls)
dir = 'images'
if not os.path.exists(dir):
    os.mkdir(dir)
# 保存图片
for url in urls:
    time.sleep(0.2)
    r = requests.get(url, headers=headers)
    name = url.split('/')[-1]
    with open(dir+'/'+name, 'wb')as f:
        f.write(r.content)
	f.close()
print("successful finish")
