# Ejemplos

Un poco de información acerca de cómo manejar el lenguaje, su sintaxis y su semántica.

```py
# Hola mundo
mostrar('Hola Mundo')

# Declaración de variables y asignaciones
numero = 23 

numero+=5

pregunta = 'what\'s going on' # Escape

# Lista mutable
cosas = [1, 2, 3] 

# La misma que la anterior, pero inicializada con azúcar sintáctica
cosas_repetida = 0..4 

# Tupla
otras_cosas = (1.5, 9.5) 

# Diccionario
varios = {'primer_nombre': 'Samus', 'primer_apellido': 'Aran'} # Dictionary

mostrar(cosas[1 + 1])

si numero > 23
	mostrar('Mayor que 23')
sino si numero == 23
	mostrar('Igual a 23')
sino
	mostrar('Menor que 23')

para x en 0..40 # Ciclo repita_para en un rango
	mostrar(x * 2)

para elem en cosas # Iterar sobre objetos
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
