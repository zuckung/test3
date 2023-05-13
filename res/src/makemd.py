import os
import requests
from datetime import datetime

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

# write header
file2 = open(headerfile, "r")
header = file2.readlines()
file2.close
print("writing header")
file1 = open(indexfile, "w")
file1.writelines(header)


# read folders, and write to README.md
entries = os.listdir(pathtoplugins)
entries.sort(key=str.lower)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")


	# get description out of pluginlist file
	if os.path.exists(pluginlistfolder + entry + ".txt") == True:
		file2 = open(pluginlistfolder + entry + ".txt" , "r")	
		author = file2.readline()
		author = author.split("=")[1]
		author = author.replace("\n", "")
		website = file2.readline()
		website = website.split("=")[1]
		website = website.replace("\n", "")
		category = file2.readline()
		category = category.split("=")[1]
		category = category.replace("\n", "")
		status = file2.readline()
		status = status.split("=")[1]
		status = status.replace("\n", "")
		description = file2.readlines()
		description = description.replace("description=", "")
	file2.close 	
	
	# get last modified date from the assetfiles
	response = requests.head(assetfiles + withdots + ".zip", allow_redirects=True)
	modif = response.headers['Last-Modified']
	datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
	modif = str(datetime_object.date())


	# get file size of the assetfiles in kb or mb
	assetsize = int(response.headers['Content-Length']) / 1024
	form = " kb"
	if assetsize > 1024 :
		assetsize = assetsize / 1024
		form = " mb"
	
	# write the plugin informations to README.md
	print("writing  " + entry)
	file1.writelines("### " + entry + "\n")
	if os.path.exists(pathtoplugins + entry + "/icon.png") == True:
		file1.writelines("<img src='"+ pathtoplugins + entry + "/icon.png' width='55'></img><br>\n")
	file1.writelines("[" + withdots + ".zip](" + assetfiles + withdots + ".zip) | ")
	file1.writelines(str(round(assetsize, 2)) + form)    
	file1.writelines(" | last upload: " + modif)
	file1.writelines(" | [view data files](" + pluginurl + forweb + "/) <br>\n")
	file1.writelines("created by: " + author + " | ")
	if website == "N/A":
		file1.writelines(website + "<br>\n")
	else:	
		file1.writelines("[" + website + "](" + website + ")<br>\n" )
	file1.writelines("category: " + category + " | status: " + status + "<br>\n\ndescription:<br>\n")
	for line in description:
		file1.writelines(">" + line)
	file1.writelines(" \n  ")
	file1.writelines("\n___ \n\n")
file1.close
