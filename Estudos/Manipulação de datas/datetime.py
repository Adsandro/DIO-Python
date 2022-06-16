from datetime import date, time, datetime, timedelta

def Date():
    print("Trabalhando com data")
    dataAtual = date.today()
    DataAtualStr = dataAtual.strftime('%A %B %Y')
    print(DataAtualStr)
    print(type(dataAtual))
    print(type(DataAtualStr))

def Time():
    print("Trabalhando com Horas")
    horario = time(hour=15, minute=18, second=10)
    print(horario)
    print(type(horario))
    horarioStr = (horario.strftime('%H:%M:%S'))
    print(horarioStr)
    print(type(horarioStr))
    
def DateTime():
    print("Trabalhando com data e hora atual")
    dataAtual = datetime.now()
    print(dataAtual)
    print(type(dataAtual))
    dataAtualStr = (dataAtual.strftime('%d/%m/%Y %H:%M:%S'))
    print(dataAtualStr)
    print(dataAtual.strftime('%c'))
    
def DateTimeSingular ():
    print("Trabalhando com data de forma singular")
    dataAtual = datetime.now()
    print(dataAtual.day)
    print(dataAtual.month)
    print(dataAtual.year)
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta' , 'sabado', 'domingo')
    print(tupla[dataAtual.weekday()])
    
def CriaData ():
    print("Trabalhando com criação de datas")
    dataAtual = datetime.now()
    dataCriada = datetime(2018, 6, 20, 10, 12, 2)
    print(dataCriada)

def stringParaDateTime ():
    print("Transformando string em data")
    dataString = '1/12/2002'
    dataConvertida = datetime.strptime(dataString, '%d/%m/%Y')
    print(dataConvertida)
    print(type(dataConvertida))

def manipulaData():
    print("Soma e subtrai datas")
    novaData = datetime.now() - timedelta(days=20)
    print(novaData)
    

divisor = ("=+"*30)

if __name__ == '__main__':
    print(divisor)
    Date()
    print(divisor)
    Time()
    print(divisor)
    DateTime()
    print(divisor)
    DateTimeSingular()
    print(divisor)
    CriaData()
    print(divisor)
    stringParaDateTime()
    print(divisor)
    manipulaData()
    print(divisor)




# Livraria utilizada do python
# https://docs.python.org/3/library/datetime.html