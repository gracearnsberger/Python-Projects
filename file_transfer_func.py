#Grace Arnsberger
#File Transfer Practice Using Python
import shutil
import time
import os

#set time 
SECONDS_IN_DAY = 24 * 60 * 60

#set the source where all .txt files are
source = '/Users/grace/OneDrive/Desktop/Documents/'

#set the destination to the Destination folder where all .txt docs that were modified in the last 24 hours goes to
destination = '/Users/grace/OneDrive/Desktop/Destination/'

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(filename):
    return os.path.getmtime(filename)

for filename in os.listdir(source):
    source_filename = os.path.join(source, filename)
    if last_mod_time(source_filename) > before:
        destination_filename = os.path.join(destination, filename)
        shutil.move(source_filename, destination_filename)


if __name__ == "__main__":
    pass

