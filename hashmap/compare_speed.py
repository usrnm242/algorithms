import avl_tree as avl
import binary_tree as binary
import hashmap
from mmap import Map, SequenceTypeError
from random import randrange
import matplotlib.pyplot as plt

from time import time
import numpy as np

avl_times = []
binary_times = []
hash_map_times = []


def compare_speed(lst, plot=False):
    avl_tree = avl.BinaryTree()
    binary_tree = binary.BinaryTree()
    hash_map = hashmap.HashMap()

    avl_time = []
    binary_time = []
    hash_map_time = []

    for i in lst:
        start = time()
        avl_tree.append(i)
        end = time()
        avl_time.append(end - start)
        # _________________________ #
        start = time()
        binary_tree.append(i)
        end = time()
        binary_time.append(end - start)
        # _________________________ #
        start = time()
        hash_map[i] = i
        end = time()
        binary_time.append(end - start)

    avl_time = np.array(avl_time)
    binary_time = np.array(binary_time)
    hash_map_time = np.array(hash_map_time)

    if plot is True:
        avl_times.append(avl_time.mean())
        binary_times.append(binary_time.mean())
        hash_map_times.append(hash_map_time.mean())

    else:
        print("avl time mean =", avl_time.mean())
        print("binary time mean =", binary_time.mean())


def main():
    lst = [randrange(-1000, 1000) for _ in range(1000)]
    print("compare speed appending random elements:")

    for limit in range(10, 450, 10):
        lst = [i for i in range(1, limit)]
        compare_speed(lst, plot=True)

    # print()
    # print("compare speed appending increasing elements (from 0 to 450):")

    # for limit in range(10, 450, 10):
    #     lst = [i for i in range(1, limit)]
    #     compare_speed(lst, plot=True)

    plt.plot(range(10, 450, 10), avl_times, label='AVL tree')
    plt.plot(range(10, 450, 10), binary_times, label='Binary tree')
    plt.plot(range(10, 450, 10), hash_map_times, label='Hash Map')
    plt.xlabel('array size')
    plt.ylabel('time')
    plt.title("Compare speed of appending increasing elements")
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    main()
