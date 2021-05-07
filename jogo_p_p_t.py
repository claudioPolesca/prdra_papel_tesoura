from time import sleep
from random import choice
sorteio = ['pedra', 'papel', 'tesoura']
bot = choice(sorteio)
cores = {"limpar": '\033[m', "vermelho": '\033[31m',
         "verde": '\033[32m', "amarelo": '\033[33m', "roxo": '\033[34m', "rosa": '\033[35m', "azul": '\033[36m',
         }


def corte():
    print(f'{cores["limpar"]}-=-'*10)


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
    elif jogador == 'tesoura' and bot == 'papel':
        vitoria_jogador()
    elif jogador == 'papel' and bot == 'pedra':
        vitoria_jogador()
    elif jogador == 'pedra' and bot == 'tesoura':
        vitoria_jogador()
    elif bot == 'tesoura' and jogador == 'papel':
        vitoria_bot()
    elif bot == 'papel' and jogador == 'pedra':
        vitoria_bot()
    elif bot == 'pedra' and jogador == 'tesoura':
        vitoria_bot()
    if jogador == 'fim':
        break
    if jogador not in sorteio:
        print(
            f'{cores["vermelho"]}Favor tentar somente opções validas.{cores["limpar"]}')
    corte()
