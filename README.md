# PythonScafold
## Plantilla para la entrega de proyectos de Computacion I
Supongamos que el laboratorio contiene varios ejercicios y deseas organizarlos por carpetas como se muestra en la siguiente imagen:
![Carpeta Ejemplo](/images/example1.png)

Dentro de cada carpeta se encuentran los incisos resueltos y separados por archivos como se muestra a continuación:
![archivos](/images/example2.png)

La documentación de python explica que es posible utilizar un archivo para ejecutar diversas instancias de programas únicamente sigue esta pequeña guia.


** Crear el directorio del proyecto **

En tu editor favorito dentro de cada directorio a incluir deberás crear un archivo ```__init__.py```. agrega la siguiente lineas de código:
Si en tu carpeta tienes los archivos ````foo.py boo.py coo.py```

``{python}

# Ejemplo del contenido carpeta1/__init__.py

##Primero importamos los archivos
import foo
import boo
import coo

```

Ahora en el directorio de tu tarea por ejemplo app deberemos agregar el main.py con lo siguiente:

```
import sys,os,pkgutil


def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module

def main():
	load_all_modules_from_dir('ejer1')
	print "Archivo principal"

if __name__ == '__main__':
        main()

```

Como puedes observar se incluye una funcion __load_all_modules_from_dir('ejer1')__ esta funcion deberá llevar el nombre del directorio que quieres incluir si deseas incluir todos los subdirectorios deberas hacer los siguiente en la función main:

```
def main():
	load_all_modules_from_dir('directorio1')
	load_all_modules_from_dir('directorio2')
	load_all_modules_from_dir('directorio3')
	load_all_modules_from_dir('directorio4')
	print "Archivo principal"
```


Para ejecutar tu programa unicamente llamarás al programa main de la siguiente manera:
```
python main.py
```

o si lo prefieres en ipython puedes utilizar el comando ````run main.py```.
