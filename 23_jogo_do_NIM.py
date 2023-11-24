def computador_escolhe_jogada(n, m):
    vezdocomputador = 1
    
    while vezdocomputador < m:
        if (n - vezdocomputador) % (m + 1) == 0:
            return vezdocomputador
        else:
            vezdocomputador = vezdocomputador + 1
    return vezdocomputador
    
def usuario_escolhe_jogada(n, m):
    valorvalido = False
    
    while not valorvalido:
        vezdojogador = int(input("Quantas peças você vai tirar? "))
        if vezdojogador > m or vezdojogador < 1 or vezdojogador > n:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            valorvalido = True
    return vezdojogador

def campeonato():
    rodada = 1
    while rodada <= 3:
        print()
        print("**** Rodada,", rodada, "****")
        partida()
        rodada = rodada + 1
    print()
    print("Placar: Voce 0 X 3 Computador")

def partida():
    ncondiçao = False
    mcondiçao = False
    
    while not ncondiçao:
        n = int(input("Quantas peças? "))
        if n < 1:
            print("Valor inválido, digite novamente.")
        else:
            ncondiçao = True
    
    while not mcondiçao:
        m = int(input("Limite de peças por jogada? "))
        if m < 1:
            print("Valor inválido, digite novamente.")
        else:
            mcondiçao = True
            
    computadorcomeça = False
    
    if n % (m + 1) == 0:
        print()
        print("Voce começa!")
    else:
        computadorcomeça = True
        print()
        print("Computador começa!")
    
    while n > 0:
        if computadorcomeça:
            vezdocomputador = computador_escolhe_jogada(n, m)
            n = n - vezdocomputador
            if vezdocomputador == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", vezdocomputador, "peças")
            computadorcomeça = False
        else:
            vezdojogador = usuario_escolhe_jogada(n, m)
            n = n - vezdojogador
            if vezdojogador == 1:
                print()
                print("Voce tirou uma peça")
            else:
                print()
                print("Voce tirou", vezdojogador, "peças")
            computadorcomeça = True
        if n == 1:
            print()
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n != 0:
            print()
            print("Agora restam", n, "peças no tabuleiro.")
    
    print("Fim do jogo! O computador ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada ")
x = int(input("2 - para jogar um campeonato "))

if x == 2:
    print()
    print("Voce escolheu um campeonato!")
    campeonato()
elif x == 1:
    print()
    print("Voce escolheu uma partida isolada!")
    partida()
else:
    print()
    print("Digite um número válido!")

    