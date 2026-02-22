#if - se ( true = executa if, false = executa o else)
#elif - inclui uma segunda condição ao if
#else - se não



# numero = int(input('Digite um número: '))
# if numero == 10:
#     print('Você acertou o número')
# else:
#     print('Você errou o número')


# idade=int(input('Qual é a sua idade?'))
# if idade >= 18:
#     print ('Você é maior de idade')
# else:
#     print ('Você é menor de idade')


# nota_aluno= float(input('Qual foi a sua nota no exame?'))
# if nota_aluno >= 7:
#     print ('Você foi aprovado')
# else:
#     print ('Você foi reprovado')


nota_aluno= float(input('Qual foi a sua nota no exame?'))
if nota_aluno >= 7:
    print ('Você foi aprovado')
elif nota_aluno >=5:
    print ('Você está de recuperação')
else:
    print ('Você foi reprovado')

