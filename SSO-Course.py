import datetime
import os
import time
import shutil

# To name the folder and time | DEBUG
#print(datetime.datetime.today())

# Making date-wise folder
today = datetime.datetime.now

# Replace F:\2-2 with the path where in you had like to allocate the SS date-wise
New_Folder = r"F:\2-2\{}" .format(today().strftime('%I %p %d %b')) 

if not os.path.exists(New_Folder):
    os.makedirs(New_Folder)

#To sort the files based on time of past x hour(s)
x = 1
SECONDS_IN_X_HOUR = x * 60 * 60

src = r"C:\Users\Swastik\Pictures\Screenshots" #Replace src with files folder
dst = New_Folder

now = time.time()
before = now - SECONDS_IN_X_HOUR

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)