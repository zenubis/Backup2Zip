# Backup2Zip
Simple script to backup a directory to a zip file.

## Instructions
Modify `savedata_path` and `backup_path` to the desired path with `savedata_path` being the path that you want to zip up and `backup_path` the path where you want to zip to.

To change the zipfile name, search for `mhw_` and replace all instance with whatever prefix you would like. The script uses the date time appended after the prefix to determine which file is the latest and use that to check if the new zip is different before committing the new data to disk.