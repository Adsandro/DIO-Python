nomeDoArquivo = input('informe o nome do arquivo: ')
diretorio = 'c:/Workspace/DIO-Python/Estudos/Manipulação de arquivos/{}.txt'.format(nomeDoArquivo)

def EscreveTexto():
    textoParaEscrever = input("Informe o texto que deve ser escrito: ")
    escreve = open(diretorio, 'w')
    escreve.write(textoParaEscrever, '\n')
    escreve.close()
    
def VisualizarTexto(diretorio):
    visualizar = open(diretorio, 'r')
    texto = visualizar.read()
    print(texto)

def AtualizarTexto(diretorio):
    novoTexto = input('Informe o texto que deve ser adicionado: ')
    atualizar = open(diretorio, 'a')
    atualizar.write(novoTexto, )
    atualizar.close()

if __name__ == '__main__':
    EscreveTexto()
    VisualizarTexto(diretorio) #Repete o texto escrito
    AtualizarTexto(diretorio)
    VisualizarTexto(diretorio) #Repete o texto escrito
