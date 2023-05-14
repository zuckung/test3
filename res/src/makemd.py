import os
import requests
from datetime import datetime
from PIL import Image



# check for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test3/res/src":
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
		elif line.find("headercategory") == 0:    # i.e. headerfile2 = res/header2.txt
			headercategory = line.split(" = ")[1]
		elif line.find("categoryfolder") == 0:    # i.e. categoryfolder = res/categories/
			categoryfolder = line.split(" = ")[1]
		elif line.find("picturefile") == 0:	  # i.e picturefile = res/icon.png
			picturefile = line.split(" = ")[1]
		elif line.find("discurl") == 0:	         # i.e https://github.com/zuckung/test2/discussions/2
			discurl = line.split(" = ")[1]
		elif line.find("pluginlistfolder") == 0: # i.e pluginlist/
			pluginlistfolder= line.split(" = ")[1]

def wentry(filex):
	# write the plugin information to a file
	filex.writelines("### " + entry + "\n<br>")
	if os.path.exists(pathtoplugins + entry + "/icon.png") == True:
		im = Image.open(pathtoplugins + entry + "/icon.png")
		w, h = im.size
		if h > w:
			filex.writelines("<img src='"+ pathtoplugins + entry + "/icon.png'' height='55'></img><br>\n")
		else:
			filex.writelines("<img src='"+ pathtoplugins + entry + "/icon.png'' width='55'></img><br>\n")
	filex.writelines("[" + withdots + ".zip](" + assetfiles + withdots + ".zip) | ")
	filex.writelines(assetsize + form)    
	filex.writelines(" | last upload: " + modif)
	filex.writelines(" | [view data files](" + pluginurl + forweb + "/) <br>\n")
	filex.writelines("Created by: " + author + " | ")
	if website == "N/A":
		filex.writelines(website + "\n")
	else:	
		filex.writelines("[" + website + "](" + website + ")<br>\n" )
	filex.writelines("Category: " + category + "\n\nDescription:\n")
	for l in description:
		filex.writelines(">" + l)
	filex.writelines(" \n" + "Status: " + status )
	filex.writelines("\n\n ")
	filex.writelines("___ \n\n")

def mdlist(filex):
	# write category overview
	if filex == file1:
		categoryfolderx = categoryfolder
		back = ""
	else:
		categoryfolderx = ""
		back = "../../"
	filex.writelines("\n\nCategories: <br>\n")
	filex.writelines("[Cheats](" + categoryfolderx + "cheats.md) (" + str(cheats) + 
						")  [Gameplay](" + categoryfolderx + "gameplay.md) (" + str(gameplay) + 
						")  [Graphics](" +  categoryfolderx + "graphics.md) (" + str(graphics) + 
						")  [Outfits](" + categoryfolderx + "outfits.md) (" + str(outfits) + 
						")<br>\n")
	filex.writelines("[Overhauls](" + categoryfolderx + "overhauls.md) (" + str(overhauls) + 
						")  [Overwrites](" + categoryfolderx + "overwrites.md) (" + str(overwrites) + 
						")  [Patches](" + categoryfolderx + "patches.md) (" + str(patches) + 
						")  [Races](" + categoryfolderx + "races.md) (" + str(races) + 
						")<br>\n")
	filex.writelines("[Ships](" + categoryfolderx + "ships.md) (" + str(ships) + 
						")  [Story](" + categoryfolderx + "story.md) (" + str(story) + 
						")  [Weapons](" + categoryfolderx + "weapons.md) (" + str(weapons) + 
						")  [Uncategorized](" + categoryfolderx + "uncategorized.md) (" + str(uncategorized) + 
						")<br>\n")
	filex.writelines(" Plugins in [all categories](" + back + indexfile + "): " + str(allplugins) + "\n\n\n")

allplugins = 0
cheats = 0
gameplay = 0
graphics = 0
outfits = 0
overhauls = 0
overwrites = 0
patches = 0
races = 0
ships = 0
story = 0
weapons = 0
uncategorized = 0

# counting categories
entries = os.listdir(pathtoplugins)
entries.sort(key=str.lower)
for entry in entries:
	allplugins += 1
	withdots = entry.replace(" ", ".")
	if os.path.exists(pathtoplugins + withdots + ".txt") == True:
		with open(pluginlistfolder + withdots + ".txt", "r") as checkfile:
			cat = checkfile.readline()
			cat = checkfile.readline()
			cat = checkfile.readline().split("=")[1].replace("\n", "")
			if cat == "cheats":
				cheats += 1
			elif cat == "gameplay":
				gameplay += 1
			elif cat == "graphics":
				graphics += 1
			elif cat == "outfits":
				outfits += 1
			elif cat == "overhauls":
				overhauls += 1
			elif cat == "overwrites":
				overwrites += 1
			elif cat == "patches":
				patches += 1
			elif cat == "races":
				races += 1
			elif cat == "ships":
				ships += 1
			elif cat == "story":
				story += 1
			elif cat == "weapons":
				weapons += 1
			else:
				uncategorized += 1
	else:
		uncategorized += 1

# reading headers
with open(headerfile, "r") as file2:
	header = file2.readlines()
with open(headercategory, "r") as file2:
	headercategory = file2.readlines()
# writing headers	
print("writing headers")
file1 = open(indexfile, "w") # README.md or whatever it is named
file1.writelines(header)
mdlist(file1)
file1.writelines("\n<h1>All Plugins: </h1>\n\n")
fcheats = open(categoryfolder + "cheats.md", "w")
fcheats.writelines(headercategory)
mdlist(fcheats)
fcheats.writelines("\n<h1>Plugin List 'Cheats':</h1>\n\n")
fgameplay = open(categoryfolder + "gameplay.md", "w")
fgameplay.writelines(headercategory)
mdlist(fgameplay)
fgameplay.writelines("\n<h1>Plugin List 'Gameplay':</h1>\n\n")
fgraphics = open(categoryfolder + "graphics.md", "w")
fgraphics.writelines(headercategory)
mdlist(fgraphics)
fgraphics.writelines("\n<h1>Plugin List 'Graphics':</h1>\n\n")
foutfits = open(categoryfolder + "outfits.md", "w")
foutfits.writelines(headercategory)
mdlist(foutfits)
foutfits.writelines("\n<h1>Plugin List 'Outfits':</h1>\n\n")
foverhauls = open(categoryfolder + "overhauls.md", "w")
foverhauls.writelines(headercategory)
mdlist(foverhauls)
foverhauls.writelines("\n<h1>Plugin List 'Overhauls':</h1>\n\n")
foverwrites = open(categoryfolder + "overwrites.md", "w")
foverwrites.writelines(headercategory)
mdlist(foverwrites)
foverwrites.writelines("\n<h1>Plugin List 'Overwrites':</h1>\n\n")
fpatches = open(categoryfolder + "patches.md", "w")
fpatches.writelines(headercategory)
mdlist(fpatches)
fpatches.writelines("\n<h1>Plugin List 'Patches':</h1>\n\n")
fraces = open(categoryfolder + "races.md", "w")
fraces.writelines(headercategory)
mdlist(fraces)
fraces.writelines("\n<h1>Plugin List 'Races':</h1>\n\n")
fships = open(categoryfolder + "ships.md", "w")
fships.writelines(headercategory)
mdlist(fships)
fships.writelines("\n<h1>Plugin List 'Ships':</h1>\n\n")
fstory = open(categoryfolder + "story.md", "w")
fstory.writelines(headercategory)
mdlist(fstory)
fstory.writelines("\n<h1>Plugin List 'Story':</h1>\n\n")
fweapons = open(categoryfolder + "weapons.md", "w")
fweapons.writelines(headercategory)
mdlist(fweapons)
fweapons.writelines("\n<h1>Plugin List 'Weapons':</h1>\n\n")
funcategorized = open(categoryfolder + "uncategorized.md", "w")
funcategorized.writelines(headercategory)
mdlist(funcategorized)
funcategorized.writelines("\n<h1>Plugin List 'Uncategorized':</h1>\n\n")

# read folders, and write to .md
entries = os.listdir(pathtoplugins)
entries.sort(key=str.lower)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")

	# get description out of pluginlist file
	if os.path.exists(pluginlistfolder + withdots + ".txt") == True:
		with open(pluginlistfolder + withdots + ".txt" , "r") as file2:
			author = file2.readline().split("=")[1].replace("\n", "")
			website = file2.readline().split("=")[1].replace("\n", "")
			category = file2.readline().split("=")[1].replace("\n", "")
			status = file2.readline().split("=")[1].replace("\n", "")
			description= file2.readlines()
			rem = description[0]
			description[0] = rem.replace("description=", "")
	
	# get last modified date from the assetfiles
	response = requests.head(assetfiles + withdots + ".zip", allow_redirects=True)
	modif = response.headers['Last-Modified']
	datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
	modif = str(datetime_object.date())

	# get file size of the assetfiles in kb or mb
	assetsize = int(response.headers['Content-Length']) / 1024
	form = " kb"
	if assetsize > 1024:
		assetsize = assetsize / 1024
		form = " mb"
	assetsize = str(round(assetsize, 2))

	
	# writing the plugin entries to the md files
	print("writing  " + entry)
	wentry(file1)
	category = str((category.strip()))
	if category == "cheats":
		wentry(fcheats)
	elif category == "gameplay":
		wentry(fgameplay)
	elif category == "graphics":
		wentry(fgraphics)
	elif category == "outfits":
		wentry(foutfits)
	elif category == "overhauls":
		wentry(foverhauls)
	elif category == "overwrites":
		wentry(foverwrites)
	elif category == "patches": 
		wentry(fpatches)
	elif category == "races":
		wentry(fraces)
	elif category == "ships":
		wentry(fships)
	elif category == "story":
		wentry(fstory)
	elif category == "weapons":
		wentry(fweapons)
	else:
		wentry(funcategorized)

fcheats.close
fgameplay.close
fgraphics.close
foutfits.close
foverhauls.close
foverwrites.close
fpatches.close
fraces.close
fships.close
fstory.close
fweapons.close
funcategorized.close
file1.close
