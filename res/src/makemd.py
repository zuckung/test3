import os
import requests
from datetime import datetime

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
		elif line.find("picturefile") == 0:	  # i.e picturefile = res/icon.png
			picturefile = line.split(" = ")[1]
		elif line.find("discurl") == 0:	         # i.e https://github.com/zuckung/test2/discussions/2
			discurl = line.split(" = ")[1]
		elif line.find("pluginlistfolder") == 0: # i.e pluginlist/
			pluginlistfolder= line.split(" = ")[1]

def wentry(filex):
	# write the plugin informations to a file
	filex.writelines("### " + entry + "\n")
	if os.path.exists(pathtoplugins + entry + "/icon.png") == True:
		filex.writelines("<img src='"+ pathtoplugins + entry + "/icon.png' width='55'></img><br>\n")
	filex.writelines("[" + withdots + ".zip](" + assetfiles + withdots + ".zip) | ")
	filex.writelines(assetsize + form)    
	filex.writelines(" | last upload: " + modif)
	filex.writelines(" | [view data files](" + pluginurl + forweb + "/) <br>\n")
	filex.writelines("created by: " + author + " | ")
	if website == "N/A":
		filex.writelines(website + "<br>\n")
	else:	
		filex.writelines("[" + website + "](" + website + ")<br>\n" )
	filex.writelines("category: " + category + " | status: " + status + "<br>\n\ndescription:<br>\n")
	for line in description:
		filex.writelines(">" + line)
	filex.writelines(" \n  ")
	filex.writelines("\n___ \n\n")

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
	with open(pluginlistfolder + entry + ".txt", "r") as checkfile:
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

# reading headers
with open(headerfile, "r") as file2:
	header = file2.readlines()
with open(headercategory, "r") as file2:
	headercategory = file2.readlines()
# writing headers	
print("writing headers")
file1 = open(indexfile, "w") # README.md or whatever it is named
file1.writelines(header)
file1.writelines("Categories:<br><br>")
file1.writelines("[Cheats](cheats.md) (" + str(cheats) + ")  [Gameplay](gameplay.md) (" + str(gameplay) + 
					")  [Graphics](graphics.md) (" + str(graphics) + ")  [Outfits](outfits.md) (" + str(outfits) + ")<br>")
file1.writelines("[Overhauls](overhauls.md) (" + str(overhauls) + ")  [Overwrites](overwrites.md) (" + str(overwrites) + 
					")  [Patches](patches.md) (" + str(patches) + ")  [Races](races.md) (" + str(races) + ")<br>")
file1.writelines("[Ships](ships.md) (" + str(ships) + ")  [Story](story.md) (" + str(story) + 
					")  [Weapons](weapons.md) (" + str(weapons) + ")  [Uncategorized](uncategorized.md) (" + str(uncategorized) + ")<br><br>")
file1.writelines(" Plugins in all categories : " + str(allplugins) + "<br><br>\n## All Plugins:<br><br>")
fcheats = open("cheats.md", "w")
fcheats.writelines(headercategory)
fcheats.writelines(" Plugins in category 'cheats': " + str(cheats) + "<br><br>\n## Plugin List 'Cheats':<br><br>")
fgameplay = open("gameplay.md", "w")
fgameplay.writelines(headercategory)
fgameplay.writelines(" Plugins in category 'gameplay': " + str(gameplay) + "<br><br>\n## Plugin List 'Gameplay':<br><br>")
fgraphics = open("graphics.md", "w")
fgraphics.writelines(headercategory)
fgraphics.writelines(" Plugins in category 'graphics': " + str(graphics) + "<br><br>\n## Plugin List 'Graphics':<br><br>")
foutfits = open("outfits.md", "w")
foutfits.writelines(headercategory)
foutfits.writelines(" Plugins in category 'outfits': " + str(outfits) + "<br><br>\n## Plugin List 'Outfits':<br><br>")
foverhauls = open("overhauls.md", "w")
foverhauls.writelines(headercategory)
foverhauls.writelines(" Plugins in category 'overhauls': " + str(overhauls) + "<br><br>\n## Plugin List 'Overhauls':<br><br>")
foverwrites = open("overwrites.md", "w")
foverwrites.writelines(headercategory)
foverwrites.writelines(" Plugins in category 'overwrites': " + str(overwrites) + "<br><br>\n## Plugin List 'Overwrites':<br><br>")
fpatches = open("patches.md", "w")
fpatches.writelines(headercategory)
fpatches.writelines(" Plugins in category 'patches': " + str(patches) + "<br><br>\n## Plugin List 'Patches':<br><br>")
fraces = open("races.md", "w")
fraces.writelines(headercategory)
fraces.writelines(" Plugins in category 'races': " + str(races) + "<br><br>\n## Plugin List 'Races':<br><br>")
fships = open("ships.md", "w")
fships.writelines(headercategory)
fships.writelines(" Plugins in category 'ships': " + str(ships) + "<br><br>\n## Plugin List 'Ships':<br><br>")
fstory = open("story.md", "w")
fstory.writelines(headercategory)
fstory.writelines(" Plugins in category 'story': " + str(story) + "<br><br>\n## Plugin List 'Story':<br><br>")
fweapons = open("weapons.md", "w")
fweapons.writelines(headercategory)
fweapons.writelines(" Plugins in category 'weapons': " + str(weapons) + "<br><br>\n## Plugin List 'Weapons':<br><br>")
funcategorized = open("uncategorized.md", "w")
funcategorized.writelines(headercategory)
funcategorized.writelines(" Plugins in category 'uncategorized': " + str(uncategorized) + "<br><br>\n## Plugin List 'Uncategorized':<br><br>")

# read folders, and write to .md
entries = os.listdir(pathtoplugins)
entries.sort(key=str.lower)
for entry in entries:
	withdots = entry.replace(" ", ".")
	forweb  = entry.replace(" ", "%20")

	# get description out of pluginlist file
	if os.path.exists(pluginlistfolder + entry + ".txt") == True:
		with open(pluginlistfolder + entry + ".txt" , "r") as file2:
			author = file2.readline().split("=")[1].replace("\n", "")
			website = file2.readline().split("=")[1].replace("\n", "")
			category = file2.readline().split("=")[1].replace("\n", "")
			status = file2.readline().split("=")[1].replace("\n", "")
			description= file2.readlines()
			rem = description[0]
			description[0] = rem.replace("description=", "")
	
	# get last modified date from the assetfiles
	#response = requests.head(assetfiles + withdots + ".zip", allow_redirects=True)
	#modif = response.headers['Last-Modified']
	#datetime_object = datetime.strptime(modif, '%a, %d %b %Y %H:%M:%S %Z')
	#modif = str(datetime_object.date())
	modif="na"

	# get file size of the assetfiles in kb or mb
	#assetsize = int(response.headers['Content-Length']) / 1024
	#form = " kb"
	#if assetsize > 1024:
	#	assetsize = assetsize / 1024
	#	form = " mb"
	# assetsize = str(round(assetsize, 2))
	assetsize = "na"
	form="na"
	
	# writing the plugin entries
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
