Las **Estructuras** cumplen un rol simlar a las clases de datos de Python, las cuales puedes describir como "tuplas nombradas mutables con valores por defecto", pero son más estrictas en el sentido de que no son **clases encubiertas**, pues no puedes definir métodos u otros comportamientos específicos de las mismas, pero aún pueden ser extendidas al sobrecargar operadores y pueden ser definidas como un tipo. Los miembros de una estructura puede ser accedidos con el operador punto `.`.

All the fields of a struct are required arguments on initialization unless a default is provided.

## Ejemplo
```py
estructura Circle
	radius: entero
	x: entero
	y: entero = 4

cir: Circle = Circle(radius=5, x=2)

mostrar(cir.radius)  # Los miembros de una estructura son accedidos utilizando un punto.
```