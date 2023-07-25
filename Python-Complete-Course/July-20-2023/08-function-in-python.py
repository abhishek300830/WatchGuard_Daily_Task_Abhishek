# Defining a basic function
def greet():
    name = input("Enter your name : ")
    print(f"Hello {name}")

greet()

# funtions with arguments

cars = [
    {"make":"ford","mileage":23000,"fuel_consumed":460},
    {"make":"Nishan","mileage":17000,"fuel_consumed":350}
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    print(f"{car['make']} does {mpg} miles per gallon.")

for car in cars:
    calculate_mpg(car)