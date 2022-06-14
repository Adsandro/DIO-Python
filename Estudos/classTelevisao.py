class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True
            
    def aumentaCanal(self):
        self.canal +=1
    def diminuiCanal(self):
        self.canal -=1
        
if __name__ == '__main__': # Este if certifica que o código funcionara apenas nesse módulo(arquivo py), e não em outro caso seja importado
    televisao = televisao()
    print('Televisão esta ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão esta ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão esta ligada? {}'.format(televisao.ligada))
    televisao.aumentaCanal()
    televisao.aumentaCanal()
    print('Canal {}'.format(televisao.canal))

