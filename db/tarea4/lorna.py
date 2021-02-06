class Estudiante:
    def __init__(self, nombre, apellido, id):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id

    def __str__(self):
        return str.format("({},{},{})", self.nombre, self.apellido, self.id)

    def __gt__(self, other):
        if isinstance(other, Estudiante):
            if self.nombre != other.nombre:
                return self.nombre > other.nombre
            else:
                return self.apellido > other.apellido


def insertion_sort(arr):
    for index in range(1, len(arr)):
        valorActual = arr[index]
        posicionActual = index

        while posicionActual > 0 and (arr[posicionActual - 1], valorActual):
            arr[posicionActual] = arr[posicionActual - 1]
            posicionActual = posicionActual - 1

        arr[posicionActual] = valorActual

    return arr


def bubble_sort(arr):
    # blucle de pasadas
    for i in range(0, (len(arr) - 1)):
        # bucle de comparacion e intercambios
        for j in range(0, (len(arr) - 1)):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def selection_sort(arr):
    # i indicates how many items were sorted
    for i in range(len(arr)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i + 1, len(arr)):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]


est1 = Estudiante("Lorna", " Espinosa", " 20145845")
est2 = Estudiante("Pablo", " Sanchez", " 25874")
est3 = Estudiante("Flerida", " Cuello", " 00000")
est4 = Estudiante("Angela", " Ureña", " 00001")

arrStudents = [est1, est2, est3, est4]

if __name__ == '__main__':
    insertion_sort(arrStudents)
    bubble_sort(arrStudents)
    selection_sort(arrStudents)
    for students in arrStudents:
        print(students)