


class Ventana:
    __titulo=''
    __xd=0
    __yd=0
    __xi=0
    __yi=0
    def __init__(self,title,xi=0,yi=0,xd=500,yd=500):
        self.__titulo=title
        self.__xi=xi
        self.__yi=yi
        self.__xd=xd
        self.__yd=yd
        pass
    def Mostrar(self):
        y=','
        print("indice superior    indice inferior    titulo")
        print(str(self.__xi),y,str(self.__yi).ljust(17),str(self.__xd),y,str(self.__yd).ljust(9),self.__titulo)
    def getTitulo(self):
        return(self.__titulo)
    def alto(self):
        alto=self.__yd-self.__yi
        return alto
    def ancho(self):
        ancho=self.__xd-self.__xi
        return ancho
    def moverDerecha(self,valor=0):
        if  self.__xd<500:
            self.__xd+=valor
            self.__xi+=valor
        return
    def moverIzquierda(self,valor=0):
        if self.__xi>0:
            self.__xi-=valor
            self.__xd-=valor
        return
    def bajar(self,valor=0):
        if self.__yd<500:
            self.__yd+=valor
            self.__yi+=valor
        return
    def subir(self,valor=0):
        if self.__yi>0:
            self.__yd-=valor
            self.__yi-=valor


    
    
