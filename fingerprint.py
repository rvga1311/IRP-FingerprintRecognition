'''
    Fingerprint Recognition - fingerprint.py

    Este código representa las funcionalidades necesarias para un reconocedor 
    de huellas digitales, siendo el objetivo principal de este proyecto de 
    software. Este programa fue realizado usando openCV que está bajo 
    la licencia Apache 2 (siendo está compatible con GLP V3). De esta 
    biblioteca se usaron las funciones principales de SIFT para extraer 
    escalares invariantes y FLANN para obtener los vecinos cercanos.

    Para fines de privacidad y seguridad personal, no se ha incluido las huellas dactilares de los usuarios
    que se usaron durante la realizacion de este proyecto.


    Ultima modificacion: 2022-11-24
    Responsables: Roy Garcia Alvarado - rvga1311@estudiantec.cr & Abiel Porras Garro - abielpg@estudiantec.cr & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr  & Elias Castro Montero - eliasc5@estudiantec.cr & Fabián Rojas Arguedas - fabian.sajor26@estudiantec.cr 
    Resumen: Creacion del codigo para el reconocimiento de huellas digitales usando SIFT y FLANN de openCV. Limpieza de codigo.

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


def fingerprintRecognition(imgToRecognize, imgToCompare):
    sift = cv2.SIFT_create()

    keyPointsImg1, descriptorsImg1 = sift.detectAndCompute(
        imgToRecognize, None)

    matchesResult = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), {}).knnMatch(
        descriptorsImg1, imgToCompare[0], k=2)

    ratio = 0.7
    matchPoints = []
    for i, j in matchesResult:
        if i.distance < ratio * j.distance:
            matchPoints.append(i)

    minKeyPoints = min(len(keyPointsImg1), imgToCompare[1])
    return len(matchPoints) / minKeyPoints * 100


def FingerprintMatch(file):
    imgToRecognize = cv2.imread(file, 0)

    bestMatch = 0
    recognizedUser = ""
    for users in os.listdir('fingerprints'):
        content = np.loadtxt(f'fingerprints/{users}')
        content = np.array(content, dtype=np.float32)
        lenKp = int(users.split('_')[1].split('.')[0])
        imgToCompare = (content, lenKp)

        score = fingerprintRecognition(imgToRecognize, imgToCompare)
        score = score if score >= 1 else score * 100
        if score > bestMatch:
            bestMatch = score
            recognizedUser = users.split('_')[0]

        # print(f'User: {users.split("_")[0]} - Score: {score}')
    if bestMatch >= 50:
        return recognizedUser


def createUser(name, fileFingerprint):
    if not os.path.exists(f'fingerprints'):
        os.mkdir(f'fingerprints')

    img = cv2.imread(fileFingerprint, 0)

    sift = cv2.SIFT_create()
    keyPointsImg, descriptorsImg = sift.detectAndCompute(img, None)
    np.savetxt(f'fingerprints/{name}_{len(keyPointsImg)}.txt', descriptorsImg)
