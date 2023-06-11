import os

# check for local testing
if os.getcwd() == "/storage/emulated/0/Download/mgit/test3/res/src":
	os.chdir("../../")
news = ""

with open("res/news.txt", "r") as file1: # reading and formating lines
	newslist = file1.readlines()
for i in range(20):
	if i <= len(newslist)-1:
		news = news + newslist[i] + "\n"

print(news)

with open("res/template.txt", "r") as file1:
	template = file1.read()
with open("test.md", "w") as file1:
	template = template.replace("%news%", news)
	file1.write(template)