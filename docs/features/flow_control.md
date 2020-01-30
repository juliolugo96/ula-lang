## Ciclos mientras


La condición debe ser de tipo booleano (VERDADERO o FALSO)

```py
x = 5
mientras(x < 10)
	x += 1
```

## Ciclos Para

Pueden ser utilizados para iterar sobre rangos o listas

```py
para x en 0..10
	mostrar(x)

mi_lista = [5,8,2]
para num en mi_lista
	mostrar(x)
```

## Sentencias si-sino

La expresión evaluada debe ser del tipo booleano.

```py
si true
	mostrar("Then do this")
sino si true
	mostrar("Never reached")
sino
	mostrar("Not even")
```

## Sentencias segun_sea

**No implicit fallthrough**, this means that in comparison with languages like C, the equivalent to a break statement is implicit in Lesma, therefore you need to specsiy the `fallthrough` keyword for the flow to go downstream to the other casos. Break statements are not allowed inside a segun_sea statement.

```py
par_impar = 1

segun_sea par_impar
	caso 1
		fallthrough # Go to the next caso
	caso 3
		mostrar('Impar')
	defecto
		mostrar("Cualquier número")
		mostrar(par_impar)
	caso 4
		mostrar('Par')
```