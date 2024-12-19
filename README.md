# Ejercicio 4
## reto 4
En este ejercicio podemos observar la implementación de composición, de hherencia, de polimorfismo y de encapsulamiento.
el objetivo es una mega clase que le de a las clases hijas diferentes datos y atributos, de los cuales le permita conocer el area, el perimetro, los vertices, las aristas y los angulos internos. 
pero primero creamos la clase padre donde estara gran parte de todo el codigo.
```python

class Point ():
    def __init__(self,x_y):
        self.x, self.y = x_y
    def punto_(self):
        self.xy = self.x, self.y
        return self.xy


class Linea():

    def __init__ ( self, punto_inicial: tuple ,  punto_final: tuple ):
        self.punto1 = Point(punto_inicial)
        self.punto  = Point(punto_final)
        self.p1  = self.punto1.punto_()
        self.p0 = self.punto.punto_()
        self.distance = float(((self.punto.x - self.punto1.x )**2+(self.punto.y - self.punto1.y )**2)**0.5)
    def distancia(self):
        return self.distance


class Shape():
    regular: bool 
    def __init__(self):
        pass
    def calcular_area(self ):
        pass
    def vertices(self, lista : "Point"):
        pass
    def aristas(self, lista : "Linea"):
        pass
    def angulos_interiores (self ):
        pass
    def calcular_perimetro(self):
        pass
```
Para la creación de este mismo me base en crear las figuras desde lo mas pequeño hasta lo mas grande, osea use composición para que el usuario me ingresara los vertices (puntos) y yo pueda unir esos puntosen un orden especcifico de tal manera que me quede la figura deseada y asi poder usar los diferentes metodos que se quieren tener, como el area o el perimetro etc.
Para darse una idea es algo asi :

```mermaid
classDiagram
class point {
+vertice: punto
}
class linea {
+arista: 2 puntos
}
figura {
+cuadrado :  lineas
}
point-->linea
linea-->figura

```
