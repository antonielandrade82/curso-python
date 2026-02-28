# from funcoes import saudacao, soma

# saudacao("André")
# print(soma(4, 5))



from funcoes import verificar_maioridade

minha_idade = int(input("Digite sua idade: "))
if verificar_maioridade(minha_idade) == "Você é maior de idade.":
    print("Parabéns! Você tem acesso a conteúdos para maiores de 18 anos.")
else:
    print("Desculpe, você não tem acesso a conteúdos para maiores de 18 anos.")

    