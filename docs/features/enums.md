**Enums** (enumerados) son un conjunto de nombres simbólicos enlazados a valores constantes y únicos. Los miembros de un enumerado pueden ser accedidos a través del operador punto `.`.

## Ejemplo
```py
enum Color
    Red
    White

white: Color = Color.White # Los miembros del enumerado son accedidos con el operador punto
red: Color = Color.Red
mostrar(white != red)
```