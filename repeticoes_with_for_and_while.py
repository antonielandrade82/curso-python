#Repetições com for e while

#FOR ( Para repetir quando eu sei o quanto preciso repetir)
# for repetir in range(1, 6):
#     print(repetir)

#While ( Para repetir, quando eu não sei o quanto é necessário ou enquanto não tenho determinado resultado)
# variavel=1
# while variavel <= 5:
#     print(variavel)
#     variavel= variavel + 1

# senha=''
# while senha !='123':
#     senha = input('Qual é a senha do sistema? ')
# print('Acesso liberado!')

#Exercicio 1
# for contar in range (1,11):
#     print (contar)

# numero = int(input("Digite um número inteiro: "))
# soma = 0
# for i in range(1, numero + 1):
#     soma += i
# print("A soma de 1 até", numero, "é:", soma)


# numero = int(input("Digite um número: "))
# while numero >= 0:
#     print(numero)
#     numero -= 1
    
numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")