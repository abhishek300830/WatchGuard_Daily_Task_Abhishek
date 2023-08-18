# Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

url_file_path = r'Practice-100-Python-Questions\Section-4\urls_94.txt'


with open(url_file_path,'r') as file:
    file_lines = file.readlines()
    file_lines = [line.strip('\n') for line in file_lines]

    for line in file_lines:
        print(line[:4]+line[5:7]+line[6:])