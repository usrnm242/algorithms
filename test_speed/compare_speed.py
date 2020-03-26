# import avl_tree as avl
from avl_map import Map as AVLmap
from binary_tree_map import Map as BinaryMap
from btree_map import Map as BTreeMap
import hashmap
import matplotlib.pyplot as plt

import sys

from time import time
import numpy as np

avl_times = []
binary_times = []
hash_map_times = []
btree_map_times = []

btree_times_diff_t = []


def compare_btree_diff_t(lst, t_parameters, batch_len=10):
    length = len(lst)  # = 2000
    parts = int(length // batch_len)  # 200

    for t in t_parameters:
        btree_map = BTreeMap(t=t, key_T=int, val_T=int)

        current_btree_time = []

        for part in range(parts):
            accum_btree_map_times = []

            for batch in range(batch_len):
                i = lst[part * batch + batch]

                start = time()
                btree_map[i] = i
                end = time()
                accum_btree_map_times.append(end - start)

            current_btree_time.append(sum(accum_btree_map_times) / len(accum_btree_map_times))

        btree_times_diff_t.append(current_btree_time)

    for t, times in zip(t_parameters, btree_times_diff_t):
        plt.plot(range(0, length // batch_len), times, label=f'BTree; t={t}')
        plt.xlabel('element')
        plt.ylabel('time')
        plt.ylim(0, 0.000025)
        plt.title("Compare speed of appending increasing elements")
        plt.legend(loc='best')

    plt.show()



def compare_speed_of_appending(lst, batch_len=10, plot=False):
    avl_map = AVLmap(key_T=int, val_T=int)
    binary_map = BinaryMap(key_T=int, val_T=int)
    btree_map = BTreeMap(t=5, key_T=int, val_T=int)
    hash_map = hashmap.HashMap(val_T=int, key_T=int)


    # avl_time = []
    # binary_time = []
    # hash_map_time = []

    length = len(lst)  # = 2000
    parts = int(length // batch_len)  # 200

    for part in range(parts):
        accum_avl_times = []
        accum_binary_times = []
        accum_hash_map_times = []
        accum_btree_map_times = []

        for batch in range(batch_len):
            i = lst[part * batch + batch]

            start = time()
            avl_map.append(i, i)
            end = time()
            accum_avl_times.append(end - start)
            # _________________________ #
            start = time()
            binary_map.append(i, i)
            end = time()
            accum_binary_times.append(end - start)
            # _________________________ #
            start = time()
            hash_map[i] = i
            end = time()
            accum_hash_map_times.append(end - start)
            # _________________________ #
            start = time()
            btree_map[i] = i
            end = time()
            accum_btree_map_times.append(end - start)

        avl_times.append(sum(accum_avl_times) / len(accum_avl_times))
        binary_times.append(sum(accum_binary_times) / len(accum_binary_times))
        hash_map_times.append(sum(accum_hash_map_times) / len(accum_hash_map_times))
        btree_map_times.append(sum(accum_btree_map_times) / len(accum_btree_map_times))

    # for i in lst:
    #     start = time()
    #     avl_map.append(i, i)
    #     end = time()
    #     avl_times.append(end - start)
    #     # _________________________ #
    #     start = time()
    #     binary_map.append(i, i)
    #     end = time()
    #     binary_times.append(end - start)
    #     # _________________________ #
    #     start = time()
    #     hash_map[i] = i
    #     end = time()
    #     hash_map_times.append(end - start)
    #     # _________________________ #
    #     start = time()
    #     btree_map[i] = i
    #     end = time()
    #     btree_map_times.append(end - start)

    # avl_time = np.array(avl_time)
    # binary_time = np.array(binary_time)
    # hash_map_time = np.array(hash_map_time)


def plot_appending_compare():
    rlimit = 1000
    batch_len = 10

    lst = [i for i in range(0, rlimit)]
    compare_speed_of_appending(lst, batch_len=10)

    # plt.plot(range(0, rlimit // batch_len), avl_times, label='AVL tree map')
    # plt.plot(range(0, rlimit // batch_len), binary_times, label='Binary tree map')
    plt.plot(range(0, rlimit // batch_len), hash_map_times, label='Hash Map')
    # plt.plot(range(0, rlimit // batch_len), btree_map_times, label='BTree')
    # plt.xlim(5, 100)
    # plt.ylim(0, 0.00012)
    plt.xlabel('element')
    plt.ylabel('time')
    plt.title("Compare speed of appending increasing elements")
    plt.legend(loc='best')
    plt.show()


def main():
    sys.setrecursionlimit(8000)
    plot_appending_compare()
    lst = [i for i in range(0, 1000)]
    # compare_btree_diff_t(lst, t_parameters=[5, 10, 15])



if __name__ == '__main__':
    main()
