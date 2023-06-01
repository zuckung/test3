import os
import requests
from datetime import datetime
import glob
import shutil
from zipfile import ZipFile


# check for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test3/res/src":
	os.chdir("../../")

# read paths and files
with open("res/config.txt") as f:
	for line in f:
		line = str((line.strip()))
		if line.find("indexfile") == 0:	# i.e. indexfile = README.md | can get changed to whatever file you want the script output go
			indexfile = line.split(" = ")[1]
		if line.find("template") == 0:	# i.e. template = res/template.txt | a template how the indexfile should look, can be edited
			template = line.split(" = ")[1]
		if line.find("listfolder") == 0:	# i.e. listfolder = res/pluginlist/ | folder to where the plugin descriptions files are
			listfolder = line.split(" = ")[1]
		if line.find("pathtoplugins") == 0:	# i.e. pathtoplugins = myplugins/ | folder where the plugin folder and files are
			pathtoplugins = line.split(" = ")[1]
		if line.find("webroot") == 0:	# i.e. webroot = https://github.com/zuckung/test3/blob/main/
			webroot = line.split(" = ")[1]	
		if line.find("pluginurl") == 0:	# i.e. pluginurl = https://github.com/zuckung/test3/tree/main/Working/All%20Plugins/
			pluginurl = line.split(" = ")[1]
		if line.find("assetfullpath") == 0:	# i.e. assetfullpath = https://github.com/zuckung/test3/releases/download/Latest/
			assetfullpath = line.split(" = ")[1]
			
			
			
			
entries = os.listdir(listfolder) # for all listfiles
entries.sort(key=str.lower)
for entry in entries:
	with open(listfolder + entry, "r") as file1:
		x = file1.readline()
		x = file1.readline()
		x = file1.readline()
		directlink = x.replace("directlink=","")
		if directlink != "N/A\n": # when there is a direct link
			directlink = directlink.strip()
			pluginname = entry[:len(entry) -4]
			print("directlink found for: " + pluginname)
			withdots = pluginname.replace(" ", ".") 
			withdots = withdots.replace("'", ".")
			withdots = withdots.replace(",", ".") 
			withdots = withdots.replace("(", ".") 
			withdots = withdots.replace(")", ".") 
			withdots = withdots.replace("&", ".") 
			withdots = withdots.replace(",", ".") 
			withdots = withdots.replace("...", ".")
			withdots = withdots.replace("..", ".")
			if withdots[len(withdots)-1] == ".":
				withdots = withdots[:len(withdots)-1]
			directzip = directlink.split(os.sep)
			directzip = str(directzip[len(directzip)-1])
			if directzip[:len(directzip) - 4] != pluginname: # checking for same name
				print("ABORTING: naming convention mismatch")
			else:
				print("SUCCESS: naming convention match")		
						
				try: # check asset file
					response = requests.head(assetfullpath + withdots + ".zip", allow_redirects=True)
					response.raise_for_status()
				except requests.exceptions.HTTPError as err:
					print(err)
				else:
					response = requests.head(assetfullpath + withdots + ".zip", allow_redirects=True)
					response.raise_for_status()
					modif = response.headers['Last-Modified']
					datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
					assetlastmodified = str(datetime_object.date())
					try: # check directlink
						response = requests.head(directlink, allow_redirects=True)
						response.raise_for_status()
					except requests.exceptions.HTTPError as err:
						print(err)
					else:
						response = requests.head(directlink, allow_redirects=True)
						response.raise_for_status()
						modif = response.headers['Last-Modified']
						datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
						linklastmodified = str(datetime_object.date())
						if assetlastmodified == linklastmodified: # both lastmodified were successful, compare them
							print("ABORTING: both files have same last modified header")
						else:	
							print("SUCCESS: both files have different last modified header")
						
							assetsize = int(response.headers['Content-Length']) / 1024 # get size in kb
							if assetsize >= 102400:
								print(assetsize)
								print("ABORTING: directlink is bigger than 100 mb")
							else:
								print("SUCCESS: file is smaller than 100 mb")
								with open(directzip, 'wb') as file2:
									r = requests.get(directlink, allow_redirects=True)
									file2.write(r.content)
									print("SUCCESS: downloaded zip")
						

# extracting zips
listing = glob.glob('*.zip')
print("last modified checks DONE, extracting zips now")
print(listing)
for entry in listing:
	# unzip all zips
	with ZipFile(entry, 'r') as zObject:
		zObject.extractall()
		firstfolder = zObject.namelist()[0]
		firstfolder = firstfolder[:len(firstfolder) -1]
		stripped = entry[:len(entry)-4]
		print(entry + " | extacted to: " + firstfolder)
		# check for same names of zip and first folder in zip
		if stripped != firstfolder:
			print("ERROR: mismatch between zipname and in-zip folder!")	
			shutil.move(firstfolder, stripped)
			print(firstfolder + " | renamed to: " + stripped)	
		print(os.listdir())	
		shutil.rmtree(pathtoplugins + stripped)
		shutil.move(stripped, pathtoplugins + stripped)
		print(os.listdir())
	with open("res/news.txt", "r") as file1: 
		news = file1.readlines()
	with open("res/news.txt", "w") as file1: # write to news file
		today = datetime.today().strftime('%Y-%m-%d')
		news = [today + " '" + stripped + "' updated\n"] + news
		file1.writelines(news)
		
					