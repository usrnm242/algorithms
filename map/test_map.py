import avl_tree as avl
import binary_tree as binary
from mmap import Map, SequenceTypeError
from random import randrange
import matplotlib.pyplot as plt

from time import time
import numpy as np


def test_tree():
    print("testing just AVL tree:")

    lst = [1, -1, 0, 2, 5, -10]

    print("sequence is", lst)

    tree = avl.BinaryTree()

    for i in lst:
        tree.append(i)

    print("iterating: ")
    for i in tree:
        print(i, end=' ')

    print('\n')

    print("iterating (used python's map to change values): ")
    for i in map(lambda x: x * 2, tree):
        print(i, end=' ')

    print('\n', '_' * 40, '\n', sep='', end='\n')


def test_mmap():
    print("testing map:")

    lst = [(1, "val1"), (2, "val2"), (3, "val3"), (-1, "val-1")]
    print("Sequence is", lst)

    # init map with specifying types
    # it doesn't necessary to specify types
    mmap = Map(lst, key_T=int, val_T=str)

    print("\nTrying to append element (4, -10):")
    try:
        mmap.append(4, -10)
    except SequenceTypeError:  # defined in mmap.py
        print("SequenceTypeError")

    print("\nappending element (55, 'aaa')")
    mmap.append(55, "aaa")

    idx = 55

    print(f"\nchecking what value with key = {idx}:")
    print(f"key = {idx}; value = {mmap[idx]}")

    print(f"\nchanging value with key = {idx} from 'aaa' to 'zero':")
    mmap[idx] = 'zero'

    print(f"\nchecking what value with key = {idx}:")
    print(f"key = {idx}; value = {mmap[idx]}; value type = {type(mmap[idx])}")

    print("\nnow iterating:")
    for value in mmap:
        print(value)


avl_times = []
binary_times = []


def compare_speed(lst, plot=False):
    avl_tree = avl.BinaryTree()
    binary_tree = binary.BinaryTree()

    avl_time = []
    binary_time = []

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

    avl_time = np.array(avl_time)
    binary_time = np.array(binary_time)

    if plot is True:
        avl_times.append(avl_time.mean())
        binary_times.append(binary_time.mean())
    else:
        print("avl time mean =", avl_time.mean())
        print("binary time mean =", binary_time.mean())
        print("is avl time mean < binary time mean:", avl_time.mean() < binary_time.mean())


def main():
    test_tree()
    test_mmap()
    lst = [randrange(-1000, 1000) for _ in range(1000)]
    print("compare speed appending random elements:")
    compare_speed(lst)

    print()
    print("compare speed appending increasing elements (from 0 to 1000):")
    for limit in range(10, 450, 10):
        lst = [i for i in range(1, limit)]
        compare_speed(lst, plot=True)

    plt.plot(range(10, 450, 10), avl_times, label='AVL tree')
    plt.plot(range(10, 450, 10), binary_times, label='Binary tree')
    plt.xlabel('array size')
    plt.ylabel('time')
    plt.title("Compare speed of appending increasing elements")
    plt.legend(loc='best')
    plt.show()





if __name__ == '__main__':
    main()
