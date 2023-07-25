cars = [
    {"make":"ford","mileage":23000,"fuel_consumed":460},
    {"make":"Nishan","mileage":17000,"fuel_consumed":350}
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg

def print_car(car,mpg):
    print(f"{car['make']} does {mpg} miles per gallon.")


for car in cars:
    mpg = calculate_mpg(car)
    print_car(car,mpg)

# more than 1 return statement in function

def divide(numerator,denominator):
    if denominator == 0:
        return "you tried to divide by zero."
    else:
        return numerator // denominator

print(divide(100,10))
