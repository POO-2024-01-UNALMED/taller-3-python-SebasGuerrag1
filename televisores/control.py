class Control:
    def __init__(self):
        self._tv=0
    
    #metodos remotos
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown
    def volumenUp(self):
        self._tv.volumenUp
    def volumenDown(self):
        self._tv.volumenDown
    def setVolumen(self,volumen):
        self._tv.setVolumen(volumen)

    def setCanal(self,canal):
        self._tv.setCanal(canal)

    #metodo enlazar
    def enlazar(self,tv):
        self._tv=tv
        self._tv.setControl(self)
    def getTv(self):
        return self._tv
    def setTv(self,tv):
        self._tv=tv

