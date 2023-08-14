# The following code is supposed to print out the square root of 9, but it throws an error instead because another line before that is missing. Please fix the script so that it prints out the square root of 9.

import math

print(math.sqrt(9) )


# Since you get the error that math is not defined, that means math is not in the default namespace. With some internet research, you could easily find out that math is a module, so you simply need to do import math  .