import json
import os
import re
import faster_than_requests as requests

file_url = []

with open('manifest.json') as json_file:
    # Getting data from the json file
    data = json.load(json_file)

# getting the Minecraft version and modpack name
minecraft_version = data['minecraft']['version']
modpack_name = data['name']

# Making Directories and Changing the current working directories
try:
    os.mkdir(modpack_name + ' ' + minecraft_version)
except:
    print('Directory already exists so skipping')
os.chdir(modpack_name + ' ' + minecraft_version)
try:
    os.mkdir('mods')
except:
    print('Directory already exists so skipping')
os.chdir('mods')
for ID in data['files']:
    file_url.append('https://addons-ecs.forgesvc.net/api/v2/addon/%s/file/%s/download-url'%(str(ID['projectID']),str(ID['fileID'])))

file_url = requests.get2str2(file_url)


for url in file_url:
    url = str(re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url.replace(" ","%20")))
#print(file_url)

for urls in file_url:
    if not os.path.exists(os.path.basename(urls)):
        requests.download2([(urls,os.path.basename(urls))])
        print("downloading:",os.path.basename(urls))
    else: 
        print("File Exists So skipping...\n")
print("Downloading Finished")