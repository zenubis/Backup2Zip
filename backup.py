import datetime;
import zipfile;
import glob;
import os;
import io;
import hashlib;
import re;

savedata_path = "D:\\games\\steam\\userdata\\71325964\\582010\\remote";
backup_path = "C:\\Users\\yowfe\\Dropbox\\mhw_save";

def parseInt(string):
	try:
		return int(string);
	except Exception as e:
		print(e)
		return 0;


def GetLatestZipHash():
	#find latest file
	filelist = glob.glob(backup_path + os.sep + "*");
	latestfile = None;
	latestdate = 0;
	for myfile in filelist:
		result = re.search(r'mhw_(\d{8,8})\.zip$', myfile)
		if None == result:
			# skip all files not in our naming format
			continue;
		#print(myfile);
		mydate = parseInt(result.group(1));
		if latestfile == None:
			latestfile = myfile;
			latestdate = mydate;
		else:
			#compare date time
			if mydate > latestdate:
				latestdate = mydate;
				latestfile = myfile;

	
	if latestfile != None:
		#get hash			
		with open(latestfile, "rb") as fp:
			print("Found latest backup file as: " + latestfile);
			h = hashlib.sha256();
			h.update(fp.read());
			return h.hexdigest();
	print("Latest backup file not found.");
	return None;

# get sha256 of lastest backup zip
ziphash = GetLatestZipHash();

# temporary buffer for our new zip file
buf = io.BytesIO();

with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, False) as zf:
	filelist = glob.glob(savedata_path + os.sep + "*");
	for myfile in filelist:
		with open(myfile) as fp:
			zf.write(myfile);

#check hash with last latest file
if ziphash != None:
	bufhash = hashlib.sha256();
	buf.seek(0);
	bufhash.update(buf.read());
	if ziphash == bufhash.hexdigest():
		#same hash, no need write to disk
		print("Save has no changes, nothing to backup.")
		exit(0);

#write out buf to file
now=datetime.datetime.now();
filename=backup_path + os.sep + "mhw_{0:4d}{1:02d}{2:02d}.zip".format(now.year, now.month, now.day);
print("writing " + filename);
with open(filename, "wb") as fp:
	buf.seek(0);
	fp.write(buf.read());


	