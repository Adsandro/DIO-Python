class computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print("Ligando o computador!!")
    def desligar(self):
        print("Desligando o computador!!")
        
    def exibeInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = computador("LENOVO","12GB", "RV8")
computador1.ligar()
computador1.desligar()
computador1.exibeInformacoes()