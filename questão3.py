nome = input("Informe o nome: ")
while len(nome ) <= 3:
    nome = input ("Informe o nome: ")

idade = int(input("Informa a Idade: "))
while idade < 0 or idade > 150:
    idade = int(input ("Informe a idade correta: "))

salario = float(input("informe o salário: "))
while salario <= 0:
    salario = float(input("Salario inválido, informe um valor superior a 0: "))

sexo = input("Informe o sexo F ou M: ")
while (sexo != 'F') and (sexo !='M'):
    sexo = input("Escolha F ou M: ")

estadoCivil = input("Informe o estado civil: ")
while (estadoCivil !='s') and (estadoCivil !='c') and (estadoCivil !='v') and (estadoCivil !='d'):
     estadoCivil = input("Informe o estado civil: ")




