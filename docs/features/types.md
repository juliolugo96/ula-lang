El tipado es opcional en ULA, pues puedes elegir si los especificas o no. Las variables con tipos de datos no especificados son inferidos en tiempo de compilación a partir del valor asignado.

Las operaciones entre tipos diferentes pueden o bien ser convertidas a un tipo común si ambos tipos son compatibles, o simplemente arrojar un error. Dos tipos son compatibles si ambos representan distenteroos tamaños de un mismo grupo de tipo (Un ejemplo de ello son los enteros o los puntos flotantes).

El tipo de dato deber ser o bien definido por el usuario, o una estructura, enumerado, clase o un tipo primitivo.

### Advertencia
	Los tipos que no son especificados son inferidos, esto es fundamentalmente diferente en comparación con los tipos dinámicos.

---

## Tipos Primitivos

### Entero
Hay múltiples tipos de enteros disponibles basados en la longitud, y en el signo. Pueden tener un mínimo de 8 bits de longitud y un máximo de 128. Si la longitud no es especificada, la misma por defecto es 64.
  - Con signo: `entero`, `entero8`, `entero16`, `entero32`, `entero64`, `entero128`
  - Sin signo: `uentero`, `uentero8`, `uentero16`, `uentero32`, `uentero64`, `uentero128`

```py
x: entero = 5
x += 27

large_num: entero128 = 5
```
#### Información
	En ULA, entero y uentero son por defecto de 64
	 bits, y pueden ensancharse según sea necesario. Este no será el comportamiento por defecto si el tamaño es especificado.

### Flotante
Representa al número real de punto flotante.

```py
x: flotante = 0.5
```

### Doble

Representa al número real de punto flotante de doble precisión.
```py
x: doble = 172312.41923
my_inf = INFINITO # INFINITO tiene el valor especificado en IEEE 754
```

### Cadena
El tipo `cadena` es la implementación ULA de las listas de cadenas/caracteres. Todas las cadenas de ULA soportan UTF-8.

```py
x: cadena = "Hello World!"
x = '🍌'
x = '夜のコンサートは最高でした。'
```

### Booleano
El tipo `booleano` ocupa solo 1 bit y su valor puede ser `VERDADERO` o `FALSO`.

```py
x: booleano = VERDADERO
```

### List
Las listas son mutables por defecto, declaradas usando `[elem1, elem2, ...]` y tienen un tamaño dinámico, comenzando desde 0, y los miembros son accedidos utilizando su índice dentro de corchetes. El tipo de dato de la tupla puede ser declarado entre `<>`. Si es tipo es omitido, la lista tendrá el tipo de los elementos contenidos.

```py
x = [1,2,3,4]
y: lista<doble> = [1.5,5.5]
mostrar(x[2])
```

### Tupla
Las tuplas son como listas, pero inmutables, y declaradas usando `(elem1, elem2, ...,)`
El tipo de dato de la tupla puede ser declarado entre `<>`. Si es tipo es omitido, la tupla tendrá el tipo de los elementos contenidos.

```py
x = (1,5,20)
y: tupla<doble> = (1.5,5.5)
mostrar(x[0])
```

### Rango
El tipo `rango` es similar al rango de Python, utilizando la sintaxis `inicio..fin`, 

Ranges are similar to Python's ranges, defined using `start..end` kind of syntax, and they're especially used for loops

```py
para x en 0..100
	mostrar(x)
```

!!! warning
	Ranges can not currently be assigned to variables

----

### Func
ULA soporta funciones de primera clase, lo que significa que a las variables se les puede asignar funciones, y que el tipo `func` está hecho para denotar el tipo de la función. Los tipos de los parámetros son incluidos entre `<>` separados por coma `,`, y el tipo de retorno con una flecha `->`.

```py
x: func<entero, entero> -> entero = def (x: entero, y: entero) -> entero
	si x > y
		retorna x + y
	sino
		retorna x * y

y = def (x: entero, y: entero) -> entero
	si x > y
		retorna x + y
	sino
		retorna x * y

z: func = def()
    mostrar(5)
```

### Vacío
Vacío es solo utilizado como valor de retorno para las funciones e ilustra el hecho de que las mismas no retornan un valor definido. Si el valor de retorno es omitido, `vacío` será utilizado por defecto. 

```py
def example() -> void
	pass

def example2()	# Here the retorna type is omitted
	pass

```

## Type Operations

### Is
El operador binario `es` chequea si el tipo de dato del operando izquierdo coincide con el tipo de dato del operando derecho, y retorna un booleano como resultado.

```py
x: entero = 5
mostrar(x is entero)
```

### Como
El operador binario `como` convierte al operando izquierdo al tipo de dato del operando derecho y retorna el valor converso.

```py
x: flotante = 5.5
mostrar(x as entero) # Deberia imprimir 5
```
