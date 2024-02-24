class TV:
    _numTV=0
    def __init__(self, marca,estado):
        self._marca= marca
        self._estado= estado
        self._precio=500
        self._canal=1
        self._volumen=1
        self._control=0
        TV._numTV+=1
    
    #metodo set y get para marca
    def getMarca(self):
        return self._marca
    def setMarca(self,marca):
        self._marca=marca
    #metodo set y get estado
    def getEstado(self):
        return self._estado
    def setEstado(self,estado):
        self._estado= estado
    #metodo get y set numTV
    @classmethod
    def setNumTV(cls,numTV):
        cls._numTV = numTV
    def getNumTV():
        return TV._numTV
    
        
    #metodo get y set precio
    def getPrecio(self):
        return self._precio
    def setPrecio(self,precio):
        self._precio=precio
    #metodo get y set canal
    def getCanal(self):
        return self._canal
    def setCanal(self,canal):
        if(self._estado and self._canal>0 and self._canal<121):
            self._canal=canal
    #metodo volumen get y set 
    def getVolumen(self):
        return self._volumen
    def setVolumen(self,volumen):
        if (self._estado==True and self._volumen<8 and self._volumen>-1):
            self._volumen=volumen
    #metodo turn off y on
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    #metodo canal up y down
    def canalUp(self):
        if(self._estado==True and self._canal<120):
            self._canal+=1
    def canalDown(self):
        if(self._estado and self._canal>1):
            self._canal+=1
    #metodo volumen up y Down
    def volumenUp(self):
        if(self._estado==True and self._volumen<7):
            self._volumen+=1
    def volumenDown(self):
        if(self._estado==True and self._volumen>0):
            self._volumen-=1
    #metodo Control get y set
    def setControl(self,control):
        self._control=control
    def getControl(self):
        return self._control
    