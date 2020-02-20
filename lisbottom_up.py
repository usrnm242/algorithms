def lis_bottom_up(values):
    d = []
    for i in range(len(values)):
        d.append(1)
        for j in range(i):
            if values[i] % values[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    print(d)
    new_values = []
    length = curr = max(d)

    i = len(d) - 1
    j = -1
    while i >= 0:
        if d[i] == curr and values[i] <= values[j]:
            new_values.append(values[i])
            curr = d[i]
            j += 1
        i -= 1
    return length, new_values


def main():
    no_matter = int(input())
    values = list(map(int, input().split()))
    length = lis_bottom_up(values)
    print(length)


if __name__ == '__main__':
    main()