notes = int(input())
print(notes)

values = [100, 50, 20, 10, 5, 2, 1]

for value in values:
    count = notes // value
    notes %= value
    print("{} nota(s) de R$ {},00".format(count, value))
    
