arquivoNota = input('informe o nome do arquivo que estão as notas: ')
diretorio = "c:/Workspace/DIO-Python/Estudos/Manipulação de arquivos/{}.txt".format(arquivoNota)

def notaAluno():
    alunoNota = input('Informe o nome do aluno e suas notas seguidas por virgula (,) :')
    arquivo = open(diretorio, 'w')
    arquivo.write(alunoNota)
    arquivo.close()
     
def notaAlunoAtualiza():
    alunoNota = input('Informe o nome do aluno e suas notas seguidas por virgula (,) :')
    arquivo = open(diretorio, 'a')
    arquivo.write(alunoNota, '\n')
    arquivo.close()

def mediaNotas():
    arquivo = open(diretorio, 'r')
    notaAluno = arquivo.read()
    notaAluno = notaAluno.split('\n') 
    #Transforma o Array em lista informando uma condição para a divisao
    listaMedia = []
    for x in notaAluno: 
        #Com o split informado anteriormente esse trecho funcionara corretamente, sem dividir o array por letras
        listaNotas = x.split(',') 
        aluno = listaNotas[0]
        listaNotas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        listaMedia.append({aluno:media(listaNotas)})
    print(listaMedia)
    
if __name__ == '__main__':
    mediaNotas()
