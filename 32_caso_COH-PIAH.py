import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado: ")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    similaridade_ab = 0
    
    for z in range(0,6):
        similaridade_ab = similaridade_ab + (abs(as_a[z] - as_b[z]))
    return similaridade_ab / 6
    
def calcula_assinatura(texto):

    tm_palavras = 0
    type_token = 0
    hapax_legomana = 0
    tm_sentencas = 0
    complex_sentenca = 0
    tm_frase = 0
    
    soma_caracteres_sentenca = 0
    soma_das_palavras = 0
    soma_caracteres_frase = 0
    
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for s in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(s)        
        comprimento_frases = separa_frases(s)

        for c in comprimento_frases:
            frases.append(c)

    for f in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(f)
        comprimento_palavras = separa_palavras(f)

        for c in comprimento_palavras:
            palavras.append(c)
    
    for p in palavras:
        soma_das_palavras = soma_das_palavras + len(p)
    
    tm_palavras = soma_das_palavras /len(palavras)
    type_token = n_palavras_diferentes(palavras)/len(palavras)
    hapax_legomana = n_palavras_unicas(palavras)/len(palavras)
    tm_sentencas = soma_caracteres_sentenca / len(sentencas)
    complex_sentenca = len(frases) / len(sentencas)
    tm_frase = soma_caracteres_frase / len(frases)

    assinatura = [tm_palavras, type_token, hapax_legomana, tm_sentencas,
                  complex_sentenca, tm_frase]

    return assinatura

def avalia_textos(textos, ass_cp):
    listando = []
    
    for t in textos:
        lista_texto = calcula_assinatura(t)
        listando.append(compara_assinatura(lista_texto, ass_cp))

    menor = listando[0]
    x = 1

    for r in range(1, len(listando)):
        if (menor > listando[r]):
            x = r
    return x

def resultado():        
    assinatura_ass_cp = le_assinatura()
    textos = le_textos()
    x = avalia_textos(textos, assinatura_ass_cp)
    print("O autor do texto", x," está infectado com COH-PIAH")

resultado()