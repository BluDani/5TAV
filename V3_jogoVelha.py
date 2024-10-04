import random
from time import sleep
import pandas as pd # para salvar os resultados em um arquivo xlsx tem que executar o "pip install openpyxl" para o xlsx
import matplotlib.pyplot as plt # para exibir um grafico , executar o "pip install matplotlib"


# Função para exibir o tabuleiro com uma lista simples de 9 posições
def exibirTabuleiro(tabuleiro):
    exibir = []
    for valor in tabuleiro:
        if (valor == ""):
            exibir.append(" ")

        else:
            exibir.append(valor)

    print("\n")
    print(f"\t  {exibir[0]}  |  {exibir[1]}  |  {exibir[2]} ")
    print("\t-----------------")
    print(f"\t  {exibir[3]}  |  {exibir[4]}  |  {exibir[5]} ")
    print("\t-----------------")
    print(f"\t  {exibir[6]}  |  {exibir[7]}  |  {exibir[8]} ")


# Função para Limpar o tabuleiro
def limparTabuleiro(tabuleiro):
    for i in range(0, 9):
        tabuleiro[i] = ""


# Função para exibir o menu principal
def menu():
    print("\n")
    print("=" * 12, end="")
    print(" Modo de Jogo ", end="")
    print("=" * 12)
    print("1 - Contra o Computador Aleatório")
    print("2 - Contra outro Jogador")
    print("3 - Contra o Computador Profissional")
    print("4 - Simulação")
    print("=" * 38)


# Função para exibir o menu de simulações
def menuSimulacoes():
    print("\n")
    print("=" * 22, end="")
    print(" Simulações ", end="")
    print("=" * 22)
    print("1 - Computador Aleatório VS Computador Aleatório")
    print("2 - Computador Aleatório VS Computador Profissional")
    print("3 - Computador Profissional VS Computador Profissional")
    print("=" * 56)


# Função para a jogada de um jogador
def jogador(tabuleiro, jogada, player=1, simbolo="X"):
    while True:

        jogador_pos = int(input(f"\nJogador {player} faça sua jogada [1-9]: ")) - 1

        # Verifica se a jogada está dentro do intervalo permitido
        if (jogador_pos < 0 or jogador_pos > 8):
            print("\033[031mJogada inválida. Escolha uma posição de 1 a 9.\033[m")

        else:
            # Verifica se a posição escolhida já está preenchida
            if (tabuleiro[jogador_pos] == ""):

                tabuleiro[jogador_pos] = simbolo
                jogada.append(jogador_pos)
                return True
            else:

                print("\033[031mA posição já está preenchida. Escolha outra.\033[m")


# Função para a jogada do computador (bobo)
def maquina(tabuleiro, jogada, simbolo="O"):
    while True:

        maquina_pos = random.randint(0, 8)  # Gera um número entre 0 e 8

        # Verifica se a posição escolhida pela máquina está disponível
        if (tabuleiro[maquina_pos] == ""):
            tabuleiro[maquina_pos] = simbolo
            jogada.append(maquina_pos)
            return True


def possibilidades(tabuleiro, simbolo, oponente):

    # Primeira linha
    if(tabuleiro[0] == tabuleiro[1] == simbolo and tabuleiro[2] == ""):
        return 2
    elif(tabuleiro[0] == tabuleiro[2] == simbolo and tabuleiro[1] == ""):
        return 1
    elif(tabuleiro[1] == tabuleiro[2] == simbolo and tabuleiro[0] == ""):
        return 0

    # Segunda linha
    elif(tabuleiro[3] == tabuleiro[4] == simbolo and tabuleiro[5] == ""):
        return 5
    elif(tabuleiro[3] == tabuleiro[5] == simbolo and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[5] == simbolo and tabuleiro[3] == ""):
        return 3

    # Terceira linha
    elif(tabuleiro[6] == tabuleiro[7] == simbolo and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[6] == tabuleiro[8] == simbolo and tabuleiro[7] == ""):
        return 7
    elif(tabuleiro[7] == tabuleiro[8] == simbolo and tabuleiro[6] == ""):
        return 6

    # Primeira coluna
    elif(tabuleiro[0] == tabuleiro[3] == simbolo and tabuleiro[6] == ""):
        return 6
    elif(tabuleiro[0] == tabuleiro[6] == simbolo and tabuleiro[3] == ""):
        return 3
    elif(tabuleiro[3] == tabuleiro[6] == simbolo and tabuleiro[0] == ""):
        return 0

    # Segunda coluna
    elif(tabuleiro[1] == tabuleiro[4] == simbolo and tabuleiro[7] == ""):
        return 7
    elif(tabuleiro[1] == tabuleiro[7] == simbolo and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[7] == simbolo and tabuleiro[1] == ""):
        return 1

    # Terceira coluna
    elif(tabuleiro[2] == tabuleiro[5] == simbolo and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[2] == tabuleiro[8] == simbolo and tabuleiro[5] == ""):
        return 5
    elif(tabuleiro[5] == tabuleiro[8] == simbolo and tabuleiro[2] == ""):
        return 2

    # Primeira diagonal
    elif(tabuleiro[0] == tabuleiro[4] == simbolo and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[0] == tabuleiro[8] == simbolo and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[8] == simbolo and tabuleiro[0] == ""):
        return 0

    # Segunda diagonal
    elif(tabuleiro[2] == tabuleiro[4] == simbolo and tabuleiro[6] == ""):
        return 6
    elif(tabuleiro[2] == tabuleiro[6] == simbolo and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[6] == simbolo and tabuleiro[2] == ""):
        return 2


    #bloquear oponente

    # Primeira linha
    if(tabuleiro[0] == tabuleiro[1] == oponente and tabuleiro[2] == ""):
        return 2
    elif(tabuleiro[0] == tabuleiro[2] == oponente and tabuleiro[1] == ""):
        return 1
    elif(tabuleiro[1] == tabuleiro[2] == oponente and tabuleiro[0] == ""):
        return 0

    # Segunda linha
    elif(tabuleiro[3] == tabuleiro[4] == oponente and tabuleiro[5] == ""):
        return 5
    elif(tabuleiro[3] == tabuleiro[5] == oponente and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[5] == oponente and tabuleiro[3] == ""):
        return 3

    # Terceira linha
    elif(tabuleiro[6] == tabuleiro[7] == oponente and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[6] == tabuleiro[8] == oponente and tabuleiro[7] == ""):
        return 7
    elif(tabuleiro[7] == tabuleiro[8] == oponente and tabuleiro[6] == ""):
        return 6

    # Primeira coluna
    elif(tabuleiro[0] == tabuleiro[3] == oponente and tabuleiro[6] == ""):
        return 6
    elif(tabuleiro[0] == tabuleiro[6] == oponente and tabuleiro[3] == ""):
        return 3
    elif(tabuleiro[3] == tabuleiro[6] == oponente and tabuleiro[0] == ""):
        return 0

    # Segunda coluna
    elif(tabuleiro[1] == tabuleiro[4] == oponente and tabuleiro[7] == ""):
        return 7
    elif(tabuleiro[1] == tabuleiro[7] == oponente and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[7] == oponente and tabuleiro[1] == ""):
        return 1

    # Terceira coluna
    elif(tabuleiro[2] == tabuleiro[5] == oponente and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[2] == tabuleiro[8] == oponente and tabuleiro[5] == ""):
        return 5
    elif(tabuleiro[5] == tabuleiro[8] == oponente and tabuleiro[2] == ""):
        return 2

    # Primeira diagonal
    elif(tabuleiro[0] == tabuleiro[4] == oponente and tabuleiro[8] == ""):
        return 8
    elif(tabuleiro[0] == tabuleiro[8] == oponente and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[8] == oponente and tabuleiro[0] == ""):
        return 0

    # Segunda diagonal
    elif(tabuleiro[2] == tabuleiro[4] == oponente and tabuleiro[6] == ""):
        return 6
    elif(tabuleiro[2] == tabuleiro[6] == oponente and tabuleiro[4] == ""):
        return 4
    elif(tabuleiro[4] == tabuleiro[6] == oponente and tabuleiro[2] == ""):
        return 2

    else:

        return -1


def maquinaProf(tabuleiro, jogada, quemComeca, simbolo="X"):
    # Maquina profissional começa
    if (quemComeca == 2):

        # Primeira jogada
        if (len(jogada) == 0):
            tabuleiro[2] = simbolo
            jogada.append(2)

        # Jogador faz a jogada e é a vez da máquina
        # Terceira jogada
        if (len(jogada) == 2):

            if (jogada[1] == 0 or jogada[1] == 3):
                tabuleiro[8] = simbolo
                jogada.append(8)

            elif (jogada[1] == 1 or jogada[1] == 5):
                tabuleiro[4] = simbolo
                jogada.append(4)

            elif (jogada[1] == 6 or jogada[1] == 7 or jogada[1] == 8):
                tabuleiro[0] = simbolo
                jogada.append(0)

            elif (jogada[1] == 4):
                tabuleiro[7] = simbolo
                jogada.append(7)

        # Jogador faz a jogada e é a vez da máquina
        # Quarta jogada
        if (len(jogada) == 4):

            if (jogada[1] == 0):

                if (jogada[3] == 5):

                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[5] = simbolo
                    jogada.append(5)

            elif (jogada[1] == 1):

                if (jogada[3] == 6):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif (jogada[1] == 3):

                if (jogada[3] == 5):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[5] = simbolo
                    jogada.append(5)

            # Jogada do meio
            elif (jogada[1] == 4):

                if (jogada[3] == 0 or jogada[3] == 1):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif (jogada[3] == 3):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                elif (jogada[3] == 5):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                elif (jogada[3] == 6 or jogada[3] == 8):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif (jogada[1] == 5):

                if (jogada[3] == 6):
                    tabuleiro[1] = simbolo
                    jogada.append(1)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif (jogada[1] == 6):

                if (jogada[3] == 1):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

            elif (jogada[1] == 7):

                if (jogada[3] == 1):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

            elif (jogada[1] == 8):

                if (jogada[3] == 1):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

        # Sexta rodada
        if (len(jogada) == 6):

            if (jogada[1] == 0 and jogada[3] == 5):

                if (jogada[5] == 4):
                    tabuleiro[7] = simbolo
                    jogada.append(7)

                elif (jogada[5] == 7):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[4] = simbolo
                    jogada.append(4)

            elif (jogada[1] == 1 and jogada[3] == 6):

                if (jogada[5] == 3):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif (jogada[5] == 8):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[3] = simbolo
                    jogada.append(3)

            elif (jogada[1] == 3 and jogada[3] == 5):

                if (jogada[5] == 0):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                elif (jogada[5] == 6):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif (jogada[1] == 5 and jogada[3] == 6):

                if (jogada[5] == 0):
                    tabuleiro[7] = simbolo
                    jogada.append(7)

                elif (jogada[5] == 7):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif (jogada[1] == 6 and jogada[3] == 1):

                if (jogada[5] == 4):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                elif (jogada[5] == 5):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[4] = simbolo
                    jogada.append(4)

            elif (jogada[1] == 7 and jogada[3] == 1):

                if (jogada[5] == 6):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif (jogada[5] == 8):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif (jogada[1] == 8 and jogada[3] == 1):

                if (jogada[5] == 3):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                elif (jogada[5] == 4):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[3] = simbolo
                    jogada.append(3)

            # Jogada do meio
            elif (jogada[1] == 4):

                if (jogada[3] == 0 or jogada[3] == 1):

                    if (jogada[5] == 6):
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                    elif (jogada[5] == 5):
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                    else:
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                elif (jogada[3] == 3):

                    if (jogada[5] == 8):
                        tabuleiro[0] = simbolo
                        jogada.append(0)

                    else:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                elif (jogada[3] == 5):

                    if (jogada[5] == 0):
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                    elif (jogada[5] == 1):
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                    elif (jogada[5] == 6 or jogada[5] == 8):
                        tabuleiro[0] = simbolo
                        jogada.append(0)

                elif (jogada[3] == 6 or jogada[3] == 8):

                    if (jogada[5] == 1):
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                    else:
                        tabuleiro[1] = simbolo
                        jogada.append(1)

        # Oitava rodada
        if (len(jogada) == 8):

            if (jogada[3] == 3):

                if (jogada[5] == 8):

                    if (jogada[7] == 1):

                        tabuleiro[6] = simbolo
                        jogada.append(6)

                    else:
                        tabuleiro[1] = simbolo
                        jogada.append(1)

            elif (jogada[3] == 5):

                if (jogada[5] == 0):

                    if (jogada[7] == 6):

                        tabuleiro[1] = simbolo
                        jogada.append(1)

                    else:
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                elif (jogada[5] == 1):

                    if(jogada[7] == 0):

                        tabuleiro[8] = simbolo
                        jogada.append(8)

                    else:
                        tabuleiro[0] = simbolo
                        jogada.append(0)
                        

                elif (jogada[5] == 6 or jogada[5] == 8):

                    if (jogada[7] == 1):
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                    else:
                        tabuleiro[1] = simbolo
                        jogada.append(1)

            elif (jogada[3] == 6 or jogada[3] == 8):

                if (jogada[5] == 1):

                    if (jogada[7] == 8):
                        tabuleiro[3] = simbolo
                        jogada.append(3)

                    else:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

    else:

        # Segunda jogada
        if len(jogada) == 1:
            # Se a primeira jogada do oponente não for no centro, ocupar o centro
            if jogada[0] != 4:
                tabuleiro[4] = simbolo
                jogada.append(4)
            else:
                # Caso contrário, ocupar um canto
                tabuleiro[2] = simbolo
                jogada.append(2)

        # Quarta jogada
        elif len(jogada) == 3:
            # Verificar se há uma jogada para vencer ou bloquear
            posicao = possibilidades(tabuleiro, simbolo, "X")

            if posicao == -1:
                # Caso não haja, jogar baseado na posição do oponente
                if jogada[0] == 4:
                    if jogada[2] == 6:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                elif jogada[0] == 0:
                    if jogada[2] == 5 or jogada[2] == 8:
                        tabuleiro[7] = simbolo
                        jogada.append(7)
                    elif jogada[2] == 7:
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                elif jogada[0] == 1:
                    if jogada[2] == 3 or jogada[2] == 6 or jogada[2] == 7:
                        tabuleiro[0] = simbolo
                        jogada.append(0)
                    elif jogada[2] == 5 or jogada[2] == 8:
                        tabuleiro[2] = simbolo
                        jogada.append(2)

                elif jogada[0] == 2:
                    if jogada[2] == 3 or jogada[2] == 6:
                        tabuleiro[1] = simbolo
                        jogada.append(1)
                    elif jogada[2] == 7:
                        tabuleiro[3] = simbolo
                        jogada.append(3)

                elif jogada[0] == 3:
                    if jogada[2] == 1 or jogada[2] == 2 or jogada[2] == 5:
                        tabuleiro[0] = simbolo
                        jogada.append(0)
                    elif jogada[2] == 7 or jogada[2] == 8:
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                elif jogada[0] == 5:
                    if jogada[2] == 0 or jogada[2] == 1 or jogada[2] == 3:
                        tabuleiro[2] = simbolo
                        jogada.append(2)
                    elif jogada[2] == 6 or jogada[2] == 7:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                elif jogada[0] == 6:
                    if jogada[2] == 2 or jogada[2] == 5:
                        tabuleiro[1] = simbolo
                        jogada.append(1)
                    elif jogada[2] == 1:
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                elif jogada[0] == 7:
                    if jogada[2] == 0 or jogada[2] == 1 or jogada[2] == 3:
                        tabuleiro[6] = simbolo
                        jogada.append(6)
                    elif jogada[2] == 2 or jogada[2] == 5:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                elif jogada[0] == 8:
                    if jogada[2] == 0 or jogada[2] == 3:
                        tabuleiro[1] = simbolo
                        jogada.append(1)
                    elif jogada[2] == 1:
                        tabuleiro[3] = simbolo
                        jogada.append(3)

            else:
                tabuleiro[posicao] = simbolo
                jogada.append(posicao)

        # Sexta jogada
        elif len(jogada) == 5:
            # Verificar se há uma jogada para vencer ou bloquear
            posicao = possibilidades(tabuleiro, simbolo, "X")

            if posicao != -1:
                tabuleiro[posicao] = simbolo
                jogada.append(posicao)
            else:
                # Se não houver posição de vitória ou bloqueio, jogar em uma posição estratégica
                for i in [0, 2, 6, 8]:
                    if tabuleiro[i] == "":
                        tabuleiro[i] = simbolo
                        jogada.append(i)
                        break

        # Oitava jogada
        elif len(jogada) == 7:
            # Verificar se há uma jogada para vencer ou bloquear
            posicao = possibilidades(tabuleiro, simbolo, "X")

            if posicao != -1:
                tabuleiro[posicao] = simbolo
                jogada.append(posicao)
            else:
                # Caso contrário, ocupar a última posição disponível
                for i in range(9):
                    if tabuleiro[i] == "":
                        tabuleiro[i] = simbolo
                        jogada.append(i)
                        break


def mostrar_grafico_linhas(vitorias_jogador1, vitorias_jogador2, velhas, num_partidas):
    partidas = list(range(1, num_partidas + 1))

    plt.plot(partidas, vitorias_jogador1, label='Jogador 1', color='blue', marker='o')
    plt.plot(partidas, vitorias_jogador2, label='Jogador 2', color='red', marker='o')
    plt.plot(partidas, velhas, label='Velhas', color='gray', marker='o')

    plt.xlabel('Número de Partidas')
    plt.ylabel('Número de Vitórias/velhas')
    plt.title('Evolução das Vitórias')
    plt.legend()
    plt.grid(True)
    plt.show()


def verificaGanhador(tabuleiro):
    # Verificando se o jogador X ganhou (linhas, colunas e diagonais)
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "X" or  # Linha 1
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "X" or  # Linha 2
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "X" or  # Linha 3
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "X" or  # Coluna 1
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "X" or  # Coluna 2
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "X" or  # Coluna 3
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "X" or  # Diagonal principal
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "X"):  # Diagonal secundária

        return 1  # Jogador X ganhou

    # Verificando se o jogador O ganhou (linhas, colunas e diagonais)
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "O" or  # Linha 1
            tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "O" or  # Linha 2
            tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "O" or  # Linha 3
            tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "O" or  # Coluna 1
            tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "O" or  # Coluna 2
            tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "O" or  # Coluna 3
            tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "O" or  # Diagonal principal
            tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "O"):  # Diagonal secundária

        return 2  # Jogador O ganhou

    # Caso ninguém tenha ganhado
    return 0


# Variáveis
tabuleiro = ["", "", "", "", "", "", "", "", ""]  # Tabuleiro linear
jogada = []  # Todas as jogadas feitas

ganhador = 0
quantPartidas = 0  # quantidade de partidas que o simulador vai rodar
quantRodadas = 0  # quantidade de rodadas do simulador
resultados = [0, 0, 0]  # 1° jogador / 2° jogador 2 ou maquina boba / 3° maquina profissional
salvar = ""

dados = {
    "modoJogo": ""
}

# Loop para saber se o jogador quer continuar
while True:

    menu()

    modoJogo = int(input("\nEscolha o modo de jogo: "))

    if (modoJogo != 4):

        quemComeca = 1 #random.randint(1, 2)  # Randomizar quem começa

        # Jogador 2 começando
        if (quemComeca == 2 and modoJogo == 2):

            exibirTabuleiro(tabuleiro)

            # O jogador 2 só sai do looping se fizer uma jogada válida
            while True:

                jogador2 = jogador(tabuleiro, jogada, 2, "O")

                if (jogador2):
                    break

        # Máquina boba começando
        if (quemComeca == 2 and modoJogo == 1):

            exibirTabuleiro(tabuleiro)

            # Vez do computador
            print("\nJogada do computador ", end="")

            # Só fazendo uma graça pra deixar bonitinho
            for c in range(0, 3):
                sleep(1)
                print(".", end="", flush=True)

            # A máquina só sai do looping se fizer uma jogada válida
            while True:

                computador = maquina(tabuleiro, jogada)

                if (computador):
                    break

        if (quemComeca == 2 and modoJogo == 3):

            exibirTabuleiro(tabuleiro)

            # Vez do computador
            print("\nJogada do computador ", end="")

            # Só fazendo uma graça pra deixar bonitinho
            for c in range(0, 3):
                sleep(1)
                print(".", end="", flush=True)

            maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")

    else:
        menuSimulacoes()

        modoSimulacao = int(input("\nEscolha a simulação: "))

        if (modoSimulacao == 2):
            quemComeca = int(input("\nQuem deve começar?\n1= Computador Aleatório\n2= Computador Profissional\n"))

        salvar = str(input('\nQuer Salvar os dados em um arquivo excel e mostrar o grafico na tela [S/N]: ')).strip().upper()[0]

        quantPartidas = int(input("Quer simular quantas partidas: "))

    # loop do jogo
    if (modoJogo != 4):
        while True:
            exibirTabuleiro(tabuleiro)

            # Jogador 1 faz a jogada (sempre ocorre, exceto em simulações automáticas)
            if (ganhador == 0 and len(jogada) < 9 and modoJogo != 4):

                while True:

                    jogador1 = jogador(tabuleiro, jogada)  # Jogador 1 com símbolo 'X'

                    if (jogador1):
                        break

                ganhador = verificaGanhador(tabuleiro)
                exibirTabuleiro(tabuleiro)

            # Modo de jogo 3: Contra o Computador Profissional
            if (modoJogo == 3 and ganhador == 0 and len(jogada) < 9):

                # Vez do computador
                print("\nJogada do computador ", end="")

                # Só fazendo uma graça pra deixar bonitinho
                for c in range(0, 3):
                    sleep(1)
                    print(".", end="", flush=True)

                maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")
                exibirTabuleiro(tabuleiro)
                ganhador = verificaGanhador(tabuleiro)

            # Modo de jogo 2: Contra outro jogador
            if (modoJogo == 2 and ganhador == 0 and len(jogada) < 9):

                while True:

                    jogador2 = jogador(tabuleiro, jogada, player=2, simbolo="O")  # Jogador 2 com símbolo 'O'

                    if (jogador2):
                        break

                ganhador = verificaGanhador(tabuleiro)

            # Modo de jogo 1: Contra o computador bobo
            if (modoJogo == 1 and ganhador == 0 and len(jogada) < 9):

                print("\nJogada do computador ", end="")

                # Só fazendo uma graça pra deixar bonitinho
                for c in range(0, 3):
                    sleep(1)
                    print(".", end="", flush=True)

                while True:

                    computador = maquina(tabuleiro, jogada)

                    if (computador):
                        break

                ganhador = verificaGanhador(tabuleiro)

            print("\nJogadas até agora:", jogada)

            # Condições de fim de jogo: Vitória ou empate

            if (len(jogada) > 8 or ganhador != 0):

                exibirTabuleiro(tabuleiro)

                if (ganhador == 1):
                    print("\nO jogador 1 venceu!")

                elif (modoJogo == 1 and ganhador == 2):
                    print("\nO computador Aleatorio venceu!")

                elif (modoJogo == 2 and ganhador == 2):
                    print("\nO jogador 2 venceu!")

                elif (modoJogo == 3 and ganhador == 2):
                    print("\nO computador Profissional venceu!")

                else:
                    print("\nEmpate!")

                break


    else:

        # Listas para gráficos
        vitorias_jogador1 = []
        vitorias_jogador2 = []
        velhas = []

        if (modoSimulacao == 1):

            while quantRodadas < quantPartidas:

                if (ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Aleatório 1:", end=" ")
                    while True:

                        computador1 = maquina(tabuleiro, jogada, simbolo="X")

                        if (computador1):
                            break

                    print(jogada[-1])  # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)

                if (ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Aleatório 2:", end=" ")
                    while True:

                        computador2 = maquina(tabuleiro, jogada)

                        if (computador2):
                            break

                    print(jogada[-1])  # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)

                if (len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if (ganhador == 1):
                        resultados[0] += 1

                    elif (ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")
            print("Computador Aleatório 1 ganhou", resultados[0], "vez(es)")
            print("Computador Aleatório 2 ganhou", resultados[1], "vez(es)")
            print("Deu Velha", resultados[2], "vez(es)")

        elif (modoSimulacao == 2):

            while quantRodadas < quantPartidas:

                if (quemComeca == 1):

                    if (ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Aleatório:", end=" ")
                        while True:

                            computador1 = maquina(tabuleiro, jogada, simbolo="X")

                            if (computador1):
                                break

                        print(jogada[-1])  # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                    if (ganhador == 0 and len(jogada) < 9):
                        print("\nJogada do computador Profissional:", end=" ")

                        computador2 = maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")

                        print(jogada[-1])  # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                else:

                    if (ganhador == 0 and len(jogada) < 9):
                        print("\nJogada do computador Profissional:", end=" ")

                        computador2 = maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")

                        print(jogada[-1])  # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                    if (ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Aleatório:", end=" ")
                        while True:

                            computador1 = maquina(tabuleiro, jogada, simbolo="X")

                            if (computador1):
                                break

                        print(jogada[-1])  # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                if (len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if (ganhador == 1):
                        resultados[0] += 1

                    elif (ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")

            if (quemComeca == 1):
                print("Computador Aleatório jogando primeiro")
                print("\nComputador Aleatório ganhou", resultados[0], "vez(es)")
                print("Computador Profissional ganhou", resultados[1], "vez(es)")
                print("Deu Velha", resultados[2], "vez(es)")

            else:
                print("Computador Profissional jogando primeiro")
                print("\nComputador Aleatório ganhou", resultados[0], "vez(es)")
                print("Computador Profissional ganhou", resultados[1], "vez(es)")
                print("Deu Velha", resultados[2], "vez(es)")


        else:

            while quantRodadas < quantPartidas:

                if (ganhador == 0 and len(jogada) < 9):
                    print("\nJogada do computador Profissional 1:", end=" ")

                    computador1 = maquinaProf(tabuleiro, jogada, quemComeca=2, simbolo="X")

                    print(jogada[-1])  # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)

                if (ganhador == 0 and len(jogada) < 9):
                    print("\nJogada do computador Profissional 2:", end=" ")

                    computador2 = maquinaProf(tabuleiro, jogada, quemComeca=1, simbolo="O")

                    print(jogada[-1])  # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)

                if (len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if (ganhador == 1):
                        resultados[0] += 1

                    elif (ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")
            print("Computador Profissional 1 ganhou", resultados[0], "vez(es)")
            print("Computador Profissional 2 ganhou", resultados[1], "vez(es)")
            print("Deu Velha", resultados[2], "vez(es)")


    if(salvar == "S"):
        
        dadosArquivos = []
        vitorias_jogador1.append(resultados[0])
        vitorias_jogador2.append(resultados[1])
        velhas.append(resultados[2])

        # Lista para armazenar os dados que serão salvos

        # Definir o nome do arquivo com base nos bots
        if(modoSimulacao == 1):
            arquivo_excel = 'resultado_aleatorio_VS_aleatorio.xlsx'
            jogador1 = 'Computador Aleatório 1'
            jogador2 = 'Computador Aleatório 2'

        elif(modoSimulacao == 2 and quemComeca == 1):
            arquivo_excel = 'resultado_aleatorio_Comecando_VS_Profissional.xlsx'
            jogador1 = 'Computador Aleatório'
            jogador2 = 'Jogador Profissional'

        elif(modoSimulacao == 2 and quemComeca == 2):
            arquivo_excel = 'resultado_Profissional_Comecando_VS_aleatorio.xlsx'
            jogador1 = 'Jogador Profissional'
            jogador2 = 'Computador Aleatório'

        elif(modoSimulacao == 3):
            arquivo_excel = 'resultado_Profissional_VS_Profissional.xlsx'
            jogador1 = 'Jogador Profissional 1'
            jogador2 = 'Jogador Profissional 2'

        # Adicionar os resultados no formato desejado
        dadosArquivos.append({
            'Jogador 1': jogador1,
            'Vitorias Jogador 1': resultados[0],
            'Jogador 2': jogador2,
            'Vitorias Jogador 2': resultados[1],
            'Velhas': resultados[2]
        })

        # Criar o DataFrame com colunas nomeadas
        df_dadosArquivos = pd.DataFrame(dadosArquivos, columns=[
            'Jogador 1', 'Vitorias Jogador 1', 'Jogador 2', 'Vitorias Jogador 2', 'Velhas'
        ])

        # Salvar o DataFrame no arquivo Excel
        df_dadosArquivos.to_excel(arquivo_excel, index=False)

        #mostrar_grafico_linhas(vitorias_jogador1, vitorias_jogador2, velhas, quantPartidas)


    continuar = str(input('\nQuer jogar novamente [S/N]: ')).strip().upper()[0]

    limparTabuleiro(tabuleiro)
    jogada.clear()  # Limpa a lista de jogadas
    ganhador = 0
    quantRodadas = 0
    resultados.clear()
    resultados = [0]*3

    if (continuar == "N"):
        break
