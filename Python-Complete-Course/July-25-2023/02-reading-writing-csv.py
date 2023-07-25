file = open("Python-Complete-Course\July-25-2023\csv_data.txt",'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f"{name} is {age}, studing {degree} in {university}")

# add value to csv file using JOIN

sample_csv_value = ','.join(['hello','123','world'])
print(sample_csv_value)