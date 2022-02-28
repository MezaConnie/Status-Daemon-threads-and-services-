# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:22:11 2022

@author: macon
"""

import threading
import time
from threading import Thread

class Alumno:
    def __init__(self, nombre = '', codigo = None, carrera = None):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
    
    def __str__(self) -> str:
        return f'\nEstudiante\nNombre: {self.nombre}\nCodigo: {str(self.codigo)}\nCarrera: {self.carrera}\n'
    
    def recover(self):
        with open('alumno.txt', 'r') as file:
            self.nombre = file.readline().strip()
            self.codigo = int(file.readline())
            self.carrera = file.readline()
            
class Hilo(Thread):
    def __init__(self, objeto:Alumno):
        Thread.__init__(self)
        self.running = True
        self.objeto = objeto
        self.daemon = True

    def run(self):
        while self.running:
            time.sleep(2)
            self.objeto.recover()

    def stop(self):
        self.running = False
        
A = Alumno()
def printLoop():
    for i in range(1000):
        print(A)
        time.sleep(2)
try:
  A.recover()
  t1 = Hilo(A)
  t2 = threading.Thread(target=printLoop)
  t1.start()
  t2.start()
except ValueError:
  print("Datos incorrectos en el archivo.")

#import subprocess

#path = "C:\Users\macon\Documents\Sem VI\Tolerante\daemon threads\main.py"

#while True:
#    try:
#        subprocess.check_call(["python2", path])
#    except subprocess.CalledProcessError:
#        continue