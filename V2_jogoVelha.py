import random
from time import sleep

# Função para exibir o tabuleiro com uma lista simples de 9 posições
def exibirTabuleiro(tabuleiro):

    exibir = []
    for valor in tabuleiro:
        if(valor == ""):
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
    print("=" * 21, end="")
    print(" Simulações ", end="")
    print("=" * 21)
    print("1 - Computador Aleatório VS Computador Aleatório")
    print("2 - Computador Aleatório VS Computador Profissional")
    print("3 - Computador Profissional VS Computador Profissional")
    print("=" * 54)

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
def maquina(tabuleiro, jogada, simbolo = "O"):

    while True:

        maquina_pos = random.randint(0, 8)  # Gera um número entre 0 e 8

        # Verifica se a posição escolhida pela máquina está disponível
        if (tabuleiro[maquina_pos] == ""):

            tabuleiro[maquina_pos] = simbolo
            jogada.append(maquina_pos)
            return True

# Função para verificar se há uma vitória no tabuleiro
def verificar_vitoria(tabuleiro, simbolo):

    vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
                (0, 4, 8), (2, 4, 6)]             # Diagonais
    
    return any(tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo for a, b, c in vitorias)

# Função para encontrar a melhor jogada (ganhar ou bloquear o adversário)
def melhor_jogada(tabuleiro, simbolo, oponente):

    for i in range(9):

        if(tabuleiro[i] == ""):  # Verifica as posições vazias

            # Testar a vitória do computador
            tabuleiro[i] = simbolo

            if(verificar_vitoria(tabuleiro, simbolo)):
                return i
            
            # Testar o bloqueio da vitória do adversário
            tabuleiro[i] = oponente
            if(verificar_vitoria(tabuleiro, oponente)):
                return i
            
            tabuleiro[i] = ""  # Reseta a posição
    return None

def maquinaProf(tabuleiro, jogada, quemComeca, simbolo="X"):

    # Maquina profissional começa
    if(quemComeca == 2):

        # Primeira jogada
        if(len(jogada) == 0):

            tabuleiro[2] = simbolo
            jogada.append(2)

        # Jogador faz a jogada e é a vez da máquina
        # Terceira jogada
        if(len(jogada) == 2):

            if(jogada[1] == 0 or jogada[1] == 3):
                tabuleiro[8] = simbolo
                jogada.append(8)

            elif(jogada[1] == 1 or jogada[1] == 5):
                tabuleiro[4] = simbolo
                jogada.append(4)

            elif(jogada[1] == 6 or jogada[1] == 7 or jogada[1] == 8):
                tabuleiro[0] = simbolo
                jogada.append(0)

            elif(jogada[1] == 4):
                tabuleiro[7] = simbolo
                jogada.append(7)

        # Jogador faz a jogada e é a vez da máquina
        # Quarta jogada
        if(len(jogada) == 4):

            if(jogada[1] == 0):
                if(jogada[3] == 5):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[5] = simbolo
                    jogada.append(5)
            
            elif(jogada[1] == 1):

                if(jogada[3] == 6):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 3):

                if(jogada[3] == 5):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[5] = simbolo
                    jogada.append(5)

            # Jogada do meio
            elif(jogada[1] == 4):

                if(jogada[3] == 0 or jogada[3] == 1):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif(jogada[3] == 3):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                elif(jogada[3] == 5):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                elif(jogada[3] == 6 or jogada[3] == 8):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 5):

                if(jogada[3] == 6):
                    tabuleiro[1] = simbolo
                    jogada.append(1)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 6):

                if(jogada[3] == 1):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

            elif(jogada[1] == 7):

                if(jogada[3] == 1):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

            elif(jogada[1] == 8):

                if(jogada[3] == 1):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[1] = simbolo
                    jogada.append(1)

        # Sexta rodada
        if(len(jogada) == 6):

            if(jogada[1] == 0 and jogada[3] == 5):

                if(jogada[5] == 4):
                    tabuleiro[7] = simbolo
                    jogada.append(7)

                elif(jogada[5] == 7):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[4] = simbolo
                    jogada.append(4)
            
            elif(jogada[1] == 1 and jogada[3] == 6):

                if(jogada[5] == 3):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif(jogada[5] == 8):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[3] = simbolo
                    jogada.append(3)

            elif(jogada[1] == 3 and jogada[3] == 5):

                if(jogada[5] == 0):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                elif(jogada[5] == 6):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 5 and jogada[3] == 6):

                if(jogada[5] == 0):
                    tabuleiro[7] = simbolo
                    jogada.append(7)

                elif(jogada[5] == 7):
                    tabuleiro[0] = simbolo
                    jogada.append(0)

                else:
                    tabuleiro[0] = simbolo
                    jogada.append(0)

            elif(jogada[1] == 6 and jogada[3] == 1):

                if(jogada[5] == 4):
                    tabuleiro[5] = simbolo
                    jogada.append(5)

                elif(jogada[5] == 5):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                else:
                    tabuleiro[4] = simbolo
                    jogada.append(4)

            elif(jogada[1] == 7 and jogada[3] == 1):

                if(jogada[5] == 6):
                    tabuleiro[8] = simbolo
                    jogada.append(8)

                elif(jogada[5] == 8):
                    tabuleiro[6] = simbolo
                    jogada.append(6)

                else:
                    tabuleiro[6] = simbolo
                    jogada.append(6)

            elif(jogada[1] == 8 and jogada[3] == 1):

                if(jogada[5] == 3):
                    tabuleiro[4] = simbolo
                    jogada.append(4)

                elif(jogada[5] == 4):
                    tabuleiro[3] = simbolo
                    jogada.append(3)

                else:
                    tabuleiro[3] = simbolo
                    jogada.append(3)

            # Jogada do meio
            elif(jogada[1] == 4):

                if(jogada[3] == 0 or jogada[3] == 1):

                    if(jogada[5] == 6):
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                    elif(jogada[5] == 5):
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                    else:
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                elif(jogada[3] == 3):

                    if(jogada[5] == 8):
                        tabuleiro[0] = simbolo
                        jogada.append(0)

                    else:
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                elif(jogada[3] == 5):

                    if(jogada[5] == 0):
                        tabuleiro[8] = simbolo
                        jogada.append(8)

                    elif(jogada[5] == 1):
                        tabuleiro[6] = simbolo
                        jogada.append(6)

                    elif(jogada[5] == 6 or jogada[5] == 8):
                        tabuleiro[0] = simbolo
                        jogada.append(0)

                elif(jogada[3] == 6 or jogada[3] == 8):

                    if(jogada[5] == 1):
                        tabuleiro[5] = simbolo
                        jogada.append(5)

                    else:
                        tabuleiro[1] = simbolo
                        jogada.append(1)

            # Oitava rodada
            if(len(jogada) == 8):

                if(jogada[3] == 3):

                    if(jogada[5] == 8):

                        if(jogada[7] == 1):

                            tabuleiro[6] = simbolo
                            jogada.append(6)

                        else:
                            tabuleiro[1] = simbolo
                            jogada.append(1)

                elif(jogada[3] == 5):

                    if(jogada[5] == 0):

                        if(jogada[7] == 6):

                            tabuleiro[1] = simbolo
                            jogada.append(1)

                        else:
                            tabuleiro[6] = simbolo
                            jogada.append(6)

                    elif(jogada[5] == 1):
                        
                        if(jogada[7] == 0):

                            tabuleiro[8] = simbolo
                            jogada.append(8)

                        else:
                            tabuleiro[0] = simbolo
                            jogada.append(0)

                    elif(jogada[5] == 6 or jogada[5] == 8):

                        if(jogada[7] == 1):
                            tabuleiro[8] = simbolo
                            jogada.append(8)

                        else:
                            tabuleiro[1] = simbolo
                            jogada.append(1)

                elif(jogada[3] == 6 or jogada[3] == 8):

                    if(jogada[5] == 1):

                        if(jogada[7] == 8):
                            tabuleiro[3] = simbolo
                            jogada.append(3)

                        else:
                            tabuleiro[8] = simbolo
                            jogada.append(8)

    else:

        # Identifica o símbolo do oponente
        oponente = "O" if simbolo == "X" else "X"
        
        # 1. Tentar ganhar ou bloquear o jogador
        posicao = melhor_jogada(tabuleiro, simbolo, oponente)
        
        # 2. Se não houver jogada de bloqueio ou vitória, escolha uma posição estratégica
        if(posicao is None):

            # Prioriza o centro
            if(tabuleiro[4] == ""):
                posicao = 4

            else:

                # Se o centro estiver ocupado, priorize os cantos
                posicao = next((pos for pos in [0, 2, 6, 8] if tabuleiro[pos] == ""), None)
                # Se os cantos estiverem ocupados, priorize as bordas

                if(posicao is None):
                    posicao = next((pos for pos in [1, 3, 5, 7] if tabuleiro[pos] == ""), None)
        
        # 3. Executa a jogada se encontrou uma posição válida
        if(posicao is not None):
            tabuleiro[posicao] = simbolo
            jogada.append(posicao)  # Armazena a jogada


def verificaGanhador(tabuleiro):
    # Verificando se o jogador X ganhou (linhas, colunas e diagonais)
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "X" or  # Linha 1
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "X" or  # Linha 2
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "X" or  # Linha 3
        tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "X" or  # Coluna 1
        tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "X" or  # Coluna 2
        tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "X" or  # Coluna 3
        tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "X" or  # Diagonal principal
        tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "X"):   # Diagonal secundária
        
        return 1  # Jogador X ganhou

    # Verificando se o jogador O ganhou (linhas, colunas e diagonais)
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == "O" or  # Linha 1
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == "O" or  # Linha 2
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == "O" or  # Linha 3
        tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == "O" or  # Coluna 1
        tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == "O" or  # Coluna 2
        tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == "O" or  # Coluna 3
        tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == "O" or  # Diagonal principal
        tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == "O"):   # Diagonal secundária
        
        return 2  # Jogador O ganhou

    # Caso ninguém tenha ganhado
    return 0


# Variáveis
tabuleiro = ["", "", "", "", "", "", "", "", ""]  # Tabuleiro linear
jogada = [] #Todas as jogadas feitas

ganhador = 0
quantPartidas = 0 #quantidade de partidas que o simulador vai rodar
quantRodadas = 0 #quantidade de rodadas do simulador

resultados = [0, 0, 0] #1° jogador / 2° jogador 2 ou maquina boba / 3° maquina profissional

# Loop para saber se o jogador quer continuar
while True:

    menu()

    modoJogo = int(input("\nEscolha o modo de jogo: "))

    if(modoJogo != 4):

        quemComeca = random.randint(1, 2)  # Randomizar quem começa

        # Jogador 2 começando
        if (quemComeca == 2 and modoJogo == 2):

            exibirTabuleiro(tabuleiro)

            # O jogador 2 só sai do looping se fizer uma jogada válida
            while True:

                jogador2 = jogador(tabuleiro, jogada, 2, "O")

                if(jogador2):
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

                if(computador):
                    break

        if(quemComeca == 2 and modoJogo == 3):
                
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

        if(modoSimulacao == 2):

            quemComeca = int(input("\nQuem deve começar?\n1= Computador Aleatório\n2= Computador Profissional\n"))


        quantPartidas = int(input("Quer simular quantas partidas: "))

    #loop do jogo
    if(modoJogo != 4):
        while True:
            exibirTabuleiro(tabuleiro)

            # Jogador 1 faz a jogada (sempre ocorre, exceto em simulações automáticas)
            if(ganhador == 0 and len(jogada) < 9 and modoJogo != 4):

                while True:

                    jogador1 = jogador(tabuleiro, jogada)  # Jogador 1 com símbolo 'X'

                    if(jogador1):
                        break

                ganhador = verificaGanhador(tabuleiro)
                exibirTabuleiro(tabuleiro)

            # Modo de jogo 3: Contra o Computador Profissional
            if(modoJogo == 3 and ganhador == 0 and len(jogada) < 9):

                maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")
                exibirTabuleiro(tabuleiro)
                ganhador = verificaGanhador(tabuleiro)

            # Modo de jogo 2: Contra outro jogador
            if(modoJogo == 2 and ganhador == 0 and len(jogada) < 9):

                while True:

                    jogador2 = jogador(tabuleiro, jogada, player=2, simbolo="O")  # Jogador 2 com símbolo 'O'

                    if(jogador2):
                        break

                ganhador = verificaGanhador(tabuleiro)

            # Modo de jogo 1: Contra o computador bobo
            if(modoJogo == 1 and ganhador == 0 and len(jogada) < 9):

                print("\nJogada do computador ", end="")

                # Só fazendo uma graça pra deixar bonitinho
                for c in range(0, 3):
                    sleep(1)
                    print(".", end="", flush=True)

                while True:

                    computador = maquina(tabuleiro, jogada)

                    if(computador):

                        break

                ganhador = verificaGanhador(tabuleiro)

            print("\nJogadas até agora:", jogada)

            # Condições de fim de jogo: Vitória ou empate
            

            if(len(jogada) > 8 or ganhador != 0):

                exibirTabuleiro(tabuleiro)

                if(ganhador == 1):
                    print("\nO jogador 1 venceu!")

                elif(modoJogo == 1 and ganhador == 2):
                    print("\nO computador Aleatorio venceu!")

                elif(modoJogo == 2 and ganhador == 2):
                    print("\nO jogador 2 venceu!")

                elif(modoJogo == 3 and ganhador == 2):
                    print("\nO computador Profissional venceu!")

                else:
                    print("\nEmpate!")

                break
    

    else:

        if(modoSimulacao == 1):

            while quantRodadas < quantPartidas:

                if(ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Aleatório 1:", end=" ")
                    while True:

                        computador1 = maquina(tabuleiro, jogada, simbolo= "X")

                        if(computador1):

                            break
                    
                    print(jogada[-1]) # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)

                if(ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Aleatório 2:", end=" ")
                    while True:

                        computador2 = maquina(tabuleiro, jogada)

                        if(computador2):

                            break
                    
                    print(jogada[-1]) # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)
                
                if(len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if(ganhador == 1):
                        resultados[0] += 1

                    elif(ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")
            print("Computador Aleatório 1 ganhou", resultados[0],"vez(es)")
            print("Computador Aleatório 2 ganhou", resultados[1],"vez(es)")
            print("Deu Velha", resultados[2],"vez(es)")

        elif(modoSimulacao == 2):

            while quantRodadas < quantPartidas:

                if(quemComeca == 1):

                    if(ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Aleatório:", end=" ")
                        while True:

                            computador1 = maquina(tabuleiro, jogada, simbolo= "X")

                            if(computador1):

                                break
                        
                        print(jogada[-1]) # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)


                    if(ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Profissional:", end=" ")
                        

                        computador2 = maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")
                        
                        print(jogada[-1]) # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                else:

                    if(ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Profissional:", end=" ")
                        

                        computador2 = maquinaProf(tabuleiro, jogada, quemComeca, simbolo="O")
                        
                        print(jogada[-1]) # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)


                    if(ganhador == 0 and len(jogada) < 9):

                        print("\nJogada do computador Aleatório:", end=" ")
                        while True:

                            computador1 = maquina(tabuleiro, jogada, simbolo= "X")

                            if(computador1):

                                break
                        
                        print(jogada[-1]) # Mostra a última jogada feita
                        ganhador = verificaGanhador(tabuleiro)

                    
                
                if(len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if(ganhador == 1):
                        resultados[0] += 1

                    elif(ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")

            if(quemComeca == 1):
                print("Computador Aleatório jogando primeiro")
                print("\nComputador Aleatório ganhou", resultados[0],"vez(es)")
                print("Computador Profissional ganhou", resultados[1],"vez(es)")
                print("Deu Velha", resultados[2],"vez(es)")

            else:
                print("Computador Profissional jogando primeiro")
                print("\nComputador Aleatório ganhou", resultados[0],"vez(es)")
                print("Computador Profissional ganhou", resultados[1],"vez(es)")
                print("Deu Velha", resultados[2],"vez(es)")         

        
        else:

            while quantRodadas < quantPartidas:

                if(ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Profissional 1:", end=" ")
                    
                    computador1 = maquinaProf(tabuleiro, jogada, quemComeca=2, simbolo= "X")
                    
                    print(jogada[-1]) # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)


                if(ganhador == 0 and len(jogada) < 9):

                    print("\nJogada do computador Profissional 2:", end=" ")

                    computador2 = maquinaProf(tabuleiro, jogada, quemComeca=1, simbolo= "O")
                    
                    print(jogada[-1]) # Mostra a última jogada feita
                    ganhador = verificaGanhador(tabuleiro)
                
                if(len(jogada) > 8 or ganhador != 0):

                    exibirTabuleiro(tabuleiro)

                    if(ganhador == 1):
                        resultados[0] += 1

                    elif(ganhador == 2):
                        resultados[1] += 1

                    else:
                        resultados[2] += 1

                    quantRodadas += 1
                    limparTabuleiro(tabuleiro)
                    jogada.clear()  # Limpa a lista de jogadas
                    ganhador = 0

            print("\n\n")
            print("Computador Profissional 1 ganhou", resultados[0],"vez(es)")
            print("Computador Profissional 2 ganhou", resultados[1],"vez(es)")
            print("Deu Velha", resultados[2],"vez(es)")


    continuar = str(input('\nQuer jogar novamente [S/N]: ')).strip().upper()[0]

    limparTabuleiro(tabuleiro)

    if(continuar == "N"):
        break
    
