Las **Clases** are objects that bundle fields and methods to provide additional functionality that you can further use as a type for any variable, which can then be further expanded using operator overloading and other type-specific behaviour. Classes members can be accessed using a dot `.`.

Las clases **requieren que sea especificado un constructor**.

## Ejemplo
```py
clase Vehicle
	year: entero
	color: str

	# Constructor
	def new(year: entero, color: cadena)
		this.year = year
		this.color = color  

# Inheritance
clase Car: Vehicle
	def new(year: entero, color='green', hatchback=FALSO)
		self.hatchback = hatchback
		super.Vehicle(year, color)

	def print_year() -> void
		mostrar('This car was made in {self.year}')

ford = Car(1992)

mostrar(ford.hatchback)
ford.print_year()
```