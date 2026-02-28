#FUNÇÕES ( são um bloco de construção onde você escreve uma vez e utiliza várias vezes)

# def saudacao(nome, idade):
#     print(f'Olá {nome}! Você tem {idade} anos de idade.')

# saudacao('André', 30)  # Chamando a função para exibir a saudação com o nome 'André' e idade 30
# saudacao('Maria', 25)  # Chamando a função para exibir a saudação com o nome 'Maria' e idade 25

# def somar(num1, num2):
#     return num1 + num2

# total = somar(4, 5)  # Chamando a função para somar os números 4 e 5, o resultado será 9
# print(f'O resultado da soma é: {total}')

def calcular_desconto(preco, desconto):
   return preco - (preco * desconto / 100)
valor_final = calcular_desconto(100, 20)  # Chamando a função para calcular o preço final com um desconto de 20% sobre o preço original de 100
print(f'O valor final com desconto é de R$ : {valor_final:.2f}')  # Exibindo o valor final formatado com duas casas decimais

