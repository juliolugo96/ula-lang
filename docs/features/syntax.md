- Los espacios en blanco afectan (al igual que en Python. La identación usa bien sea tabulaciones o exactamente cuatro espacios.
- Las sentencias de control de flujos, estructuras o funciones requieren identación.
- ULA reportará toda la sintaxis errónea.
- El nombre de variable `_` será utilizado como un resultado ignorado, y será tratado similar a como es en Golang.

```py

si VERDADERO
	hacer_esto()
sino si FALSO
	si VERDADERO
	hacer_aquello()
sino
	hacer_otro()

para _ en 0..20
	hacer_esto()

mientras(FALSO)
	hacer_aquello()

```

