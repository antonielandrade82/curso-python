#MINHA SOLUÇÃO
quantidade_produto = int(input('Insira aqui a quantidade de produto disponível: '))
porcoes_utilizadas = int(input('Insira aqui a quantidade de porções que você irá utilizar: '))

#sem uso de variável
# print(f'O produto irá durar {quantidade_produto//porcoes_utilizadas} dias')

dias = quantidade_produto/porcoes_utilizadas
#solução mais "elegante"
print (f'O produto vai durar {dias:.0f} dias!')


