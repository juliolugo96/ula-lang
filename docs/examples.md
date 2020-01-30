# Ejemplos

Un poco de inparamación acerca de cómo manejar el lenguaje, su sintaxis y su semántica.

```py
# Hola mundo
mostrar('Hola Mundo')

# Declaración de variables y asignaciones
numero = 23 

numero+=5

pregunta = 'what\'s going on' # Escaping

# Lista mutable
cosas = [1, 2, 3] 

# La misma que la anterior, pero inicializada con azúcar sintáctica
cosas_repetida = 0..4 

# Tupla
otras_cosas = (1.5, 9.5) 

# Diccionario
varios = {'first_name': 'Samus', 'last_name': 'Aran'} # Dictionary
otros_varios: list<int> = [] # Empty Array of ints

mostrar(cosas[1 + 1])

si numero > 23
	mostrar('greater than 23')
sino si numero == 23
	mostrar('equals 23')
sino
	mostrar('less than 23')

para x en 0..40 # para loop using a range
	mostrar(x * 2)

para elem en cosas # Iterate over objects
	mostrar(item)

mientras numero > 1
	numero -= 1
	mostrar(numero)

si 2 en cosas
	mostrar('yes')

si 2 no en cosas
	mostrar('no')

par_impar = 1
```
