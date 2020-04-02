import random
import btree_map

random.seed(7)


def main():
    rand_lst = [random.randint(-5, 5) for _ in range(5)]

    arr = [(i, f"string[{i}]") for i in rand_lst]

    print("array is", arr, end='\n\n')

    map_btree = btree_map.Map(arr, t=5)

    print("map is", map_btree, "with t = 5\n")

    print(len(map_btree), "is len of map\n")

    key = 17
    val = "TEST"

    print(f"inserting value ({key}: {val}): ", end='')
    map_btree[key] = val  # inserting new value

    print(map_btree, f"\nchanging value by key={key}: ", end='')
    map_btree[key] = "NEW_TEST_VALUE"  # changing value

    print(map_btree, f"\ndeleting value by key={key}: ", end='')
    del map_btree[key]

    print(map_btree)

    print("getting value by key = -1:", map_btree[-1])

    print()

    print("Iterating:")

    for i in map_btree:
        print(i)

    print()

    print("is map empty:", map_btree.is_empty())

    if (-5, "string[-5]") in map_btree:
        print("map contains pair 2, 'string[2]'")
    else:
        print("map doesn't contain pair 2, 'string[2]'")

    if -1 in map_btree:
        print("map contains key '-1'")
    else:
        print("map doensn't contain key '-1'")

    print('_' * 40)
    print()

    rand_lst = [random.randint(-10000, 10000) for _ in range(0, 10**4)]
    arr = [(i, f"string[{i}]") for i in rand_lst]
    map_btree = btree_map.Map(arr, t=5)

    print(len(map_btree), "is len of map. there are repeating elements\n")

    for i in range(-10000, 1):
        if i in map_btree:
            del map_btree[i]

    print(len(map_btree), "is len of map after deleting by keys 10000 < key < 0")

    map_btree = None  # delete all tree :)


if __name__ == '__main__':
    main()
