import avl_tree as avl
import binary_tree as binary
from avl_map import Map, SequenceTypeError
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


def main():
    test_tree()
    test_mmap()


if __name__ == '__main__':
    main()
