import os
import glob
import shutil
from zipfile import ZipFile

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

listing = glob.glob('*.zip')
for entry in listing:
	# unzip all zips
	with ZipFile(entry, 'r') as zObject:
		zObject.extractall(pathtoplugins)
		firstfolder = zObject.namelist()[0]
		firstfolder = firstfolder[:len(firstfolder) -1]
		stripped = entry[:len(entry)-4]
		print(entry + " | extacted to: " + pathtoplugins + firstfolder)
		# check for same names of zip and first folder in zip
		if stripped != firstfolder:
			print("mismatch between zipname and in-zip folder!")
			shutil.move(pathtoplugins + firstfolder, pathtoplugins + stripped)
			print(firstfolder + " | renamed to: " + stripped)
	
	# check for pluginlistfolder file in unzipped path
	source = pathtoplugins + stripped + "/" + stripped +".txt"
	target = pluginlistfolder + stripped +".txt"
	if os.path.exists(source) == True:
		# copy to pluginlistfolder
		shutil.copyfile(source, target)
	else:
		if os.path.exists(target) != True:
		# create empty pluginlistfolder file
			print(target + " created!")
			file1 = open(target, "w")
			file1.writelines("author = N/A\nwebsite = N/A\ncategory = N/A\nstatus = N/A\ndescription = \nN/A")
			file1.close