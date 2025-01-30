#1. Criar um ficheiro de texto vazio (sem nada escrito)
#2. Abrir o ficheiro e escrever "Boa noite"
#3. Ler e mostrar o que foi escrito
#4. Abrir o ficheiro criado e anexar "Está quase na hora de jantar"
#5. Ler o ficheiro alterado

file=open('ivo.txt','w')
file.write('Boa noite')
file=open('ivo.txt','r')
print(file.read())
file=open('ivo.txt','a')
file.write('\n'+'Está quase na hora de jantar')
file=open('ivo.txt','r')
print(file.read())
