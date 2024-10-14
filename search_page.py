
import requests
url = "https://isp.uv.es"
response = requests.get(url, verify=False)

# print text that contains ".html"
urls = []
for line in response.text.split("\n"):
    if (".html" in line) and ("href" in line) and (line != ''):
        href = line.split('href="')[1].split('"')[0]
        url = "https://isp.uv.es/" + href
        print(url)
        urls.append(url)


import os
# raster todos lo archivos .html de este directorios e hijos
dir = "D:\GitHub\page_ipl_practice\content"

urls = []
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith(".html"):
            url = os.path.join(root, file)
            urls.append(url)