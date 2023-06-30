import requests
from datetime import datetime
import git
import os

directlink = "https://github.com/1010todd/Mega-Freight/archive/refs/heads/main.zip"
asset = "https://github.com/Hecter94/EndlessSky-PluginArchive/releases/download/Latest/Mega.Freight.zip"

directlinkb = "https://github.com/zuckung/endless-sky-plugins/releases/download/Latest/additional.command.buttons.zip"
assetb = "https://github.com/Hecter94/EndlessSky-PluginArchive/releases/download/Latest/additional.command.buttons.zip"

os.environ["GIT_PYTHON_REFRESH"] = "quiet"


repo = git.Repo("https://github.com/1010todd/Mega-Freight/")
tree = repo.tree()
for blob in tree:
	commit = next(repo.iter_commits(paths=blob.path, max_count=1))
	print(blob.path, commit.committed_date)




#response = requests.head(directlink, allow_redirects=True)
#response.raise_for_status()
#print(response.headers)
#print("\n")

#response = requests.head(asset, allow_redirects=True)
#response.raise_for_status()
#print(response.headers)
#print("\n")

#print("b\n")

#response = requests.head(directlinkb, allow_redirects=True)
#response.raise_for_status()
#print(response.headers)
#print("\n")

#response = requests.head(assetb, allow_redirects=True)
#response.raise_for_status()
#print(response.headers)