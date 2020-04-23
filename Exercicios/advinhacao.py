print('*******************************')
print('Bem vindo no jogo de Advinhacao')
print('*******************************')

numero_secreto = 42
chute = input('Digite o seu numero: ')

if (numero_secreto == chute):
    print('voce acertou')
else:
    print('Voce errou')