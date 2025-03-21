class CuentaBancaria:


    def __init__(self):
        self.dinero = 0
    
    def depositar(self, dinero):
        self.dinero += dinero
    
    def debitar(self, dinero):
        hay_dinero_suficiente = self.dinero >= dinero
        if hay_dinero_suficiente:
            self.dinero -= dinero
        return hay_dinero_suficiente