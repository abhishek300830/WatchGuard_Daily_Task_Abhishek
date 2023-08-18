# detect screen height and width of the screen.
from screeninfo import get_monitors

height = get_monitors()[0].height
width = get_monitors()[0].width

print(f"height : {height} width : {width}")

# We're using the get_monitors  method of the screeninfo  library which can be installed with pip install screeninfo . The get_monitors  method produces a list like [monitor(1920x1080+0+0), monitor(1280x1024+-1280+-31)]  listing all the monitors connected to the computer. Applying [0]  to that list gives the first monitor object out of the list. Applying width  to that monitor, the object gives the width of the monitor, and the same goes for the height  property.