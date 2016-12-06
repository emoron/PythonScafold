# PythonScafold
## Plantilla para la entrega de proyectos de Computacion I

How to use a ```__main__.py``` file

La documentacin de python explica que es posible utilizar un archivo para ejecutar diversas instancias de programas unicamente sigue esta pequeña guia.

** Crear el directorio del proyecto **En tu editor favorito crea el archivo  ```app/__main__.py```. agrega la siguiente lineas de código:
```{python}

# Ejemplo del contenido app/__main__.py

##Primero importamos los archivos
import tarea1 as t1
import tarea2a as t2a
import tarea2b as t2b



def main():
  print('The rain in Spain falls mainly in the plain.')
  t2a.entrega()
  t2b.entrega()
   
## en esta funcion podemos llamar a los archivos de nuestro proyecto
if __name__ == '__main__':
  main()
  
```

A continuación en lugar de ejecutar el archivo ```__main__.py``` directamente, tratamos el directorio como si fuera un programa de la siguiente manera:
```
$ python app
```

En el caso de ipython podemos corres de la misma manera.

```{python}
[1] run app

```
