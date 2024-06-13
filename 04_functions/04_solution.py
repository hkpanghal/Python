# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def calculate(raduis):
    area = math.pi * raduis * raduis
    circ = 2 * math .pi * raduis 

    return area,circ

print(calculate(5))