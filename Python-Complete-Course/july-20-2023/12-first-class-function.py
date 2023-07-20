def greet():
    print("Hello Abhishek")

hello = greet
hello()

# a good example of it is

avg = lambda sequence: sum(sequence) / len(sequence)
total = lambda sequence: sum(sequence)
top = lambda sequence: max(sequence)

operations={
    'average':avg,
    'total':total,
    'top':top
}

students = [
    {'name':'Abhishek','grades':(90,80,95,85)},
    {'name':'kunal','grades':(90,80,95,85)},
    {'name':'kush','grades':(90,80,95,85)}
]

for student in students:
    name = student['name']
    grade = student['grades']

    operation = input("Enter average, total or top : ")
    operation_function = operations[operation]

    print(operation_function(grade))

