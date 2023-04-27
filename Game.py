from random import randint
from time import sleep

jogador = 0
jogador2 = 0

## Definindo a lista de opções
options = ['pedra', 'papel', 'tesoura']

## Função para decidir o vencedor
def DecideWinner(UserChoice, ComputerChoice):
    global jogador, jogador2  # make variables accessible from function
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print ('-' * 20)
    print ('Voce escolheu', UserChoice)
    print ('O outro jogador escolheu', ComputerChoice)
    print ('-' * 20)

    if UserChoice == ComputerChoice:
        print ('EMPATE')
    elif UserChoice == options[0]:
        if ComputerChoice == options[1]:
            print ('Computador venceu')
            jogador2 += 1
        else:
            print ('VOCE VENCEU!!!')
            jogador += 1
    elif UserChoice == options[1]:
        if ComputerChoice == options[2]:
            print ('Computador venceu')
            jogador2 +=  1
        else:
            print ('VOCE VENCEU!!!')
            jogador += 1
    elif UserChoice == options[2]:
        if ComputerChoice == options[0]:
            print ('Computador venceu')
            jogador2 += 1
        else:
            print ('VOCE VENCEU!!!')
            jogador += 1
    else:
        print ('Opcao invalida')

## Função para jogar novamente
def PlayAgain():
    print('Deseja jogar novamente? (s/n)')
    return input().lower().startswith('s')

## Função para jogar contra o computador
def PlayComputer():
    global jogador, jogador2  # make variables accessible from function
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice = input('Voce: ') 
    ComputerChoice = options[randint(0,2)]
    DecideWinner(UserChoice, ComputerChoice)

## Função para jogar contra outro jogador
def PlayPlayer():
    global jogador, jogador2  # make variables accessible from function
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice = input('Jogador 1: ')
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice2 = input('Jogador 2: ')
    DecideWinner(UserChoice, UserChoice2)

def ComputerComputer():
    global jogador, jogador2  # make variables accessible from function
    print('Escolha entre pedra, papel ou tesoura')
    ComputerChoice1 = options[randint(0,2)]
    print('Escolha entre pedra, papel ou tesoura')
    ComputerChoice2 = options[randint(0,2)]
    DecideWinner(ComputerChoice1, ComputerChoice2)

## Loop principal
while True:
    print('-•' * 10)
    print('Bem vindo ao Jokempo')
    print('-•' * 10)
    print('1 - Jogar contra o computador')
    print('2 - Jogar contra outro jogador')
    print('3 - Computador contra o computador')
    print('4 - imprimir placar')
    print('5 - Sair')
    option = int(input('Escolha uma opção:'))
    if option == 1:
        PlayComputer()
    elif option == 2:
        PlayPlayer()
    elif option == 3:
        ComputerComputer()
    elif option == 4:
        print('Jogador 1: ', jogador)
        print('Jogador 2: ', jogador2)
    elif option == 5:
        break
    else:
        print('Opcao invalida')
    if not PlayAgain():
        break

print('Obrigado por jogar')
print('Jogador 1: ', jogador)
print('Jogador 2: ', jogador2)






