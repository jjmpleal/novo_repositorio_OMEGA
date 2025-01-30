ficheiro=open('exemplo.txt','r')
linhas=ficheiro.readlines()
        
# Contar o número de linhas
num_linhas = len(linhas)
        
# Contar o número de palavras e caracteres
num_palavras = 0
num_caracteres = 0
        
for linha in linhas:
    palavras = linha.split() # dividir (ou separar) uma string em várias partes
    num_palavras += len(palavras)
    num_caracteres += len(linha)
        
        # Imprimir os resultados
#print(f"Ficheiro: {nome_ficheiro}")
print(f"Número de linhas: {num_linhas}")
print(f"Número de palavras: {num_palavras}")
print(f"Número de caracteres: {num_caracteres}")

