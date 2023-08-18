import glob

folder_path = "Practice-100-Python-Questions\Section-4"

files = glob.glob1(folder_path,"*.py")

print(len(files))

# We're using glob  which is a standard Python library that finds pathnames matching a specified pattern. From glob  we're using glob1  which takes a directory name as the first argument and a pattern which in our case is *.py  which returns all the files starting with whatever and ending with .py in the files  directory.