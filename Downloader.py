import shutil
import json
import os
import urllib3
import re
from tqdm import tqdm
from urllib.request import urlretrieve
from urllib.parse import quote
from zipfile import ZipFile


http = urllib3.PoolManager()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Extracting the zip to another file with the modpack name
file_name = str([files for files in os.listdir(os.getcwd())
                 if files.endswith('.zip')]).strip("['").strip("']")
with ZipFile(os.getcwd() + "\\" + file_name, 'r') as zip:
    file_name = file_name.strip(".zip")
    try:
        os.mkdir(os.getcwd() + "\\" + file_name)
    except:
        print("Folder already exists so skipping.....")
    os.chdir(os.getcwd() + "\\" + file_name)
    zip.extractall()


with open('manifest.json') as json_file:
    # Getting data from the json file
    data = json.load(json_file)
# getting the Minecraft version and modpack name
minecraft_version = data['minecraft']['version']
modpack_name = data['name']
modLoader_name_all = str(data['minecraft']['modLoaders']).strip(
    "[{").strip("}]").rsplit(',')
modLoader_name_all = modLoader_name_all[0].rsplit(':')
modloader_name = modLoader_name_all[1].replace("'", "")
# Making Directories and Changing the current working directories
try:
    os.mkdir('mods')
except:
    print('Folder already exists so skipping')
os.chdir('mods')
# looping throught the Mod ID's and their file ID's
for ID in tqdm(data['files'], desc="Downloading:", unit='files', ascii=True):
    # Getting the ID's into a variable
    projectID = ID['projectID']
    fileID = ID['fileID']

    # Getting the File url using a resolving api
    file_url = 'https://addons-ecs.forgesvc.net/api/v2/addon/' + \
        str(projectID)+'/file/'+str(fileID)+'/download-url'

    r = http.request('GET', file_url)
    # converting the data from the recived data and convert that into a url
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(r.data).replace(" ", "%20"))
    file_name = os.path.basename(urls[0].strip("'")).replace("%20", " ")
    if not os.path.exists(file_name):

        urls[0] = urls[0].strip("'")
        # opening the link provided by the resolver
        source = http.request('GET', urls[0].replace("'", '%27'))

        # downloading the file and saving it as jar
        urlretrieve(urls[0].replace("'", '%27'),
                    file_name)
    else:
        continue


# Copying the files inside the overrides folder into the general folder
os.chdir('../')
for folders in os.listdir(os.getcwd() + '\\' + "overrides"):
    print(folders)
    shutil.copytree(os.getcwd() + '\\' + "overrides" +
                    '\\' + str(folders), os.getcwd()+'\\' + str(folders), dirs_exist_ok=True)

shutil.rmtree(os.getcwd() + '\\' + "overrides")


print("Downloading Finished")