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

			
if os.path.isdir("temp") == False: # creating temp directory
	os.mkdir("temp")						


username = os.getenv("GITHUB_ACTOR")
token = os.getenv("github_token")



entries = os.listdir(listfolder) # for all listfiles
entries.sort(key=str.lower)		
for entry in entries:
	with open(listfolder + entry, "r") as file1:
		x = file1.readline()
		x = file1.readline()
		x = file1.readline()
		directlink = x.replace("directlink=","")
	if directlink == "N/A\n": # when there is a direct link
		continue
	else:
		directlink = directlink.strip()
		pluginname = entry[:len(entry) -4] # removes '.txt'
		print("\ndirectlink found for: " + pluginname)
		withdots = pluginname.replace(" ", ".") # getting asset file name
		withdots = withdots.replace("'", ".")
		withdots = withdots.replace(",", ".") 
		withdots = withdots.replace("(", ".") 
		withdots = withdots.replace(")", ".") 
		withdots = withdots.replace("&", ".")  
		withdots = withdots.replace("...", ".")
		withdots = withdots.replace("..", ".")
		if withdots[len(withdots)-1] == ".":
			withdots = withdots[:len(withdots)-1]
		directzip = directlink.split(os.sep)
		directzip = str(directzip[len(directzip)-1])
		
		try: # check if asset file is there, and get assetlastmodified
			response = requests.head(assetfullpath + withdots + ".zip", allow_redirects=True)
			response.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print(err)
			assetlastmodified = "FALSE"
		else:
			modif = response.headers['Last-Modified']
			datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
			assetlastmodified = datetime_object.date()
		
		try: # check directlink
			response = requests.head(directlink, allow_redirects=True)
			response.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print("ABORTING: directlink not reachable")
			print(err)
			continue
		else: 
			try: # checking if last-modified/content-length tags are there
				modif = response.headers['Last-Modified']
				datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
				linklastmodified = datetime_object.date()
				linksize = int(response.headers['Content-Length']) / 1024 # get size in kb
			except:
				if directlink[:18] == "https://github.com": # check if github repo
					urllist = directlink.split(os.sep)
					author = urllist[3]
					plug = urllist[4]
					linksize = "FALSE"
					try: # check gifhub api for last commit
						params = {'page': '1', 'per_page': '1'}
						response = requests.get('https://api.github.com/repos/' + author +'/' + plug + '/commits', params=params, auth=(username,token))
					except:
						print("ABORTING: github api not reachable")
						linklastmodified = "FALSE"
						continue
					else: # get last commit date and time
						cont = str(response.content)
						dateandtime = cont.split(",")[4]
						commitdate = dateandtime[8:18] 
						committime = dateandtime[19:27]
						linklastmodified = datetime.strptime(commitdate, '%Y-%m-%d').date()
		if linksize != "FALSE":
			if linksize >= 102400:
				print("ABORTING: directlink is bigger than 100 mb")
				continue
		if linklastmodified != "FALSE":
			if assetlastmodified != "FALSE":
				datediff = linklastmodified - assetlastmodified # both lastmodified were successful, compare them
				if datediff.days < 1: 
					print("ABORTING: assetfile is newer | link: " + str(linklastmodified) + " asset: " + str(assetlastmodified) + " datediff: " + str(datediff.days))
				else:	
					print("SUCCESS: linkfile is newer")
					with open("temp/" + pluginname + ".zip", "wb") as file2: # create zip file
						r = requests.get(directlink, allow_redirects=True)
						file2.write(r.content)
						print("SUCCESS: downloaded zip")
			else:
				print("no assetfile, must be a new plugin")
				with open("temp/" + pluginname + ".zip", "wb") as file2: # create zip file
					r = requests.get(directlink, allow_redirects=True)
					file2.write(r.content)
					print("SUCCESS: downloaded zip")
				
# extracting zips
listing = glob.glob("temp/*.zip")
print("\nlast modified checks DONE, extracting zips now")
for entry in listing:
	# unzip all zips
	with ZipFile(entry, 'r') as zObject:
		zObject.extractall("temp/")
		firstfolder = zObject.namelist()[0] # first folder inside zip, should be pluginname
		firstfolder = firstfolder[:len(firstfolder) -1]
		ossep = entry.split(os.sep)
		stripped = ossep[1]
		stripped = stripped[:len(stripped)-4] # pluginname stripped from zip name
		print("\n" + entry + " | extacted to: temp/" + firstfolder)
		# check for same names of zip and first folder in zip
		if stripped != firstfolder:
			print("ERROR: mismatch between zipname and in-zip folder!")
			shutil.move("temp/" + firstfolder, "temp/" + stripped)
			print("temp/" + firstfolder + " | renamed to: temp/" + stripped)
		if os.path.isdir(pathtoplugins + stripped):
			shutil.rmtree(pathtoplugins + stripped) # delete old plugin
		shutil.move("temp/" + stripped, pathtoplugins + stripped)
	with open("res/news.txt", "r") as file1: 
		news = file1.readlines()
	with open("res/news.txt", "w") as file1: # write to news file, newest on top, keep old contents
		today = datetime.today().strftime('%Y-%m-%d')
		with open("res/pluginlist/" + stripped + ".txt") as file2:
			author = file2.readline()
			author = author.replace("author=", "")
			author = author.strip()
			c = file2.readline()
			c = file2.readline()
			c = file2.readline()
			c = c.replace("category=", "")
			c = c.strip()
			if c == "N/A":
				c = "uncategorized"
			c = "[" + c + "](" + webroot + indexfile + "#" + c + ")\n" # anchor link to category
		news = [today + " '" + stripped + "' updated by " + author + " | category: " + c] + news
		file1.writelines(news)
	# renaming zips to asset convention
	withdots = stripped.replace(" ", ".") 
	withdots = withdots.replace("'", ".")
	withdots = withdots.replace(",", ".") 
	withdots = withdots.replace("(", ".") 
	withdots = withdots.replace(")", ".") 
	withdots = withdots.replace("&", ".") 
	withdots = withdots.replace("...", ".")
	withdots = withdots.replace("..", ".")
	if withdots[len(withdots)-1] == ".":
		withdots = withdots[:len(withdots)-1]
	shutil.move(entry, "temp/" + withdots + ".zip")
