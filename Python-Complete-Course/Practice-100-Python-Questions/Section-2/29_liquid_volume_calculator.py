#   Please write a function that calculates liquid volume in a sphere
#  using the following formula. The radius r  is always 10, 
# so consider making it a default parameter.
import math
PI =math.pi

def volume(h, r=10):
    first_part = (4 * PI * pow(r,3))/3
    last_part = (PI * pow(h,2)*(3*r - h))/3
    result = first_part - last_part
    print(result)

volume(2)