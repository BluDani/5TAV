import random
from time import sleep

#Área das Funções
def exibirTabuleiro(tabuleiro):

    print("\n")
    print(f"\t  {tabuleiro[0][0]}  |  {tabuleiro[0][1]}  |  {tabuleiro[0][2]} ")
    print("\t--------------")
    print(f"\t  {tabuleiro[1][0]}  |  {tabuleiro[1][1]}  |  {tabuleiro[1][2]} ")
    print("\t--------------")
    print(f"\t  {tabuleiro[2][0]}  |  {tabuleiro[2][1]}  |  {tabuleiro[2][2]} ")


def menu():

    print("=" *7, end="")
    print("Modo de Jogo", end="")
    print("=" *7)

    print("1 - Contra o Computador Bobo")
    print("2 - Contra outro Jogador")
    print("3 - Contra o Computador Profissional")
    print("4 - Simulação")

    print("=" *26)

def simulacoes():
    print("=" *7, end="")
    print("Simulações", end="")
    print("=" *7)

    print("1 - Computador Bobo VS Computador Bobo")
    print("2 - Computador Bobo VS Computador Profissional")
    print("3 - Computador Profissional VS Computador Profissional")

    print("=" *26)


def jogador(tabuleiro, jogada, player = 1, simbolo = "X"):

    jogador = int(input(f"\nJogador {player} faça sua jogada [1-9]: ")) -1

    #Verifica qual posição o jogador escolheu
    if(jogador < 0 or jogador > 9):

        print("\033[031mJogada inválida\033[m")

    elif(jogador < 3):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[0][jogador] == ""):

            tabuleiro[0][jogador] = simbolo
            jogada.append(jogador)
            return True

        else:
            print("\033[031mA posição já está preenchida\033[m")

    elif(jogador < 6):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[1][jogador -3] == ""):

            tabuleiro[1][jogador -3] = simbolo
            jogada.append(jogador)
            return True

        else:
            print("\033[031mA posição já está preenchida\033[m")

    elif(jogador < 9):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[2][jogador -6] == ""):

            tabuleiro[2][jogador -6] = simbolo
            jogada.append(jogador)
            return True

        else:
            print("\033[031mA posição já está preenchida\033[m")

    #Caso a jogada seja inválida, retorna false
    return False


def maquina(tabuleiro, jogada):

    maquina = random.randint(0, 9)

    #Verifica qual posição a maquina escolheu

    if(maquina < 3):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[0][maquina] == ""):

            tabuleiro[0][maquina] = "O"
            jogada.append(maquina)
            return True

    elif(maquina < 6):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[1][maquina -3] == ""):

            tabuleiro[1][maquina -3] = "O"
            jogada.append(maquina)
            return True

    elif(maquina < 9):

        #verifica se a posição escolhida já está preenchida
        if(tabuleiro[2][maquina -6] == ""):

            tabuleiro[2][maquina -6] = "O"
            jogada.append(maquina)
            return True

    #Caso a jogada seja inválida, retorna false
    return False

def maquinaProf(tabuleiro, jogada, quemComeca, simbolo = "X"):

    #maquina profissional começa
    if(quemComeca == 1):

        #primeira jogada
        if(len(jogada) == 0):
            tabuleiro[0][2] = simbolo
            jogada.append(2)
        
        #jogador vai fazer a jogada dele e vai ser a vez da maquina
        #terceira jogada
        
        if(len(jogada) == 2):
            if(jogada[1] == 0 or jogada[1] == 3):
                tabuleiro[2][2] = simbolo
                jogada.append(8)

            elif(jogada[1] == 1 or jogada[1] == 5):
                tabuleiro[1][1] = simbolo
                jogada.append(4)

            elif(jogada[1] == 6 or jogada[1] == 7 or jogada[1] == 8):
                tabuleiro[0][0] = simbolo
                jogada.append(0)

            elif(jogada[1] == 4):
                tabuleiro[2][1] = simbolo
                jogada.append(7)

        #jogador vai fazer a jogada dele e vai ser a vez da maquina
        #quarta jogada
        if(len(jogada) == 4):
            if(jogada[1] == 0):

                if(jogada[3] == 5):
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[1][2] = simbolo
                    jogada.append(5)
            
            elif(jogada[1] == 1):

                if(jogada[3] == 6):
                    tabuleiro[1][2] = simbolo
                    jogada.append(5)

                else:
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 3):

                if(jogada[3] == 5):

                    tabuleiro[1][1] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[1][2] = simbolo
                    jogada.append(5)

            #jogada do meio
            elif(jogada[1] == 4):

                if(jogada[3] == 0 or jogada[3] == 1):
                    tabuleiro[2][2] = simbolo
                    jogada.append(8)

                elif(jogada[3] == 3):
                    tabuleiro[1][2] = simbolo
                    jogada.append(5)

                elif(jogada[3] == 5):
                    tabuleiro[1][0] = simbolo
                    jogada.append(3)

                elif(jogada[3] == 6 or jogada[3] == 8):
                    tabuleiro[0][0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 5):

                if(jogada[3] == 6):
                    tabuleiro[0][1] = simbolo
                    jogada.append(1)

                else:
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 6 ):

                if(jogada[3] == 1):
                    tabuleiro[2][2] = simbolo
                    jogada.append(8)

                else:
                    tabuleiro[0][1] = simbolo
                    jogada.append(1)

            elif(jogada[1] == 7):

                if(jogada[3] == 1):
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[0][1] = simbolo
                    jogada.append(1)

            elif(jogada[1] == 8):

                if(jogada[3] == 1):
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[0][1] = simbolo
                    jogada.append(1)

        #sexta Rodada
        if(len(jogada) == 6):
            if(jogada[1] == 0 and jogada[3] == 5):

                if(jogada[5] == 4):
                    tabuleiro[2][1] = simbolo
                    jogada.append(7)
                
                elif(jogada[5] == 7):
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)
            
            elif(jogada[1] == 1 and jogada[3] == 6):
                
                if(jogada[5] == 3):
                    tabuleiro[2][2] = simbolo
                    jogada.append(8)
                
                elif(jogada[5] == 8):
                    tabuleiro[1][0] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[1][0] = simbolo
                    jogada.append(3)

            elif(jogada[1] == 3 and jogada[3] == 5):
                
                if(jogada[5] == 0):
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)
                
                elif(jogada[5] == 6):
                    tabuleiro[0][0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0][0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 5 and jogada[3] == 6):
                
                if(jogada[5] == 0):
                    tabuleiro[2][1] = simbolo
                    jogada.append(7)
                
                elif(jogada[5] == 7):
                    tabuleiro[0][0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0][0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 6 and jogada[3] == 1):
                
                if(jogada[5] == 4):
                    tabuleiro[1][2] = simbolo
                    jogada.append(5)
                
                elif(jogada[5] == 5):
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)

            elif(jogada[1] == 7 and jogada[3] == 1):
                
                if(jogada[5] == 6):
                    tabuleiro[2][2] = simbolo
                    jogada.append(8)
                
                elif(jogada[5] == 8):
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[2][0] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 8 and jogada[3] == 1):
                
                if(jogada[5] == 3):
                    tabuleiro[1][1] = simbolo
                    jogada.append(4)
                
                elif(jogada[5] == 4):
                    tabuleiro[1][0] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[1][0] = simbolo
                    jogada.append(3)

            #jogada do meio
            elif(jogada[1] == 4):

                if(jogada[3] == 0 or jogada[3] == 1):
                    
                    if(jogada[5] == 6):
                        tabuleiro[1][2] = simbolo
                        jogada.append(5)

                    elif(jogada[5] == 5):
                        tabuleiro[2][0] = simbolo
                        jogada.append(6)

                    else:
                        tabuleiro[2][0] = simbolo
                        jogada.append(6)

                elif(jogada[3] == 3):
                    
                    if(jogada[5] == 8):
                        tabuleiro[0][0] = simbolo
                        jogada.append(0)

                    else:
                        tabuleiro[2][2] = simbolo
                        jogada.append(8)

                elif(jogada[3] == 5):
                    
                    if(jogada[5] == 0):
                        tabuleiro[2][2] = simbolo
                        jogada.append(8)

                    elif(jogada[5] == 1):
                        tabuleiro[2][0] = simbolo
                        jogada.append(6)

                    elif(jogada[5] == 6 or jogada[5] == 8):
                        tabuleiro[0][0] = simbolo
                        jogada.append(0)

                elif(jogada[3] == 6 or jogada[3] == 8):
                    
                    if(jogada[5] == 1):
                        tabuleiro[1][2] = simbolo
                        jogada.append(5)

                    else:
                        tabuleiro[0][1] = simbolo
                        jogada.append(1)
        
        #oitava Rodada
        if(len(jogada) == 8):

            if(jogada[3] == 3):
                
                if(jogada[5] == 8):
                    
                    if(jogada[7] == 1):
                        tabuleiro[2][0] = simbolo
                        jogada.append(6)

                    else:
                        tabuleiro[0][1] = simbolo
                        jogada.append(1)

            elif(jogada[3] == 5):
                
                if(jogada[5] == 0):

                    if(jogada[7] == 6):
                        tabuleiro[0][1] = simbolo
                        jogada.append(1)
                    
                    else:
                        tabuleiro[2][0] = simbolo
                        jogada.append(6)

                elif(jogada[5] == 1):

                    if(jogada[7] == 0):
                        tabuleiro[2][2] = simbolo
                        jogada.append(8)

                    else:
                        tabuleiro[0][0] = simbolo
                        jogada.append(0)

                elif(jogada[5] == 6 or jogada[5] == 8):

                    if(jogada[7] == 1):
                        tabuleiro[2][2] = simbolo
                        jogada.append(8)

                    else:
                        tabuleiro[0][1] = simbolo
                        jogada.append(1)

            elif(jogada[3] == 6 or jogada[3] == 8):
                
                if(jogada[5] == 1):
                    
                    if(jogada[7] == 8):
                        tabuleiro[1][0] = simbolo
                        jogada.append(3)

                    else:
                        tabuleiro[2][2] = simbolo
                        jogada.append(8)


        
    

    
    


def verificaGanhador(tabuleiro):

    #verificando se o X ganhou, na ordem está linhas, colunas, trasversal
    if(tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "X" or 
       tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "X" or
       tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "X" or
       tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "X" or
       tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "X" or
       tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "X" or
       tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X" or
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X" 
       ):
        
        return 1
    

    if(tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == "O" or 
       tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == "O" or
       tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == "O" or
       tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == "O" or
       tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == "O" or
       tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == "O" or
       tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O" or
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O" 
       ):
        
        return 2
    
    return 0


#Variáveis
tabuleiro = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

jogada = []
ganhador = 0
quemComeca = 0


menu()

modoJogo = int(input("\nEscolha o modo de jogo: "))

#quemComeca = random.randint(1, 2)

#Jogador 2 começando
if(quemComeca == 2 and modoJogo == 2):

    exibirTabuleiro(tabuleiro)

    #O jogador2 só sai do looping se fizer uma jogada válida
    while True:
        jogador2 = jogador(tabuleiro, jogada, 2, "O")

        if(jogador2):
            break

#Maquina boba começando
if(quemComeca == 2 and modoJogo == 1):

    exibirTabuleiro(tabuleiro)

    #vez do computador
    print("\nJogada do computador ", end="")
    
    #só fazendo uma graça pra deixar bonitinho
    for c in range(0, 3):

        sleep(1)
        print(".", end="", flush=True)

    #A maquina só sai do looping se fizer uma jogada válida
    while True:
        computador= maquina(tabuleiro, jogada)

        if(computador):
            break


while True:

    exibirTabuleiro(tabuleiro)

    if(modoJogo == 3 and ganhador == 0 and len(jogada) < 9):
        maquinaProf(tabuleiro, jogada, quemComeca=1, simbolo="O")
        exibirTabuleiro(tabuleiro)
    
    #Verifica se o jogada não chegou no limite
    if(ganhador == 0 and len(jogada) < 9):

        #O jogador1 só sai do looping se fizer uma jogada válida
        while True:
            jogador1 = jogador(tabuleiro, jogada)

            if(jogador1):
                break
        
        #Exibe o tabuleiro depois da jogada do jogador1
        #Verifica se alguém ganhou
        ganhador = verificaGanhador(tabuleiro)
        exibirTabuleiro(tabuleiro)


    #Verifica se o modo de jogo é contra outro jogador e se o jogada não chegou no limite
    if(modoJogo == 2 and ganhador == 0 and len(jogada) < 9):

        #O jogador2 só sai do looping se fizer uma jogada válida
        while True:
            jogador2 = jogador(tabuleiro, jogada, 2, "O")

            if(jogador2):
                break
        
        #Verifica se alguém ganhou
        ganhador = verificaGanhador(tabuleiro)

    #Verifica se o modo de jogo é contra o computador Bobo e se o jogada não chegou no limite
    if(modoJogo == 1 and ganhador == 0 and len(jogada) < 9):

        #vez do computador
        print("\nJogada do computador ", end="")
        
        #só fazendo uma graça pra deixar bonitinho
        for c in range(0, 3):

            sleep(1)
            print(".", end="", flush=True)

        #A maquina só sai do looping se fizer uma jogada válida
        while True:
            computador= maquina(tabuleiro, jogada)

            if(computador):
                break

        #Verifica se alguém ganhou
        ganhador = verificaGanhador(tabuleiro)
    
    print("\n")
    print(jogada)

    if(len(jogada) > 8 or ganhador != 0):

        exibirTabuleiro(tabuleiro)

        if(ganhador == 1):
            print("\nO jogador 1 venceu")

        elif(modoJogo == 1 and ganhador == 2):
            print("\nO computador venceu")

        elif(modoJogo == 2 and ganhador == 2):
            print("\nO jogador 2 venceu")

        else:
            print("\nEmpate")

        break
