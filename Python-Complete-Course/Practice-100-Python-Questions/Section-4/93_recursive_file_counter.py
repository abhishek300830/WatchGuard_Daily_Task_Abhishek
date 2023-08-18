# Please download the attached ZIP file. Inside the ZIP file, there's a directory named subdirs. That directory contains other directories inside. Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.z

import glob
 
file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))