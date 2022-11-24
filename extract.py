'''
    Fingerprint Recognition - extract.py

    Este código representa funcionalidades necesarias para la extracción de los
    diferentes especimenes de una huella digital por cada hoja de usuario recolectada.
    Este programa fue realizado usando openCV que está bajo 
    la licencia Apache 2 (siendo está compatible con GLP V3). De esta 
    biblioteca se usaron las funciones basicas para el manipulamiento de
    imagenes


    Copyright (C) 2022  Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr 

    Ultima modificacion: 2022-11-21
    Responsables: Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr 
    Resumen: Creacion del codigo para la extraccion de los especimenes de una huella digital por cada hoja de usuario recolectada

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

import cv2
import numpy as np
import os
import shutil

margin = 20

# Función para obtener los puntos de la parte izquierda de la cuadricula de la hoja de usuario recolectada
# empezando de abajo hacia arriba


def getPointLeft(img, stroke=0, height=None):
    if height == None:
        height, width = img.shape[:2]
    else:
        width = img.shape[1]
    points = []
    for x in reversed(range(height)):
        for y in range(0, width//3):
            if len(points) <= 2:
                if img[x][y] == 255:
                    points.append([x, y])
                    break
            else:
                break
    point = min(points, key=lambda x: x[1], default=None)
    return [point[0]-stroke, point[1]+stroke]

# Función para obtener los puntos de la parte derecha de la cuadricula de la hoja de usuario recolectada
# empezando de abajo hacia arriba


def getPointRight(img, stroke=0, height=None):
    if height == None:
        height, width = img.shape[:2]
    else:
        width = img.shape[1]
    points = []
    for x in reversed(range(height)):
        for y in reversed(range(width//3*2, width)):
            if len(points) <= 2:
                if img[x][y] == 255:
                    points.append([x, y])
                    break
            else:
                break
    point = max(points, key=lambda x: x[1], default=None)
    return [point[0]-stroke, point[1]-stroke]

# Función para obtener los puntos de la parte superior de la cuadricula de la hoja de usuario recolectada
# empezando de la izquierda hacia la derecha


def getPointTop(img, startPoint, stroke=0):
    points = []
    while not (img[startPoint[0]][startPoint[1]] == 0):
        for x in reversed(range(0, startPoint[0])):
            if img[x][startPoint[1]] == 0:
                points.append([x+stroke+1, startPoint[1]])
                startPoint[1] += 1
                break
    return min(points, key=lambda x: x[0], default=None)

# Funcion que extrae las lineas verticales de la imagen que forman una cuadricula


def getVerticals(gray):

    gray = cv2.bitwise_not(gray)
    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 15, -2)

    vertical = np.copy(bw)

    rows = vertical.shape[0]
    verticalsize = rows // 30

    verticalStructure = cv2.getStructuringElement(
        cv2.MORPH_RECT, (1, verticalsize))

    vertical = cv2.erode(vertical, verticalStructure)
    vertical = cv2.dilate(vertical, verticalStructure)

    return vertical

# Funcion que extrae las lineas horizontales de la imagen que forman una cuadricula


def getRects(verticals, file):
    stroke = 0
    rectList = []
    heightPoint = verticals.shape[0]
    startLeftPoint = getPointLeft(verticals, stroke, heightPoint)
    endLeftPoint = getPointTop(verticals, startLeftPoint, stroke)
    topLenght = startLeftPoint[0] - endLeftPoint[0]

    for i in range(2):
        startLeftPoint = getPointLeft(verticals, stroke, heightPoint)
        rightPoint = getPointRight(verticals, stroke, heightPoint)[1]
        rectList.append([[startLeftPoint[0]-topLenght, startLeftPoint[1]], [startLeftPoint[0] -
                        topLenght, rightPoint], startLeftPoint, [startLeftPoint[0], rightPoint]])
        heightPoint = startLeftPoint[0]-topLenght-5

    return rectList

# Funcion que extrae y recorta por separado cada espacio de la imagen de la hoja de usuario recolectada
# segun los datos extraidos de las funciones anteriores


def crop_image(img: np.array, x1, x2, y1, y2, name):
    varName = 1
    distanceX = (x2 - x1)//6
    distanceY = (y2 - y1)//2

    for i in range(2):
        for j in range(6):

            crop = img[12+(y1 + i * distanceY):(y1 + (i+1) * distanceY)-10,
                       10+(x1 + j * distanceX):(x1 + (j+1) * distanceX)-10]

            _, crop = cv2.threshold(
                crop, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

            cv2.imwrite(f"fingerprints2/{name}_{varName}.png", crop)
            varName += 1

# Funcion que crea las carpetas donde se guardaran las imagenes de las hojas de usuarios recolectadas


def makeFolders():
    # Lista de nombres de las carpetas a crear (cada carpeta corresponde a una persona de la lista)
    folderlist = ["Abiel", "Elias", "Fabian", "Roy"]
    if not os.path.exists("fingerprints2"):
        os.mkdir("fingerprints2")

    for person in folderlist:
        if not os.path.exists("fingerprints2/"+person):
            os.mkdir("fingerprints2/"+person)
        else:
            shutil.rmtree("fingerprints2/"+person)
            os.mkdir("fingerprints2/"+person)


# Main del programa que se encarga de llamar a las funciones anteriores
# y guardar las imagenes de las hojas de usuarios recolectadas
# en las carpetas correspondientes
# se debe cambiar el nombre de la carpeta donde se encuentran las hojas de usuario recolectadas
# Las hojas de usuario recolectadas deben estar en formato .png. Para este caso se utilizo una hoja con 2 tablas de 6x2 por usuario
# Este codigo está elaborado para extaer especimenes bajo el formato de la hoja de usuario anteriormente mencionada
if __name__ == "__main__":
    rectList = []
    makeFolders()
    folder = "images"  # Carpeta donde se encuentran las hojas de usuario recolectadas
    for file in os.listdir(folder):

        img = cv2.imread(f"{folder}/" + file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(
            img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        print(f"Procesando: {file}")
        gray = img

        if rectList == []:
            rectList = getRects(getVerticals(gray), file)

        for i in range(len(rectList)):
            if i == 0:
                pathSide = "L"
            elif i == 1:
                pathSide = "R"

            pathSide = f"{file.split('.')[0]}/{pathSide}"
            crop_image(gray, rectList[i][0][1], rectList[i][1][1],
                       rectList[i][0][0], rectList[i][2][0], pathSide)
