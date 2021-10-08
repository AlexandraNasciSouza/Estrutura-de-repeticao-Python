nome = input("Nome usuario : ")
senha = input("Senha: ")

while senha == nome:
		print("Erro: nome e senha não pode ser iguais, informe a senha novamente")
		senha = input("Senha: ")
else:
	    print("Dados corretos")