diretorio = 'c:/Workspace/DIO-Python/Estudos/Manipulação de arquivos/LoremIpsum.txt'
def escreverArquivo (texto):
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()
    
def atualizarArquivo(texto):
    arquivo = open(diretorio, 'a')
    arquivo.write(texto)
    arquivo.close()
    
def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
    
if __name__ == '__main__':
    texto = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
    
    
    escreverArquivo('{}. \n'.format(texto))
    # atualizarArquivo('terceira linha. \n')
    lerArquivo(diretorio)