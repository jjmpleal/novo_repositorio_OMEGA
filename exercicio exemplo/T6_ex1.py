# Crie um programa em Python que recebendo um ficheiro de texto, peça ao utilizador que pesquise uma
# determinada palavra no ficheiro. Caso esta palavra exista, deverá ser devolvida a linha ou as linhas
# onde essa palavra se encontra.
# Garanta que o seu programa, consegue pesquisar a palavra, seja ela inserida em maiúsculas ou minúsculas.

ficheiro = open('exemploTarefa6.txt', 'r', encoding='utf8') 
palavra = input("Palavra a pesquisar: ")
linhas = ficheiro.readlines()  #Lê todas as linhas do ficheiro e armazena-as como uma lista na variável linhas.
                                #Cada elemento da lista corresponde a uma linha do ficheiro.

palavra = palavra.lower()      #Converte a palavra inserida pelo utilizador para letras minúsculas, para que a  
                               #pesquisa seja insensível a maiúsculas/minúsculas.

lista_encontradas = []        #Inicializa uma lista vazia chamada lista_encontradas, que será usada para armazenar
                              # as linhas onde a palavra for encontrada.


for numero, linha in enumerate(linhas, start=1):  #6ª linha: Inicia um ciclo for para iterar sobre cada linha do ficheiro:
                                                  #numero: É o número da linha, gerado pela função enumerate (começando por 1 graças a start=1).
                                                  #linha: É o conteúdo da linha.
    if palavra in linha.lower():
        lista_encontradas.append((numero, linha.strip()))  #linha.strip() remove espaços e quebras de linha no início e no final da linha.

if lista_encontradas:
    print(f"'{palavra}' existe nas linhas:")
    for numero, frase in lista_encontradas:
        print(f"{numero}: {frase}")
else:
    print(f"A palavra '{palavra}' não encontrada no ficheiro.")

ficheiro.close()   #Fecha o ficheiro aberto, liberando os recursos associados. Boa prática