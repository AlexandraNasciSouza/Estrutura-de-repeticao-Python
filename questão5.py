A = 80000
B = 200000
ano = 0

while A <= B:
    A += A * 0.03
    B += B * 0.015
    ano += 1

print("A ultrapassa ou se iguala com B em %d anos" %ano)