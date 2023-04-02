## Jokempo game in Python, the user can play against the computer or againt other player, yhe code is in a while loop, so the user can play as many times as he wants.

from random import randint
from time import sleep

## Definindo a lista de opções
options = ['pedra', 'papel', 'tesoura']

## Função para decidir o vencedor
def DecideWinner(UserChoice, ComputerChoice):
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
        else:
            print ('VOCE VENCEU!!!')
    elif UserChoice == options[1]:
        if ComputerChoice == options[2]:
            print ('Computador venceu')
        else:
            print ('VOCE VENCEU!!!')
    elif UserChoice == options[2]:
        if ComputerChoice == options[0]:
            print ('Computador venceu')
        else:
            print ('VOCE VENCEU!!!')
    else:
        print ('Opcao invalida')

## Função para jogar novamente
def PlayAgain():
    print('Deseja jogar novamente? (s/n)')
    return input().lower().startswith('s')

## Função para jogar contra o computador
def PlayComputer():
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice = input('Voce: ')
    ComputerChoice = options[randint(0,2)]
    DecideWinner(UserChoice, ComputerChoice)

## Função para jogar contra outro jogador
def PlayPlayer():
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice = input('Jogador 1: ')
    print('Escolha entre pedra, papel ou tesoura')
    UserChoice2 = input('Jogador 2: ')
    DecideWinner(UserChoice, UserChoice2)

## Loop principal
while True:
    print('-•' * 10)
    print('Bem vindo ao Jokempo')
    print('-•' * 10)
    print('Escolha uma opção:')
    print('1 - Jogar contra o computador')
    print('2 - Jogar contra outro jogador')
    print('3 - Sair')
    option = int(input())
    if option == 1:
        PlayComputer()
    elif option == 2:
        PlayPlayer()
    elif option == 3:
        break
    else:
        print('Opcao invalida')
    if not PlayAgain():
        break

print('Obrigado por jogar')






