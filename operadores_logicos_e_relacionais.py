# num1 = 10
# num2 = 2

#EXEMPLOS DE OPERADORES RELACIONAIS
# print(num1==num2) #igual
# print(num1!=num2) #diferente
# print(num1>num2) #maior que
# print(num1<num2) #menor que
# print(num1>=num2) #maior ou igual que
# print(num1<=num2) #menor ou igual que

#OPERADORES LOGICOS
#AND
#OR
#NOT

# Para dirigir a pessoa tem que ser maior de 18 anos de idade e ter CNH
# idade = int(input('Qual é a sua idade? '))
# cnh = True
# verificador = idade >=18 and cnh
# print(verificador)


usuario = input('Digite o seu usuário: ')
senha = input ('Digite a sua senha: ')
login_valido = usuario == 'Admin' and senha == '12345'
print(f'Login Permitido: {login_valido}')