from os import getpid
from psutil import Process
from matplotlib import pyplot as plt
from time import time
from string import ascii_letters
from random import choice, randint
from terminaltables import AsciiTable

N_REPETITION = 5
N_TIMES = 10000009
N_STEP = 1000000


def graph_men_and_time(data, title):
    """
    :param title
    :param data
        {
            "data": [
                (i, men, tm, x_time)
            ],
            "title": "Label"
        }
    """
    x_axis, y_men_axis, y_time_axis = [], [], []
    for i, men, tm, x_time in data:
        x_axis.append(i)
        y_time_axis.append(tm)
        y_men_axis.append(men)
    graph(x_axis, y_time_axis, title, "N", "Time (s)")
    graph(x_axis, y_men_axis, title, "N", "Memory (kb)")


def graph(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def get_current_ram():
    """
    :return ran memory in KB
    """
    return Process(getpid()) \
        .memory_info() \
        .rss


def get_current_time():
    """
    :return current time in second
    """
    return time()


def generate_range_numbers():
    return [i for i in range(0, N_TIMES)]


def get_avg(arr):
    return sum(arr) / len(arr)


def get_deviation(avg, arr):
    acc = 0
    for v in arr:
        acc += (v - avg) ** 2
    return (acc / (len(arr) - 1)) ** 0.5


def standardize_sample(dic_sample):
    sample = []
    for key, values in dic_sample.items():
        men_values = values[0]
        tm_values = values[1]

        avg_men = get_avg(men_values)

        avg_time = get_avg(tm_values)
        dev_time = get_deviation(avg_time, tm_values)

        sample.append((key, avg_men, avg_time, dev_time))
    return sample


def with_rep_and_standardize(func, rep=N_REPETITION):
    columns = [('N (unidad)', 'Memoria Actual (KB)', 'Tiempo promedio(s)', 'Varianza Tiempo')]
    sample = {}
    for _ in range(rep):
        func(sample)
    data = standardize_sample(sample)
    print(AsciiTable(columns + data).table)
    return data


def add_to_sample(n, delta, men, sample):
    if n in sample:
        sample[n][0].append(men)
        sample[n][1].append(delta)
    else:
        sample[n] = [[men], [delta]]
    return sample


def get_random_str(size):
    s = size * "".join([choice(ascii_letters),
                        choice(ascii_letters),
                        choice(ascii_letters),
                        choice(ascii_letters)])
    return s[:size]


def random_number_between(start=0, end=N_TIMES):
    return randint(start, end)

from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, add_to_sample, get_random_str, N_STEP


def repeated_character(str):
    chars_dic = {}
    for val in str:
        if val not in chars_dic:
            chars_dic[val] = 1
        else:
            chars_dic[val] += 1
    return chars_dic


def generate_repeated_character():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            s = get_random_str(j)
            init = get_current_time()
            repeated_character(s)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, N_STEP, add_to_sample, random_number_between


def generate_sample_append():
    def f(sample):
        sample_list = []
        for j in range(0, N_TIMES, N_STEP):
            init = get_current_time()
            sample_list.append(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_copy():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.copy()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_index():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.index(0)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_insert_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            index = 0
            n = random_number_between()
            init = get_current_time()
            list_sample.insert(index, n)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_insert_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            index = int((len(list_sample) - 1) / 2)
            n = random_number_between()
            init = get_current_time()
            list_sample.insert(index, n)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_insert_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            index = j - 1
            n = random_number_between()
            init = get_current_time()
            list_sample.insert(index, n)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


def generate_sample_remove_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            init = get_current_time()
            list_sample.remove(0)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            index = int((len(list_sample) - 1) / 2)
            init = get_current_time()
            list_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            index = j - 1
            init = get_current_time()
            list_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_sort():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            list_sample = [random_number_between() for i in range(j)]
            init = get_current_time()
            list_sample.sort()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            el = list_sample[0]
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            el = list_sample[int((len(list_sample) - 1) / 2)]
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = [i for i in range(j)]
            el = list_sample[j-1]
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)

from util import with_rep_and_standardize, get_current_ram, \
    get_current_time, N_TIMES, N_STEP, add_to_sample


def generate_sample_add():
    def f(sample):
        sample_set = set()
        for j in range(0, N_TIMES, N_STEP):
            init = get_current_time()
            sample_set.add(j)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_clear():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.clear()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_copy():
    def f(sample):
        for j in range(0, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            init = get_current_time()
            set_sample.copy()
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = min(set_sample)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = int(j / 2)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_remove_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            set_sample = set([i for i in range(j)])
            index = max(set_sample)
            init = get_current_time()
            set_sample.remove(index)
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_start():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = 0
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_middle():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = int(j / 2)
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample

    return with_rep_and_standardize(f)


def generate_sample_in_end():
    def f(sample):
        for j in range(1, N_TIMES, N_STEP):
            list_sample = set([i for i in range(j)])
            el = j-1
            init = get_current_time()
            el in list_sample
            men, delta = get_current_ram(), get_current_time() - init
            sample = add_to_sample(j, delta, men, sample)
        return sample
    return with_rep_and_standardize(f)


from character_frecuency import generate_repeated_character
import time_comparison_list
import time_comparison_set
from util import graph_men_and_time


def main():
    # List
    list_samples = [
        {"func": time_comparison_list.generate_sample_append, "title": "List Append"},
        {"func": time_comparison_list.generate_sample_clear, "title": "List clear"},
        {"func": time_comparison_list.generate_sample_copy, "title": "List copy"},
        {"func": time_comparison_list.generate_sample_index, "title": "List index"},
        {"func": time_comparison_list.generate_sample_insert_start, "title": "List insert start"},
        {"func": time_comparison_list.generate_sample_insert_middle, "title": "List insert middle"},
        {"func": time_comparison_list.generate_sample_insert_end, "title": "List insert end"},
        {"func": time_comparison_list.generate_sample_remove_start, "title": "List remove start"},
        {"func": time_comparison_list.generate_sample_remove_middle, "title": "List remove middle"},
        {"func": time_comparison_list.generate_sample_remove_end, "title": "List remove end"},
        {"func": time_comparison_list.generate_sample_sort, "title": "List sort"},
        {"func": time_comparison_list.generate_sample_in_start, "title": "List in start"},
        {"func": time_comparison_list.generate_sample_in_middle, "title": "List in middle"},
        {"func": time_comparison_list.generate_sample_in_end, "title": "List in end"}
    ]
    print("================List Sample================")
    for sample in list_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Set
    set_samples = [
        {"func": time_comparison_set.generate_sample_add, "title": "Set add"}
        {"func": time_comparison_set.generate_sample_clear, "title": "Set clear"},
        {"func": time_comparison_set.generate_sample_copy, "title": "Set copy"},
        {"func": time_comparison_set.generate_sample_remove_start, "title": "Set remove start"},
        {"func": time_comparison_set.generate_sample_remove_middle, "title": "Set remove middle"},
        {"func": time_comparison_set.generate_sample_remove_end, "title": "Set remove end"},
        {"func": time_comparison_set.generate_sample_in_start, "title": "Set in start"},
        {"func": time_comparison_set.generate_sample_in_middle, "title": "Set in middle"},
        {"func": time_comparison_set.generate_sample_in_end, "title": "Set in end"}
    ]

    print("================Set Sample================")
    for sample in set_samples:
        print("Sample for {} generated".format(sample["title"]))
        graph_men_and_time(sample['func'](), sample["title"])

    # Repeated character
    print("================Repeated character Sample================")
    print("Sample for {} generated".format("Repeated Characters"))
    graph_men_and_time(generate_repeated_character(), "Repeated Character")


if __name__ == '__main__':
    main()
