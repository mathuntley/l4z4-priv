"""
Moduł zawierający funkcje wykorzystane w realizacji poleceń zadania 4
"""

'''
author: Mikołaj Kikolski
date: 04.05.2021
'''


def tab_split(tab, start, end):

    """
    Funkcja podziału tablicy dla funkcji quicksort()
    """

    split_val = tab[end]
    i = start
    for j in range(start, end):
        if tab[j] < split_val:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
    tab[i], tab[end] = tab[end], tab[i]
    return i


def quicksort(tab, lp, rp):
    """
    Funkcja implementująca algorytm sortowania szybkiego przedstawiony na wykładzie

    Parameters
    ----------
    tab : list of ints
        tablica do posortowania
    lp, rp : int
        początek i koniec zakresu sortowania

    Returns
    -------
    list of ints
        posortowana tablica
    """
    if lp < rp:
        mid = tab_split(tab, lp, rp)
        quicksort(tab, lp, mid - 1)
        quicksort(tab, mid + 1, rp)


def bubble_sort(tab):
    """
    Implementacja algorytmu sortowania bąbelkowego, z funkcją pomocniczą swap(a, b)

    Parameters
    ----------
    tab : list of ints
        Tablica z nieuporządkowanymi liczbami całkowitymi

    Returns
    -------
    list of ints
        Zwraca przekształconą, uporządkowaną tablicę wejściową
    """
    czy_byla_podmiana = True

    do_sortowania = len(tab)

    while czy_byla_podmiana == True and do_sortowania > 1:
        czy_byla_podmiana = False
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                czy_byla_podmiana = True
        do_sortowania -= 1
    return tab


def new_quicksort(tab, lp, rp):
    """
    Funkcja implementująca, zgodnie z poleceniem zad 4, usprawniony algorytm sortowania szybkiego
    dla list o długości mniejszej niż 10

    Parameters
    ----------
    tab : list of ints
        tablica do posortowania
    lp, rp : int
        początek i koniec zakresu sortowania

    Returns
    -------
    list of ints
        posortowana tablica
    """
    if lp < rp:
        if rp - lp > 10:
            mid = tab_split(tab, lp, rp)
            quicksort(tab, lp, mid - 1)
            quicksort(tab, mid + 1, rp)
        else:
            do_sortowania = 10
            for i in range(do_sortowania - 1):
                for j in range(do_sortowania - i - 1):
                    if tab[j] > tab[j + 1]:
                        tab[j], tab[j + 1] = tab[j + 1], tab[j]


def new_quicksort_var_n(tab, lp, rp, n):
    if lp < rp:
        if rp - lp > n:
            mid = tab_split(tab, lp, rp)
            new_quicksort_var_n(tab, lp, mid - 1, n)
            new_quicksort_var_n(tab, mid + 1, rp, n)
        else:
            do_sortowania = n
            for i in range(do_sortowania - 1):
                for j in range(do_sortowania - i - 1):
                    if tab[j] > tab[j + 1]:
                        tab[j], tab[j + 1] = tab[j + 1], tab[j]

