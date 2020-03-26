import hashmap

hm = hashmap.HashMap([('1', 0), ('2', 0), ('3', 0)],
                     load_factor=2.0,
                     hash_func=lambda x: hash(str(x)))

print('_' * 40)

hm['4'] = 123  # appending new value
hm['4'] = 100  # changing old value

for i in hm:
    print(i)

print('_' * 40)

try:
    hm[123] = 456
except hashmap.SequenceTypeError:
    print("\nSequenceTypeError\n")

for i in range(15):
    hm[f'{i}'] = i * 2

for i in hm:
    print(i)

del hm['4']  # deleting

print("\ncurrent load factor is", hm.current_load_factor())

print("changing load factor; \ncalling func with setting load factor = 0.72")

hm.change_load_factor(0.72)  # we can use any value

print("current load factor is", hm.current_load_factor())

print('_' * 40)

for i in hm:
    print(i)

print('_' * 40)

print("number of elements is", hm.number_of_elements)
