import requests

directlink = "https://github.com/1010todd/Mega-Freight/archive/refs/heads/main.zip"
asset = "https://github.com/Hecter94/EndlessSky-PluginArchive/releases/download/Latest/Mega.Freight.zip"

params = {'page': '1', 'per_page': '1'}
response = requests.get('https://api.github.com/repos/1010todd/Mega-Freight/commits', params=params)
cont = str(response.content)
datetime = cont.split(",")[4]
date = datetime[8:18]
time = datetime[19:27]
print(date)
print(time)