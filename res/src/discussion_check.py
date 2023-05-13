import requests
import os
from bs4 import BeautifulSoup

# check for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test2/src":
	os.chdir("../../") 

# read paths and files
with open("res/paths.txt") as f:
	for line in f:
		line = str((line.strip()))
		if line.find("pathtoplugins") == 0:	# i.e. pathtoplugins = myplugins/
			pathtoplugins = line.split(" = ")[1]
		elif line.find("indexfile") == 0: 		# i.e.indexfile = README.md
			indexfile = line.split(" = ")[1]
		elif line.find("assetfiles") == 0:	   # i.e. assetfiles = https://github.com/zuckung/test/releases/download/Latest/
 			assetfiles = line.split(" = ")[1]
		elif line.find("pluginurl") == 0:		 # i.e pluginurl = https://github.com/zuckung/test/tree/main/myplugins/
			pluginurl = line.split(" = ")[1]
		elif line.find("headerfile") == 0:	  # i.e. headerfile = res/header.txt
			headerfile = line.split(" = ")[1]
		elif line.find("picturefile") == 0:	  # i.e picturefile = res/icon.png
			picturefile = line.split(" = ")[1]
		elif line.find("discurl") == 0:	         # i.e https://github.com/zuckung/test2/discussions/2
			discurl = line.split(" = ")[1]
		elif line.find("pluginlistfolder") == 0: # i.e pluginlist/
			pluginlistfolder= line.split(" = ")[1]

# read discussion thread 2 and get all urls
reqs = requests.get(discurl)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
zips = set()
zipsc = set()
# find all urls with .zip in it
for link in soup.find_all('a'):
	check = link.get('href')
	pos = check.find(".zip")
	if pos > 2:
		zips.add(check) # added all links with '.zip'
		zipsc.add(check) # for compare

# reading links file and reopen for adding		
file1 = open("res/dlinks.txt", "r")
lines = file1.readlines()
file1.close

# check for allready added files and remove from zipsc
# so zipsc has only new added zip urls, while zips has all zip urls
for line in lines: 
	linec = line.replace("\n", "")
	for zipfile in zips:
		if linec == zipfile:
			zipsc.remove(zipfile)

if len(zipsc) == 0:
	print("Nothing added!")
else:
	# rewriting links file with all zip links
	print(zipsc , " new links added!")
	file1 = open("res/dlinks.txt", "w")
	zips = sorted(zips)
	for zipfile in zips:
		file1.writelines(zipfile)
		file1.writelines("\n")
	file1.close
	print("all links written to res/dlinks.txt")


# downloading new zip files
for zipfile in zipsc:
	r = requests.get(zipfile, allow_redirects=True)
	parts = zipfile.split(os.sep)
	last = parts[len(parts) -1]
	open(last, 'wb').write(r.content)
	print(last + " downloaded!")