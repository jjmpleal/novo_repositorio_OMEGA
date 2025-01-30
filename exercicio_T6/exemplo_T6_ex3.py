

nomefich = input("Nome do ficheiro: ").lower()
nomefich = nomefich+".txt"
max = 0
nome =""
soma = 0
contar = 0

try:
    lerFicheiro = open(nomefich,"r+",encoding="utf-8")
    
except:
    print("Altere o nome! O Ficheiro não existe ou a localização errada!!!")

else: #garante que só se executa o código se o ficheiro for aberto com sucesso.
    while True: #inicia um loop infinito para ler linha por linha.

        linha = lerFicheiro.readline() #lê uma linha do ficheiro.
        if not linha:  #se não tiver nada termina
            break
        else:
            if linha == "\n": #Se a linha for apenas uma mudança de linha ("\n"), o código não faz nada (pass).
                pass          #Poderia usar linha.strip() para remover espaços e evitar pass.
            else:
                aluno = linha.split(",") #cada linha do fich passa para uma lista nome, nota
                nota = int(aluno[1])
                if nota > max: 
                    max = nota
                    nome = aluno[0]  
                    
                    #melhores_alunos = [aluno[0]]
                #elif nota == max:
                 #   melhores_alunos.append(aluno[0])
                    
                    
                    
                    
                    
                soma += nota  #acumular as notas 
                contar += 1   #conta o nº de alunos
                if nota > 9:
                    print(f"{aluno[0]:.<25} {nota}  Aprovado")  #:.<25 para alinhar o texto.
                else:
                    print(f"{aluno[0]:.<25} {nota}  Reprovado")
    print("-"*40)
    print(f"Média das notas ......... {soma/contar:.2f}")
    print(f"Melhor nota: {nome:.<12} {max}")
    print("-"*40)
    lerFicheiro.close()