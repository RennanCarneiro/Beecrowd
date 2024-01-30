import math

p1 = map(float,input().split(" "))
p2 = map(float,input().split(" "))
x1, y1 = p1
x2, y2 = p2
distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

print(round(distance, 4))