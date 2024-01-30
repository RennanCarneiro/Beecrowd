import math

a, b, c = map(float, input().split())
delta = (b**2) - (4*a*c)

if delta < 0 or a==0:
    print("Impossivel calcular")
else:
    deltaSqr = math.sqrt(delta)
    root1 = (-b + deltaSqr)/(2*a)
    root2 = (-b - deltaSqr)/(2*a)
    print(f"R1 = {root1:.5f}\nR2 = {root2:.5f}")