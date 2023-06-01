import glob
import os

if os.getcwd() == "/storage/emulated/0/Download/mgit/test3/res/src": # check for local testing
	os.chdir("../../")

listing = glob.glob('*.zip')
print(listing)
for entry in listing:
	os.remove(entry)
