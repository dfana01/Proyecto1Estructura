import re
from os import scandir
import sys

# 76/100

# no se hicieron tests de integracion que validen el algoritmo funcionando en conjunto -4
# no se contempla cambio de variables -20


def read_file(path):
    """
    :complexity
        - time: O(n), Dado que debe recorrer cada caracter.
        - space: O(n), Dado que se cuenta como n la por la cantidad de caracteres a pesar de que solo se ejecuta una instrucción de lectura y se almacenara en una variable.
    """
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text


def equalize_functions_n_vars(s):
    """
    :complexity
        - time: O(n), dado que se recorre 2 veces el string pero estos no estan anidados. 
        - space: O(1), pues no se usan regex constates.
        notes: todo estos procesos requieren previo a la ejecución la creacion del arbol de regex este tiene un costo en time y space O(2^m)
        ref: https://stackoverflow.com/a/5892130/6872875
    """
    return re.sub("(?<=public static void).*?\w+", re.sub(r"\w+\s+[=]\s+", "var1=", re.sub(r"\bdef\s+\w+\b\(", "func1(", s)))


def clean(s):
    """
    :complexity
        - time: O(n), dado que se recorre 3 veces el string pero estos no estan anidados.
        - space: O(1), pues no se usan nuevas variables.
    """
    return s.replace(" ", "").replace("\t", "").replace("\n", "")


def calculate_similarity(s1, s2, difference):
    """
    :complexity
        - time: O(1), solo se ejecuta una instrucción
        - space: O(1), solo se ejecuta una instrucción sin crear nuevas variables.
    """
    return round((1 - (difference / max(len(s1), len(s2)))) * 100, 2)


def levenshtein_distance(s1, s2):
    """
    :complexity
        - time: O(NxM), dado que se comparan todos los elementos dentro de la matriz.
        - space: O(NxM), porque se genera una matriz para almacenar todas las comparaciones.
    """
    m, n = len(s1) + 1, len(s2) + 1
    d = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        d[i][0] = i
    for j in range(n):
        d[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1
    return d[len(s1)][len(s2)]


def equal(s1, s2):
    """
    :complexity
        - time: O(1), Pues solo se comparan dos string.
        - space:  O(1), Pues no hay nuevas varibles.
    """
    return s1 == s2


def read_folder_meta(path):
    """
    :complexity
        - time: O(n), Pues se recorren todos los archivos para ver cuales aplican para ser escaneados y su mayor
        complejidad puede ser n donde n es la cantidad máxima de archivo.
        - space: O(1), Dado que el mismo genera una lista donde la mayor complejidad son todos los archivos dentro de
        la carpeta enviada por parámetro pero no la almacena en ninguna variable.
    """
    return filter(lambda x: x.name.endswith('.java') or x.name.endswith('.c') or x.name.endswith('.py'), scandir(path))


def plagiarism_checker(base_path):
    """
    :complexity
        - time: O(N^2 * M * P), dado que este recorre todos los archivos dos veces anidados este es O(n^2) mas la 
        ejecución del algoritmo de comparación que es N * P.
        - space: O(1), Dado que se utiliza una sola variable para los resultados y no se usa ninguna lista su
        complejidad es constante.
    :enhance: 
        - Se puede intentar bajar la complejidad de tiempo algoritmo calculando la comparaciones y almacenando
        asi sacrificando la complejidad de espacio a O(n) y tratar de bajar la complejidad de tiempo no calculando nueva vez
        los datos calculados. 
        - Se podria mejorar cambiando el algoritmo de levenshtein distance por uno que se pueda hacer comparaciones en conjunto 
        - Agregar un proceso de hash para hacer comparaciones previas a la de levenshtein distance y solo correr levenshtein cuando 
        sea necesaria.
    """
    results = f"==========================Folder: {base_path}==========================\n"
    for entry0 in read_folder_meta(base_path):
        content0 = read_file(entry0.path)
        results += f"- {entry0.name}\n"
        for entry1 in read_folder_meta(base_path):
            if entry1.name == entry0.name:
                continue
            content1 = read_file(entry1.path)

            diff_with_tap_n_space = levenshtein_distance(content0, content1)
            diff_with_equalize_function = levenshtein_distance(equalize_functions_n_vars(clean(content0)),
                                                               equalize_functions_n_vars(clean(content1)))
            diff = levenshtein_distance(clean(content0), clean(content1))

            probability_with_tap_n_space = calculate_similarity(content0, content1, diff_with_tap_n_space)
            probability_with_equalize_function = calculate_similarity(equalize_functions_n_vars(clean(content0)),
                                                                      equalize_functions_n_vars(clean(content1)),
                                                                      diff_with_equalize_function)
            probability = calculate_similarity(clean(content0), clean(content1), diff)

            results += f"\t|_____{entry1.name}\n"
            results += f"\t\t\t|_____there are {probability}% of plagiarism without taps and spaces\n"
            results += f"\t\t\t|_____there are {probability_with_tap_n_space}% of plagiarism with taps and spaces\n"
            results += f"\t\t\t|_____there are {probability_with_equalize_function}% of plagiarism with equalize " \
                       f"functions and variables\n "
            if equal(clean(content0), clean(content1)):
                results += f"\t\t\t|_____files are equal\n"
            if probability_with_tap_n_space <= 80 and probability >= 50:
                results += f"\t\t\t|_____is possible that the user try to hide plagiarism with taps and spaces\n"
            if probability_with_tap_n_space <= 80 and probability_with_equalize_function >= 50:
                results += f"\t\t\t|_____is possible that the user try to hide plagiarism renaming function and/or " \
                           f"variables\n"
    return results


if __name__ == '__main__':
    print(plagiarism_checker(sys.argv[1])) # pueden usar sys.args
