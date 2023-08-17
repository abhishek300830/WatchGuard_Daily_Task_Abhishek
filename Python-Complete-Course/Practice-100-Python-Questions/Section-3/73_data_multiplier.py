import csv

file_path = "Practice-100-Python-Questions\Section-3\csv_data_73.csv"

fields = []
x = []
y = []
with open(file_path, "r") as file:
    csv_data = csv.reader(file)
    fields = next(csv_data)
    for list1 in csv_data:
        x.append(list1[0])
        y.append(list1[1])

print(fields)
print(x)
print(y)

#  using pandas
import pandas

data = pandas.read_csv(file_path)
data_2 = data * 2
print(data_2)
data_2.to_csv("Practice-100-Python-Questions\Section-3\csv_data_generated_73.csv",index=None)
