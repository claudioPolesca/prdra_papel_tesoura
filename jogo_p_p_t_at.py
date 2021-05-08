from time import sleep
from random import choice
sorteio = ['pedra', 'papel', 'tesoura']
bot = choice(sorteio)
cores = {"limpar": '\033[m', "vermelho": '\033[31m',
         "verde": '\033[32m', "amarelo": '\033[33m', "roxo": '\033[34m', "rosa": '\033[35m', "azul": '\033[36m',
         }


def corte():
    print(f'{cores["limpar"]}-=-'*10)


def Pedra(j, b):
    if f'{j}' == 'pedra' and f'{b}' == 'tesoura':
        vitoria_jogador()
    if f'{b}' == 'pedra' and f'{j}' == 'tesoura':
        vitoria_bot()


def Papel(j, b):
    if f'{j}' == 'papel' and f'{b}' == 'pedra':
        vitoria_jogador()
    if f'{b}' == 'papel' and f'{j}' == 'pedra':
        vitoria_bot()


def Tesoura(j, b):
    if f'{j}' == 'tesoura' and f'{b}' == 'papel':
        vitoria_jogador()
    if f'{b}' == 'tesoura' and f'{j}' == 'papel':
        vitoria_bot()


def vitoria_jogador():
    print(f'{cores["azul"]}{nome_jogador} escolheu {jogador}. VENCEU!\n'
          f'bot escolheu {bot}. PERDEU!{cores["limpar"]}')


def vitoria_bot():
    print(f'{cores["vermelho"]}bot escolheu {bot}. VENCEU!\n'
          f'{nome_jogador} escolheu {jogador}. PERDEU!{cores["limpar"]}')


print('=====JOKENPÔ====')
nome_jogador = input(
    f'{cores["amarelo"]}Digite o nome do jogador: ').capitalize()
print(
    f'Bem vindo ao jogo {nome_jogador}!\n Digite [fim] para parar de jogar.{cores["limpar"]}')
corte()
while True:

    jogador = input(f'{cores["verde"]}{nome_jogador} Escolha uma opção: \n'
                    f'Pedra\n'
                    f'Papel\n'
                    f'Tesoura\n').lower()
    sleep(1)
    print(f'{cores["roxo"]}JO')
    sleep(1)
    print(f'KEN')
    sleep(1)
    print(f'PÔ{cores["limpar"]}')
    sleep(1)
    corte()
    if jogador == bot:
        print(f'{cores["amarelo"]}Empate!{cores["limpar"]}')
    Pedra(jogador, bot)
    Papel(jogador, bot)
    Tesoura(jogador, bot)

    if jogador == 'fim':
        break
    if jogador not in sorteio:
        print(
            f'{cores["vermelho"]}Favor tentar somente opções validas.{cores["limpar"]}')
    corte()
