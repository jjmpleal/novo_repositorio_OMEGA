frase = input("Digite uma frase: ")
    
# Nome do ficheiro
nome_ficheiro = "frase.txt"
    
# Escreve a frase no ficheiro
file=open('frase.txt','w')
file.write(frase)

print(f"A frase foi escrita no ficheiro '{nome_ficheiro}'.")
    
# Lê o conteúdo do ficheiro e imprime no ecrã
file=open('frase.txt','r')
print(file.read())

