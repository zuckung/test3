import subprocess
import glob
import os

# check for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test2/src":
	os.chdir("../../") 

# deleting now useless zip files in root dir
listing = glob.glob('*.zip')
print("./*.zip : ")
print(listing)
for entry in listing:
	os.remove(entry)
	print(entry, " deleted ")
