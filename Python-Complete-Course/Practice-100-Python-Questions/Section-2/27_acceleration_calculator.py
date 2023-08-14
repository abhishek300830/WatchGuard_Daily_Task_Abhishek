# Create a function that calculates acceleration given initial velocity v1, 
# final velocity v2, start time t1, and end time t2. The formula for acceleration is:

def calculate_acceleration(v1,v2,t1,t2):
    v = v2 - v1
    t = t2 - t1
    a = v / t
    print(a)

calculate_acceleration(0,10,0,20)