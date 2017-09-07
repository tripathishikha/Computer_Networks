import urllib2
import sys
from urlparse import urlparse
from os.path import splitext, basename
import time 
import math
import shutil
from shutil import copyfile
import os

URL_LIST=sys.argv[1]
count=1
duration=dict()
record_url=dict()
record_size=dict()
original_folder="downloaded_files"
time_list=[]
# code to get the current working directory 
cwd = os.getcwd()
new_path=cwd+'/'


with open(URL_LIST) as f:
	for line in f:
		URL=line
		disassembled = urlparse(line)
		filename, file_ext = splitext(basename(disassembled.path))
		with open(filename,'wb') as f:
			start=time.time()
 			f.write(urllib2.urlopen(URL).read())
			elapsed = time.time() - start
			elapsed=elapsed*1000
			#print("image number",count,"with time",elapsed)
			duration[elapsed]=filename
			record_url[filename]=line
			#record_size[filename]=getsize(filename)
			time_list.append(elapsed)
			count=count+1
    			f.close()
#before sorting 

#for i in duration:
#		print i,duration[i]
#after sorting
# sorting the list of duration
time_list.sort(reverse=False)


# creating the folder for fast and slow downloaded images


# Path to be created
path_slow = "SlowDownloaded"
path_fast="FastDownloaded"
length=len(time_list)



if not os.path.exists(new_path+path_fast):
	os.mkdir(path_fast)
else:
	shutil.rmtree(new_path+path_fast, ignore_errors=True, onerror=None)
	os.mkdir(path_fast)
if not os.path.exists(new_path+path_slow):
	os.mkdir(path_slow)
else:
	shutil.rmtree(new_path+path_slow, ignore_errors=True, onerror=None)
	os.mkdir(path_slow)

flag=True

print "Fast Downloaded Files\n"
print "URL,Size(bytes),Download time(ms)\n"


for i in range(length):
	
	if i<(length/2):
		file_num=time_list[i]
		file_name=duration[file_num]
		if not os.path.exists(new_path+path_fast+'/'+file_name):
			print record_url[file_name]+",\t"+"\t",os.path.getsize(file_name),",\t"+"\t",file_num,"\n"
			shutil.move(new_path+file_name,new_path+path_fast)
			
		else:
			print record_url[file_name]+",\t"+"\t",os.path.getsize(file_name),",\t"+"\t",file_num,"\n"
			os.remove(new_path+path_fast+'/'+file_name) 
			shutil.move(new_path+file_name,new_path+path_fast)
			
		
	else:	
		if flag==True:
			print "---------------------------------------------"
			print "Slow Downloaded Files\n"
			print "URL,Size(bytes),Download time(ms)\n"
			flag=False
		file_num=time_list[i]
		file_name=duration[file_num]
		
		if not os.path.exists(new_path+path_slow+'/'+file_name):
			print record_url[file_name]+",\t"+",\t",os.path.getsize(file_name),",\t"+"\t",file_num,"\n"
			shutil.move(new_path+file_name,new_path+path_slow)
			
			
		else:
			print record_url[file_name]+",\t"+",\t",os.path.getsize(file_name),",\t"+"\t",file_num,"\n"
			os.remove(new_path+path_slow+'/'+file_name) 
			shutil.move(new_path+file_name,new_path+path_slow)	
			

print "Complete!"
