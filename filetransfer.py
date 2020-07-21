#Grace Arnsberger
#File Transfer Practice Using Python
import shutil
import os

#set where the source of the files are
source = '/Users/grace/OneDrive/Desktop/FolderA/'

#set the destination path to Folder B
destination = '/Users/grace/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    #we are saying to move the files represented by "i" to their new destination
     shutil.move(source+i, destination)    
