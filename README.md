# IRP-FingerprintRecognition
Introducción al Reconocimiento de Patrones - Proyecto 2

## Instituto Tecnologico de Costa Rica
### Escuela de Computacion

### IC8046 - Introducción al Reconocimiento de Patrones

Profesor: Eduardo Adolfo Canessa Montero

Estudiantes: 
+ Elias Castro Montero - 2020098930 - eliasc5@estudiantec.cr
+ Roy Vinicio Garcia Alvarado - 2020109283 - rvga1311@estudiantec.cr
+ Fabián Rojas Arguedas - 2019380107 - fabian.sajor26@estudiantec.cr
+ Abiel Porras Garro - 2020209597 - abielpg@estudiantec.cr

Semestre II 2022

# Proyecto

El objetivo de este proyecto es crear un sistema de reconocimiento de huellas digitales para la asignatura de Introduccion al Reconocimiento de Patrones. El proyecto consiste en un sistema donde se permite registrar la huella digital de un usuario que este carga al sistema. El sistema extrae los puntos clave y los descriptores de la misma y los guarda en un archivo. Cuando el usuario desea ingresar al sistema, este carga una imagen de su huella digital y el sistema la procesa y compara con las huellas digitales registradas. Si el sistema encuentra una huella digital similar, el usuario es identificado, dando el nombre en pantalla del usuario con el que fue reconocido. Si no se encuentra una huella digital, el usuario no es identificado.

# Licencia

Todos los archivos de codigo fuente usados para este proyecto están bajo la lincencia GNU General Public License version 3. Se permite la copia, distribucion y modificacion del software siempre que realice un seguimiento de los cambios/fechas en los archivos fuente. Cualquier modificación o software, incluido (a través del compilador) código con licencia GPL, también debe estar disponible bajo la GPL junto con las instrucciones de compilación e instalación.

Copyright (C) 2022  Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr"

# Datos
El sistema fue desarrollado en Python 3.10.5 y utiliza la libreria OpenCV para el procesamiento de imagenes y la libreria tkinter para la interfaz grafica.

## Requerimientos para usar el sistema
+ Python 3.8 o superior
+ Biblioteca ```OpenCV``` para el procesamiento y manipulación de imágenes.
+ Biblioteca ```tkinter``` para la interfaz gráfica.
+ Biblioteca ```numpy``` para el manejo de matrices (formato en el que las imagenes son almacenadas).
+ Biblioteca ```os``` para el manejo de archivos y carpetas.
+ Biblioteca ```shutil``` como complemento para el manejo de archivos y carpetas.
+ Biblioteca ```math``` para el uso de funciones ```atan2``` y ```degrees```  utilizadas para la alineación de las hojas de usuarios.
+ Bilioteca ```PIL``` para el manejo y renderización de imagenes en la interfaz grafica.
+ Biblioteca ```time``` para el manejo de tiempo en la interfaz grafica; más especificamente para el uso de la función ```sleep``` para animar la barra de progreso.

## Nota importante
El sistema fue desarrollado en Windows 11. La función ```os.system("start COPYING")``` fue utilizada para abrir los archivos COPYING  en el sistema operativo Windows. En caso de que el sistema sea ejecutado en otros sistemas operativos, se recomienda cambiar esta función el comando correspondiente que permita abrir un archivo de texto en un visualizador de texto externo, teniendo que ejemplares como Okular (en cuyo caso el comando seria ```os.system("okular COPYING")```). Dicho reemplazo debe ser realizado en el archivo ```main.py``` en la linea 160 dentro de la función declarada como ```openLicense()```.
