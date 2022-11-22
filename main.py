'''
    Fingerprint Recognition - main.py

    Este código representa una simulacion de un sistema de reconocimiento de huellas dactilares. 
    En este caso, se ha añadido una interfaz gráfica para poder interactuar con el sistema.
    En el sistema se puede registrar un usuario con su huella dactilar y posteriormente,
    se puede identificar al usuario con su huella dactilar.
    Para fines de privacidad y seguridad personal, no se ha incluido las huellas dactilares de los usuarios
    que se usaron durante la realizacion de este proyecto.

    La interfaz gráfica ha sido creada con la libreria tkinter, bajo la licencia Python License.


    Copyright (C) 2022  Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr 

    Ultima modificacion: 2022-11-21
    Responsables: Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr 
    Resumen: Creacion de la interfaz grafica para el sistema de reconocimiento de huellas dactilares.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from fingerprint import *
import time

# Configuración de la ventana
window = Tk()
window.title("Caja fuerte")
# change color of background
bgColor = "#395685"
window.configure(background=bgColor)
window.geometry('1000x700')
window.resizable(False, False)

# Función para la animacion de la barra de progreso


def progress():
    Progress_Bar.pack(pady=spacing, side=TOP)
    Progress_Bar['value'] = 20
    menu_frame.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 50
    menu_frame.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 80
    menu_frame.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 100


filename = None

# Función para habilitar el boton de registro una vez que se haya escrito el nombre del usuario


def toggle_state(*_):
    if userName.var.get():
        registerUser['state'] = 'normal'
        registerUser['bg'] = "#395685"
    else:
        registerUser['state'] = 'disabled'
        registerUser['bg'] = '#0b2247'

# Renderizacion de componentes en caso que se quiera registrar un usuario
# Se pide el nombre del usuario y se habilita el boton de registro el cual llama a la funcion registerUserAction


def registerGUI():
    welcomeLabel.pack_forget()
    global filename
    filename = filedialog.askopenfilename(
        title="Abrir", filetypes=[("Imagen", "*.jpg *.jpeg *.png")])

    infoLabel.pack(pady=spacing+20, side=TOP)
    userName.pack(side=TOP)
    registerUser.pack(pady=spacing+20, side=TOP)

    userName.var = StringVar()
    userName['textvariable'] = userName.var
    userName.var.trace_add('write', toggle_state)

# Funcion para registrar un usuario usando funciones de fingerprint.py


def registerUserAction():
    name = userName.get()
    print(name)
    print(filename)
    createUser(userName.get(), filename)
    userName.delete(0, 'end')
    registerUser.pack_forget()
    userName.pack_forget()
    infoLabel.pack_forget()

# Renderizacion de componentes en caso que se quiera identificar un usuario
# Se carga una imagen y se usa la funcion FingerprintMatch para identificar al usuario
# Se muestra en pantalla si el usuario ha sido reconocido o no


def login():
    userName.delete(0, 'end')
    registerUser.pack_forget()
    userName.pack_forget()
    infoLabel.pack_forget()
    welcomeLabel.pack_forget()

    filename = filedialog.askopenfilename(
        title="Abrir", filetypes=[("Imagen", "*.jpg *.jpeg *.png")])
    img = Image.open(filename)
    img = img.resize((326//2, 444//2))
    img = ImageTk.PhotoImage(img)
    imgLabel = Label(menu_frame, image=img)
    imgLabel.pack()
    progress()

    user = FingerprintMatch(filename)

    while Progress_Bar['value'] < 100:
        continue

    Progress_Bar.pack_forget()
    loading.pack_forget()
    imgLabel.pack_forget()

    if user == "":
        text = "No se ha podido identificar al usuario"
    else:
        text = f"Usuario identificado: {user}"

    welcomeLabel['text'] = text
    welcomeLabel.pack(pady=spacing+20, side=TOP)

# Renderizacion de componentes de "Acerca de"


def exitAbout():
    about_frame.pack_forget()
    menu_frame.pack()

# Funcion para abrir el archivo de licencia


def openLicense():
    os.system("start LICENSE")

# Renderizacion de componentes de "Acerca de"
# En esta funcion se renderiza informacion acerca del proyecto


def about():
    menu_frame.pack_forget()
    about_frame.pack()

    exitBtn = Button(about_frame, text="Salir", command=exitAbout,
                     bg="#395685", fg="white", font=("Arial", 20))
    exitBtn.pack(pady=spacing, side=TOP)

    copyingOpenBtn = Button(about_frame, text="Abrir licencia",
                            command=openLicense, bg="#395685", fg="white", font=("Arial", 20))
    copyingOpenBtn.pack(pady=spacing, side=TOP)

    info = "Este proyecto fue realizado por Roy Garcia Alvarado, Abiel Porras Garro, Elias Castro Montero y Fabián Rojas Arguedas como proyecto de la materia de Introduccion al Reconocimiento de Patrones del Instituto Tecnológico de Costa Rica, sede San José. El objetivo de este proyecto es crear un sistema de reconocimiento de huellas digitales para la asignatura de Introduccion al Reconocimiento de Patrones. El sistema fue desarrollado en Python 3.10.5 y utiliza la libreria OpenCV para el procesamiento de imagenes y la libreria tkinter para la interfaz grafica. El sistema fue probado en Windows 11. El sistema fue desarrollado usando Visual Studio Code.\n El proyecto consiste en un sistema donde se permite registrar la huella digital de un usuario que este carga al sistema. El sistema extrae los puntos clave y los descriptores de la misma y los guarda en un archivo. Cuando el usuario desea ingresar al sistema, este carga una imagen de su huella digital y el sistema la procesa y compara con las huellas digitales registradas. Si el sistema encuentra una huella digital similar, el usuario es identificado, dando el nombre en pantalla del usuario con el que fue reconocido. Si no se encuentra una huella digital similar, el usuario no es identificado.\n Todos los archivos de codigo fuente usados para este proyecto están bajo la lincencia GNU General Public License version 3. Se permite la copia, distribucion y modificacion del software siempre que realice un seguimiento de los cambios/fechas en los archivos fuente. Cualquier modificación o software, incluido (a través del compilador) código con licencia GPL, también debe estar disponible bajo la GPL junto con las instrucciones de compilación e instalación.\n \n Copyright (C) 2022  Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr"
    label = Label(about_frame, text=info, bg=bgColor,
                  fg="white", font=("Arial", 14), wraplengt=900)
    label.pack(pady=spacing+20, side=TOP)


# =============== Frame Menu =============== #
spacing = 10
menu_frame = Frame(window, width=1200, height=800)
menu_frame.configure(background=bgColor)

about_frame = Frame(window, width=1200, height=800)
about_frame.configure(background=bgColor)

menu_frame.pack()

title = Label(menu_frame, text="Bienvenido a la caja fuerte de huellas dactilares", font=(
    "Arial", 30), bg=bgColor, fg="white", wraplengt=500)
title.pack(pady=spacing+30, side=TOP)

register_btn = Button(menu_frame, text="Registrar Huella Digital",
                      command=registerGUI, font=("Arial", 20), bg=bgColor, fg="white")
register_btn.pack(pady=spacing, side=TOP)

login_btn = Button(menu_frame, text="Iniciar Sesión",
                   command=login, font=("Arial", 20), bg=bgColor, fg="white")
login_btn.pack(pady=spacing, side=TOP)

about_btn = Button(menu_frame, text="Acerca de", command=about,
                   font=("Arial", 20), bg=bgColor, fg="white")
about_btn.pack(pady=spacing, side=TOP)

# =============== Utilities =============== #
loading = Label(menu_frame, text="Analizando...", font=(
    "Arial", 20), bg=bgColor, fg="white", wraplengt=500)
registerEnd = Label(menu_frame, text="Registro exitoso", font=(
    "Arial", 20), bg=bgColor, fg="white", wraplengt=500)
Progress_Bar = Progressbar(
    menu_frame, orient=HORIZONTAL, length=250, mode='determinate')
userName = Entry(menu_frame, width=30, borderwidth=5, font=("Arial Bold", 15))
registerUser = Button(menu_frame, text="Registrar", command=registerUserAction, font=(
    "Arial Bold", 20), bg='#0b2247', fg="white", state='disabled')
infoLabel = Label(menu_frame, text="Ingrese su nombre de usuario SIN ESPACIOS", font=(
    "Arial Bold", 15), bg=bgColor, fg="white")
welcomeLabel = Label(menu_frame, text="", font=(
    "Arial", 20), bg=bgColor, fg="white")


window.mainloop()
