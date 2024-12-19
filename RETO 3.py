#Defina una clase base MenuItem: esta clase
#  debe tener atributos como nombre, precio y un método para calcular el precio total

#Cree subclases para diferentes tipos de elementos de menú: herede de MenuItem y 
# defina propiedades específicas para cada tipo (por ejemplo, bebida, aperitivo, plato principal).


# Defina una clase de pedido: esta clase debe tener una lista de objetos y métodos MenuItem para 
# agregar artículos, calcular el monto total de la factura y, potencialmente, aplicar descuentos 
# específicos según la composición del pedido.
class MenuItem():    
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def neto(self):
        return self._precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"{self._nombre}: ${self._precio}"


class  Almuerzo(MenuItem):
    def __init__(self, nombre: str, precio: float, sopa: bool):
        super().__init__(nombre, precio)
        self._sopa = "con sopa" if sopa else "sin sopa"
        if not sopa:
            self._precio -= 500

    def get_sopa(self):
        return self._sopa

    def set_sopa(self, sopa):
        self._sopa = "con sopa" if sopa else "sin sopa"
        if not sopa:
            self._precio -= 500
        else: 
            self._precio += 500
            
    def __str__(self):
        return f"{super().__str__()} ({self._sopa})"

    

class Jugo(MenuItem):                                            
    def __init__(self, nombre: str, precio: float, agua: bool):
        super().__init__(nombre, precio)
        self._agua = "Jugo en agua" if agua else "Jugo en leche"
        if not agua:
            self._precio += 1500

    def get_agua(self):
        return self._agua

    def set_agua(self, agua):
        self._agua = "Jugo en agua" if agua else "Jugo en leche"
        if not agua:
            self._precio += 1500
        else: 
            self._precio -= 1500       
    
    
        
class Postre(MenuItem):
    def __init__(self, nombre: str, precio: float, extra: bool):
        super().__init__(nombre, precio)
        self._extra = "Postre normal" if not extra else "Postre Grande"
        if extra:
            self._precio += 2000

    def get_extra(self):
        return self._extra

    def set_extra(self, extra):
        self._extra = "Postre normal" if not extra else "Postre Grande"
        if extra:
            self._precio += 2000
        else: 
            self._precio -= 2000

class Order:
    def __init__(self):                        
        self.lista_cuenta = []
          
    def añadidura(self, item: "MenuItem"):
        self.lista_cuenta.append(item)
    
    def cuenta(self):
        self.total = float(0)                
        
        for item in self.lista_cuenta:
            self.total += item.neto()

        return self.total
    
    def Pago(self):
        if 100000>self.total >=80000:
            return self.total*0.95 
        elif 300000>self.total>=100000:
            return self.total*0.90
        elif 500000>self.total>=300000:
            return self.total*0.85
        elif 1000000>self.total>500000:
            return self.total*0.8
        else:
            return self.total*0.7

cliente = Order()                                             
cliente.añadidura(Jugo("maracuya", 5000, False))   
cliente.añadidura(Almuerzo("corriente", 12000, False))
cliente.añadidura(Postre("wafles", 2500, True))
cliente.añadidura(Jugo("fresa", 5000, True))   
cliente.añadidura(Almuerzo("pescado", 20000, False))
cliente.añadidura(Postre("fresas con crema", 3000, True))
cliente.añadidura(Jugo("mora", 5000, False))   
cliente.añadidura(Almuerzo("bandeja paisa", 25000, True))
cliente.añadidura(Postre("arequipe", 1000, True))
cliente.añadidura(Jugo("mango", 5000, True))   
cliente.añadidura(Almuerzo("corriente", 25000, True))
cliente.añadidura(Postre("brownie", 1000, True))

print(f"Total before discount: ${cliente.cuenta()}")
print (f"total after discount: $ {cliente.Pago()}")
