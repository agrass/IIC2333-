import multiprocessing

class Proceso:

    def __init__(self,id,nombre,tiempo):
        self.id = id
        self.name = nombre
        self.time = tiempo

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getId(self):
        return self.id

class Llamada(Proceso):

    def __init__(self,nombre,tiempo,numero,duracion):
        self.id = id
        self.name = nombre
        self.time = tiempo
        self.number = numero
        self.length = duracion

    def getNumber(self):
        return self.number

    def getLength(self):
        return self.length

class Mensaje(Proceso):

    def __init__(self,nombre,tiempo,numero,texto):
        self.id = id
        self.name = nombre
        self.time = tiempo
        self.number = numero
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

if __name__ == "__main__":

    m = Mensaje('Mensaje Entrante',1,'2345678','Probando mensaje entrante')
    print '('+ str(m.getTime()) + ') ' + m.getName() + ' de ' + m.getNumber() + ': ' + m.getText()
