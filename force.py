import random as ran
import math

inside = 0

total = 10000000
for i in range(0, total):
    # Generate random x, y in [0, 1].
    x2 = ran.random()**2
    y2 = ran.random()**2
    
    if math.sqrt(x2 + y2) < 1.0:
        inside = inside + 1
pi = (float(inside) / total) * 4

print(pi)