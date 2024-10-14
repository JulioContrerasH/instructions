import os

dir = r"D:\GitHub\IPL-UV.github.io\docs\old_pages"

urls = []

dir = "D:\\GitHub\\IPL-UV.github.io\\docs\\old_pages"

for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith(".html"):
            local_path = os.path.join(root, file)
            url = local_path.replace("D:\\GitHub\\IPL-UV.github.io\\docs", "https://ipl-uv.github.io")
            url = url.replace("\\", "/")
            urls.append(url)
            print(url) 