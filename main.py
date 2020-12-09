import os
import os.path
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
from datetime import datetime

#get newest file
path = r'your path to clips'
filelist = [os.path.join(path, f) for f in os.listdir(path)]
filelist = [f for f in filelist if os.path.isfile(f)]
newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
print(newest)

#get the date and time plus the .mp4 extension
todaysDate = newest[-23:]

#gauth process
gauth = GoogleAuth() 
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 

#varible defining
title = "Newest Gaming Clip" + todaysDate
fid = "your auth code"
filename = newest[-60:]

#upload clip
file = drive.CreateFile({'title': title,
                         "parents": [{"kind": "drive#fileLink", "id": fid}]})
file.SetContentFile(path + "\\" + filename)
file.Upload()                         

