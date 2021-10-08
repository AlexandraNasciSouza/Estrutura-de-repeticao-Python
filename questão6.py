A = int(input("Informe a população de A: "))
while A < 0:
   A = int(input("Informe a população de A: ")) 
taxaA = float(input("Informa a taxa de A: "))    

B = int(input("Informe a população de B: "))
while B < 0:
    B = int(input("Informe a população de B: "))
taxaB = float(input("Informa a taxade B: "))   


ano = 0

while A <= B:
    A += A * taxaA
    B += B * taxaB
    ano += 1

print("A ultrapassa ou se iguala com B em %d anos" %ano)