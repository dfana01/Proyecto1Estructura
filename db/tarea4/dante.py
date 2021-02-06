from random import shuffle


class Student:
    display_name = None

    def __init__(self, display_name):
        self.display_name = display_name

    def __repr__(self):
        return "{}".format(self.display_name)

    def __gt__(self, other):
        return self.display_name > other.display_name

    def __lt__(self, other):
        return self.display_name < other.display_name


def get_shuffle_list():
    samples_student = [
        Student("Monet"),
        Student("Maximillian"),
        Student("Rhiannan"),
        Student("Reema"),
        Student("Erin"),
        Student("Maciej"),
        Student("Hannah"),
        Student("Ilyas"),
        Student("Travis"),
        Student("Antony"),
    ]
    shuffle(samples_student)
    return samples_student.copy()


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


if __name__ == '__main__':
    print(get_shuffle_list())
    print(insertion_sort(get_shuffle_list()))
    print(bubble_sort(get_shuffle_list()))
    print(selection_sort(get_shuffle_list()))
