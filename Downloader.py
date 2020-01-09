import json
import os
import urllib3
import re
from urllib.request import urlretrieve

http = urllib3.PoolManager()

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

    # looping throught the Mod ID's and their file ID's
    for ID in data['files']:

        # Getting the ID's into a variable
        projectID = ID['projectID']
        fileID = ID['fileID']

        # Getting the File url using a resolving api
        file_url = 'https://addons-ecs.forgesvc.net/api/v2/addon/' + \
            str(projectID)+'/file/'+str(fileID)+'/download-url'

        r = http.request('GET', file_url)
        # converting the data from the recived data and convert that into a url
        urls = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(r.data).replace(" ","%20"))
        file_name = os.path.basename(urls[0].replace("'", ''))

        if not os.path.exists(file_name.replace("%20"," ")):

            # opening the link provided by the resolver
            source = http.request('GET', urls[0].replace("'", ''))

            #printing the file which is downloading     
            print("Downloading: %s " % (file_name))

            #downloading the file and saving it as jar
            urlretrieve(urls[0].replace("'", ''),file_name.replace("%20"," "))
        else: 
            print("File Already Exists, so skipping")
            continue