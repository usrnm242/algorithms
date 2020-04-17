from knuth_morris_pratt import kmp
from boyer_moore import boyer_moore
from rabin_karp import rabin_karp

import matplotlib.pyplot as plt
from time import time


default_pattern = "QWERTY"
default_text = "0123456QWERTYmmmmmmmQWERTY"


def print_delimiter(func):
    def printing():
        func()
        print('_' * 40, end='\n\n')
    return printing


def print_params(pattern, text):
    print("Text:", text)
    print("Pattern:", pattern)
    print()


@print_delimiter
def test_kmp():
    print("Knuth-Morris-Pratt search;")
    print_params(default_pattern, default_text)
    indices = kmp(default_pattern, default_text)
    print("indices:", indices)


@print_delimiter
def test_boyer_moore():
    print("Boyer-Moore search;")
    print_params(default_pattern, default_text)
    indices = boyer_moore(default_pattern, default_text)
    print("indices:", indices)


@print_delimiter
def test_rabin_karp():
    print("Rabin-Karp search;")
    print_params(default_pattern, default_text)
    indices = rabin_karp(default_pattern, default_text)
    print("indices:", indices)


@print_delimiter
def test_speed():
    with open("Vojna_i_mir._Tom_1.txt", 'r') as file:
        war_and_peace = file.read()

    pattern = "князь Андрей"

    start = time()
    rk_indices = rabin_karp(pattern, war_and_peace)
    end = time()
    rk_time = end - start

    start = time()
    kmp_indices = kmp(pattern, war_and_peace)
    end = time()
    kmp_time = end - start

    start = time()
    bm_indices = boyer_moore(pattern, war_and_peace)
    end = time()
    bm_time = end - start

    assert rk_indices == kmp_indices == bm_indices

    plt.bar(['Rabin-Karp', 'Knuth-Morris-Pratt', 'Boyer-Moore'],
            [rk_time, kmp_time, bm_time])
    plt.show()


if __name__ == '__main__':
    test_kmp()
    test_boyer_moore()
    test_rabin_karp()
    # test_speed()
