from sa.algorythms import *
from sa.helper_functions import *
import time as t
import csv

"""
author: Mikołaj Kikolski
date: 10.05.2021
"""

# nasze 4 długości to 1e1, 1e2, 1e3, 1e4
arr_e2 = generate_data(1e2)
arr_e3 = generate_data(1e3)
arr_e4 = generate_data(1e4)
arr_e5 = generate_data(1e5)

csv_rows_q = [["len", "try", "time"]]
csv_rows_qu = [["len", "try", "time"]]
csv_rows_bu = [["len", "try", "time"]]


def pomiar(arr):
    l = len(arr)
    for i in range(6):
        start = t.time()
        quicksort(list(arr), 0, len(arr) - 1)
        czas = t.time() - start
        csv_rows_q.append([str(l), i, czas])
    with open(f'quicksort_{l}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows_q)
    print("Zapisano plik z danymi dla algorytmu quicksort")
    for i in range(6):
        start = t.time()
        new_quicksort(list(arr), 0, len(arr) - 1)
        czas = t.time() - start
        csv_rows_qu.append([str(l), i, czas])
    with open(f'quicksort_updated_{l}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows_qu)
    print("Zapisano plik z danymi dla algorytmu quicksort_u")
    for i in range(6):
        start = t.time()
        bubble_sort(list(arr))
        czas = t.time() - start
        csv_rows_bu.append([str(l), i, czas])
    with open(f'bubblesort_{l}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_rows_bu)
    print("Zapisano plik z danymi dla algorytmu bubblesort")
    print(f"Ukończono gromadzenie danych dla długości listy {l}")


def zaleznosc_n():
    data_arr = []
    for i in range(6):
        data = generate_data(1e5)
        data_arr.append(data)
    rows_var_n = [["n", "avg_time"]]
    for i in range(5, 50):
        avg_time = 0
        for j in range(6):
            start = t.time()
            new_quicksort_var_n(list(data_arr[j]), 0, len(data_arr[j]) - 1, i)
            czas = t.time() - start
            avg_time += czas
        avg_time = avg_time / 6
        avg_time_s = str(avg_time)
        avg_time_s.replace(".", ",")
        rows_var_n.append([f"{i}", avg_time_s])
        print(f"Skończono pomiar dla n = {i}")
    with open('var_n_quicksort.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows_var_n)


def optimal_quicksort():
    data_arr = []
    for i in range(4):
        le = float(f"1e{i + 3}")
        data = generate_data(le)
        data_arr.append(data)
    data_rows = [["le", "t_q", "t_q8", "t_q10"]]
    for i in range(4):
        sum_q = 0
        sum_q8 = 0
        sum_q10 = 0
        for j in range(6):
            start = t.time()
            quicksort(list(data_arr[i]), 0, len(data_arr[i]) - 1)
            czas = t.time() - start
            sum_q += czas
            start = t.time()
            new_quicksort_var_n(list(data_arr[i]), 0, len(data_arr[i]) - 1, 10)
            czas = t.time() - start
            sum_q10 += czas
            start = t.time()
            new_quicksort_var_n(list(data_arr[i]), 0, len(data_arr[i]) - 1, 8)
            czas = t.time() - start
            sum_q8 += czas
            print(f"skończono pomiar {j} dla 1e{i + 3}")
        sum_q = sum_q / 6
        sum_q8 = sum_q8 / 6
        sum_q10 = sum_q10 / 6
        t_q = str(sum_q).replace(".", ",")
        t_q8 = str(sum_q8).replace(".", ",")
        t_q10 = str(sum_q10).replace(".", ",")
        data_rows.append([len(data_arr[i]), t_q, t_q8, t_q10])
    with open('optimised.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data_rows)


pomiar(arr_e2)

