import os
import psutil
import time

# frecuencia de caracteres de un string
process = psutil.Process(os.getpid())
w = "QWERTYQWERTYYERRTYUEERERRGG"


def repe(w):
    caracteres = sorted(w)
    contador = len(caracteres)
    char = ""
    dccionario = {}
    for y in range(contador):
        if char != caracteres[y]:
            repeticion = caracteres.count(caracteres[y])
            char = caracteres[y]
            dccionario[caracteres[y]] = repeticion

    return dccionario


def repeCaracter(w):
    for i in range(0, 5):
        print("-------------------------------------------------------")
        for x in range(0, 10000, 1000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            for _ in range(x):
                repe(w)
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)

import os
import psutil
import time

# list
process = psutil.Process(os.getpid())
colores = ['Rojo', 'Azul', 'Gris']


def insert():
    for i in range(0, 5):
        print("----------------INSERT---------------------")
        for x in range(0, 10000000, 1000000):
            colores = []
            for _ in range(x):
                colores.append("azul")
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            colores.insert(1, 'verde')
            duracion = time.time() - tiempo_inicial
            print("n: ", x, '\t', "tiempo ", duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print(ram_usada)


def indice():
    for i in range(0, 5):
        print("----------------INDEX---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            colores = ['rojo', 'Gris']
            for _ in range(x):
                colores.index('Gris')
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def copiar():
    for i in range(0, 5):
        print("----------------COPIAR---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            colores = ['rojo', 'Gris']
            for _ in range(x):
                colores.copy()
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def remover():
    for i in range(0, 5):
        print("----------------REMOVE---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            for _ in range(x):
                colores.append("azul")
                colores.remove('azul')
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def ordenar():
    for i in range(0, 5):
        print("----------------SORT---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            colores = ['rojo', 'Gris']
            for _ in range(x):
                colores.sort()
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def clearlist():
    for i in range(0, 5):
        print("----------------CLEAR---------------------")
        for x in range(0, 10000000, 1000000):
            colores = []
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            for _ in range(x):
                colores.clear()
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


if __name__ == '__main__':
    insert()
    indice()
    copiar()
    remover()
    ordenar()
    clearlist()

# Set
frutas = {"apple", "banana", "cherry"}


def agregar():
    for i in range(0, 5):
        print("----------------ADD---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            frutas.add("grenade")
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def copiarset():
    for i in range(0, 5):
        print("----------------COPY---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            frutas.copy()
            duracion = time.time() - tiempo_inicial
            print("n: ", x, '\t', "tiempo ", duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def remover1():
    for i in range(0, 5):
        print("----------------REMOVE---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            for _ in range(x):
                frutas.add("granade")
                frutas.remove('granade')
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


def cleanset():
    for i in range(0, 5):
        print("----------------CLEAN---------------------")
        for x in range(0, 10000000, 1000000):
            ram_inicial = process.memory_info().rss  # in bytes
            tiempo_inicial = time.time()
            for _ in range(x):
                frutas.clear()
            duracion = time.time() - tiempo_inicial
            print(x, '\t', duracion)
            ram_usada = process.memory_info().rss - ram_inicial  # in bytes
            print("RAM USADA: ", ram_usada)


if __name__ == '__main__':
    agregar()
    copiarset()
    remover1()
    cleanset()
    repeCaracter(w)
