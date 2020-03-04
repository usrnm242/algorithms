# import avl_tree as avl
from avl_map import Map as AVLmap
from binary_tree_map import Map as BinaryMap
import binary_tree as binary
import hashmap
import matplotlib.pyplot as plt

from time import time
import numpy as np

avl_times = []
binary_times = []
hash_map_times = []


def compare_speed_of_appending(lst, plot=False):
    avl_map = AVLmap(key_T=int, val_T=int)
    # avl_tree = avl.BinaryTree()
    binary_map = BinaryMap(key_T=int, val_T=int)
    # binary_tree = binary.BinaryTree()
    hash_map = hashmap.HashMap(val_T=int, key_T=int)

    avl_time = []
    binary_time = []
    hash_map_time = []

    for i in lst:
        start = time()
        avl_map.append(i, i)
        end = time()
        avl_time.append(end - start)
        # _________________________ #
        start = time()
        binary_map.append(i, i)
        end = time()
        binary_time.append(end - start)
        # _________________________ #
        start = time()
        hash_map[i] = i
        end = time()
        hash_map_time.append(end - start)

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


def plot_appending_compare():
    for limit in range(10, 450, 10):
        lst = [i for i in range(1, limit)]
        compare_speed_of_appending(lst, plot=True)

    plt.plot(range(10, 450, 10), avl_times, label='AVL tree')
    plt.plot(range(10, 450, 10), binary_times, label='Binary tree')
    plt.plot(range(10, 450, 10), hash_map_times, label='Hash Map')
    plt.xlabel('array size')
    plt.ylabel('time')
    plt.title("Compare speed of appending increasing elements")
    plt.legend(loc='best')
    plt.show()


def compare_speed_of_search(lst):
    avl_map = AVLmap(lst, key_T=int, val_T=int)
    binary_map = BinaryMap(lst, key_T=int, val_T=int)
    hash_map = hashmap.HashMap(lst, val_T=int, key_T=int)

    avl_time = []
    binary_time = []
    hash_map_time = []

    for i in range(450):
        start = time()
        a = avl_map[i]
        end = time()
        avl_time.append(end - start)
        # _________________________ #
        start = time()
        a = binary_map[i]
        end = time()
        binary_time.append(end - start)
        # _________________________ #
        start = time()
        a = hash_map[i]
        end = time()
        hash_map_time.append(end - start)

    avl_time = np.array(avl_time)
    binary_time = np.array(binary_time)
    hash_map_time = np.array(hash_map_time)

    if True:
        avl_times.append(avl_time.mean())
        binary_times.append(binary_time.mean())
        hash_map_times.append(hash_map_time.mean())

    else:
        print("avl time mean =", avl_time.mean())
        print("binary time mean =", binary_time.mean())


def plot_search_compare(rand=False):
    for limit in range(10, 450, 10):
        lst = [(i, i) for i in range(1, limit)]
        compare_speed_of_search(lst)

    plt.plot(range(10, 450, 10), avl_times, label='AVL tree')
    plt.plot(range(10, 450, 10), binary_times, label='Binary tree')
    plt.plot(range(10, 450, 10), hash_map_times, label='Hash Map')
    plt.xlabel('array size')
    plt.ylabel('time')
    plt.title("Compare speed of searching elements")
    plt.legend(loc='best')
    plt.show()


def main():
    plot_search_compare()


if __name__ == '__main__':
    main()
