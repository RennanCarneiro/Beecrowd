n= int(input())
years = n / 365
restoYears = n % 365
restoMes = restoYears % 30
months = restoYears / 30
days = restoMes % 30

print(f"{int(years)} ano(s)\n{int(months)} mes(es)\n{int(days)} dia(s)")