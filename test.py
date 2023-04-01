import math

for i in range(0,360,45):
    x = math.radians(i)
    print(i,":",round(float(math.cos(x)),2), round(float(math.sin(x)),2))
    