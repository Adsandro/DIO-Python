class carro:
    def __init__(self, modelo, desenvolvedora, ano, quantidade_portas):
        self.modelo = modelo
        self.desenvolvedora = desenvolvedora
        self.ano = ano
        self.quantidade_portas = quantidade_portas

    def desbloquear(self):
        print("Portas abertas")
    def bloqueado(self):
        print("Carro bloqueado, caso as portas sejam forçadas soara o alarme!")
    
    def ligar(self):
        print("A chave esta na ignição, pronto para partida")
    def desligar(self):
        print("O carro foi desligado, portanto pode estar retirando a chave")
        
    def carroInformacoes(self):
        print(self.modelo, self.desenvolvedora, self.ano, self.quantidade_portas)

carro1 = carro("sedã", "volkswagen", "2020", "4")

carro1.desbloquear()
carro1.bloqueado()
carro1.ligar()
carro1.desligar()
carro1.carroInformacoes()

