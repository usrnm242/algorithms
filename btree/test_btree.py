import random
import btree_map

random.seed(0)


def main():
    rand_lst = [random.randint(-5, 5) for _ in range(5)]

    sequence = [(i, f"string[{i}]") for i in rand_lst]

    print("sequence is", sequence, end='\n\n')

    mmap = btree_map.Map(sequence, t=5)

    print("map is", mmap, "\ninserting new value: ", end='')

    mmap[10] = "TEST"  # inserting new value

    print(mmap, "\nchanging value by key=10: ", end='')
    mmap[10] = "NEW_TEST_VALUE"  # changing value

    print(mmap, "\ndeleting value by key=10: ", end='')
    del mmap[10]

    print(mmap)

    print()

    print("Iteraring:")

    for i in mmap:
        print(i)

    print()

    print("is map empty:", mmap.is_empty())

    empty_map = btree_map.Map(key_T='str', val_T='int')

    print("init new empty map. Is new map empty:", empty_map.is_empty())

    if btree_map.KeyValue(1, "string[1]") in mmap:
        print("map contains pair 1, 'string[1]'")
    else:
        print("map doesnt contains pair 1, 'string[1]'")

    if (2, "string[2]") in mmap:
        print("map contains pair 2, 'string[2]'")
    else:
        print("map doesn't contains pair 2, 'string[2]'")


if __name__ == '__main__':
    main()
