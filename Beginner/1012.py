A,B,C = list(map(float,input().split()))

rectangledTriangle = (A * C) / 2
circle = (C ** 2) * 3.14159
trapezium = ((A + B) * C) / 2
squareArea = B ** 2
rectangleArea = A * B

print(f"TRIANGULO: {rectangledTriangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {squareArea:.3f}")
print(f"RETANGULO: {rectangleArea:.3f}")