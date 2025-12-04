# OBRIGATÓRIO PREENCHER:

# NUMERO ALUNO: 40250183
# NOME: Inês Santos

import random
import os

def fillBoard():                                            #preencher board
    """
    Fill the table board (3x3 list) with random values. 
    Point 1 of Exercice script.   
    """
    global board
    board = [[0]*3 for _ in range(3)]
    return board

def printBoard():                                           #imprimir board
    """
    Print the table board in the format presentend in the exercice.    
    Point 2 of Exercice script.
    """

    print("\n"+"Tabuleiro de Jogo".center(40))              #titulo centrado
    print("-"*40)                                           #traços horizontais
    for row in board:                                       #para cada linha do board
        print("         ".join(f"{v:2d}" for v in row).center(40))
    print("-"*40+"\n")                                      #traços horizontais

def sumBoard():                                             #soma dos valores do board
    """
    Sum all the values present in the board and return the result.
    Point 4 of Exercice script.
    """
    return sum(sum(linha) for linha in board)               


def play():                                                 #função do jogo
    """
    Implement the point 3 of the exercice script 
    """
    global terminar                                         
    global moves

    try:
        linha=input("Indique a linha (1-3) ou Q para sair: ").strip().lower()  #pedir linha ou sair
        
        if linha=="q": #sair do jogo
            terminar=True
            return
        
        linha=int(linha)
        coluna=int(input("Indique a coluna (1-3): "))       #pedir coluna

        if not (1<=linha<=3 and 1<=coluna<=3):              #se linha ou coluna inválidas
            raise ValueError
    except ValueError:
        print("\nCoordenadas inválidas!\n")                 #mensagem de erro para coordenadas inválidas
        return

    r,c=linha-1,coluna-1                                    #posicoes no board

    if board[r][c]!=0:                                      #verificar se posicao ja utilizada
        print("\nPosição já revelada!\n")
        return

    usados={v for linha in board for v in linha if v != 0}  #valores já usados no board
    livres=[n for n in range(1, 31) if n not in usados]     #valores disponíveis para usar

    if not livres:
        print("\nSem números disponíveis.\n")               #mensagem de erro para sem números disponíveis
        terminar = True
        return

    board[r][c]=random.choice(livres)                       #atribuir valor aleatório disponível
    moves+=1                                                #incrementar número de jogadas

    printBoard()                                            #imprimir board atualizado

    total=sumBoard()                                        #calcular soma dos valores do board
    
    if total>=100:                                          #verificar condição de vitória ou seja soma dos numeros >=100
        print(f"Parabéns, ganhou em {moves} jogadas!")
        terminar=True                                       #ganhar o jogo

    elif all(v != 0 for linha in board for v in linha):     #verificar se todas as posições estão preenchidas
        print("Não consegui ganhar! Tente novamente!")
        terminar=True                                       #perder o jogo                        

#------------------- TABLE BOARD GAME -------------------#

fillBoard()                                                 #inicio do código, mostra board vazio com 0s
printBoard()

terminar=False
moves=0

while not terminar:
    play()

