valor = float(input(" "))
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for value in notas:
    count = valor // value
    valor %= value
    print("{} nota(s) de R$ {}.00".format(int(count), value))
print("MOEDAS:")
for value in moedas:
    count = valor // value
    valor %= value
    print("{} moeda(s) de R$ {:.2f}".format(int(count), value))