This is a small python script to download you favourite minecraft modpacks, and play it without any troubles of other downloader.

*NOTE: This tutorial is assuming that you already have installed python and forge version of the modpack you want*
*NOTE 2 : This program only works in Windows*

Instructions:

A) Downloading the modpack
    
   1) Clone this repo or download the zip and extract the content into a folder.

   2) Download the zip file of the modpack you want and then place it into the folder you created in step 1.

   3) Open cmd or powershell in adminstrator mode and change the directory to the working folder ie, the folder in step 1.

   4)  To download the modpack run the following command: `Python downloader.py <name of zip file of the modpack>`.

B) To add the modpack to the launcher

   1) Open the launcher and go to installations.![installations](https://imgur.com/IXt2C2x)
    
   2) create a new profile.![new_profile](https://imgur.com/8WHP7kB)
    
   3) Name the installation something youll understand.
    
   4) Select the version as the forge version you installed.![forge_version](https://imgur.com/kMF2yiQ)
    
   5) In the Game Directory field place the directory of the folder the script makes after you run the script.![directory](https://imgur.com/lmCCfv2)
    
   6) select more options and in jvm arguments in -Xmx, replace the number as the amount of ram indicated by the modpack maker for example  if the modpack recomends 6gb of ram replace it as -Xmx6G![ram](https://imgur.com/No20cnX)![ram1](https://imgur.com/XGiZuDp)
    
   7) click create and enjoy.
