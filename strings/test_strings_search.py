from knuth_morris_pratt import kmp
from boyer_moore import boyer_moore
from rabin_karp import rabin_karp
from aho_corasick import Automaton

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
    indices = rabin_karp([default_pattern], default_text)
    print("indices:", indices)


@print_delimiter
def test_aho_korasik():
    print("Aho Korasik search;")
    print_params(default_pattern, default_text)
    A = Automaton([default_pattern])
    indices = A.search_in(default_text)
    print("indices:", indices)


def test_speed():
    """long execution"""
    with open("Vojna_i_mir._Tom_1.txt", 'r') as file:
        war_and_peace = file.read()

    print(len(war_and_peace))  # 2989848

    limits = range(10, len(war_and_peace), 50000)

    pattern1 = "князь Андрей"
    pattern2 = " Болконский "
    pattern3 = "простумитесь"

    rk_times = []
    aho_times = []

    for limit in limits:
        start = time()
        rk_indices = rabin_karp([pattern1, pattern2, pattern3], war_and_peace)
        end = time()
        rk_time = end - start
        rk_times.append(rk_time)

        #, pattern2, pattern3, pattern4])
        start = time()
        A = Automaton([pattern1, pattern2, pattern3])
        aho_indices = A.search_in(war_and_peace)
        end = time()
        aho_time = end - start
        aho_times.append(aho_time)

        assert rk_indices == aho_indices

    # plt.bar(['Rabin-Karp', "Aho-Korasik"], [rk_time, aho_time])
    plt.plot(limits, rk_times, label='Rabin-Karp')
    plt.plot(limits, aho_times, label='Aho-Korasick')
    plt.legend()
    plt.title('Searching patterns in "War and peace"')
    plt.show()


def test_speed_barplot():
    with open("Vojna_i_mir._Tom_1.txt", 'r') as file:
        war_and_peace = file.read()

    pattern1 = "князь Андрей"
    pattern2 = " Болконский "
    pattern3 = "простумитесь"

    start = time()
    rk_indices = rabin_karp([pattern1, pattern2, pattern3], war_and_peace)
    end = time()
    rk_time = end - start

    start = time()
    A = Automaton([pattern1, pattern2, pattern3])
    aho_indices = A.search_in(war_and_peace)
    end = time()
    aho_time = end - start

    assert rk_indices == aho_indices

    plt.bar(['Rabin-Karp', "Aho-Korasik"], [rk_time, aho_time])
    plt.show()


if __name__ == '__main__':
    test_kmp()
    test_boyer_moore()
    test_rabin_karp()
    test_aho_korasik()
    # test_speed()
    test_speed_barplot()
