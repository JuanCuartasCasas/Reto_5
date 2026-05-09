# Reto 5: Modulos Y Paquetes
> Aplicaciòn de modulos y Paquetes en archivos escalables.

El presente demuestra la aplicación y ventajas del uso de módulos y paquetes cómo organizador de proyectos 
en constante evolución, modulando archivos independientes, uná vez se módifique uno de estos, no surgira afectación al cuerpo entero del proyecto

---

Responde a las asignaciones del reto:

- Organizar el reto 4 ( Generación de formas a partir del polimorfismo de clases Base) a partir de módulos y paquetes
- Realizar una organización que module la formación de las estructuras geometricas generales, 
para luego aplicarlas a casos especificos

## Estructura: 

```
├── Space/
│   ├── __init__.py
│   ├── Line.py
│   └── Point.py
│
├── Shape/
|    ├── __init__.py
|    └── Shape.py
| 
├── Shapes/
|    ├── __init__.py
|    ├── Rectangle.py
|    ├── Square.py
|    ├── Triangle.py
|    ├── Equilateral.py
|    ├── Isosceles.py
|    ├── Scalene.py
|    └── Trirectangle.py
│
└── Main.py


```

Busca darle una sintaxis más comprensible, y es totalmente eficiente para una mejora constante

- A partir de la estructura logramos diferenciar los elementos básicos, formando una jerarquia de relación entre módulos,
  Culminando con su punto final en Main.py

- Se da uso del ` __name__ == "__main__"` en el main para validar si es el archivo principal y ejecutar las herramientas asignadas

## Referencias

- [Clase 11: Modulos y Paquete](https://github.com/fegonzalez7/poo_unal_clase11.git)
- [Documentación Python](https://docs.python.org/es/3/tutorial/modules.html)
