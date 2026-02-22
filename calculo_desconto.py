preco = int(input ('Digite o valor do produto: ')) #valor em R&
desconto = int(input('Digite o valor do descoto a ser aplicado: ')) #desconto em %


novo_preco = preco - preco * desconto / 100
print(f' O valor com desconto é de R$ {novo_preco}')