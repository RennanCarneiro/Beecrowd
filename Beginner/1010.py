product1 = input().split(" ")
product2 = input().split(" ")

code1, units1, price1 = product1
code2, units2, price2, = product2

amount = (int(units1) * float(price1)) + (int(units2) * float(price2))

print(f"VALOR A PAGAR: R$ {amount:.2f}")