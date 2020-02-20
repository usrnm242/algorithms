def catalan_generator(left, right):
    length = L = R = 0

    if left == right == 0:
        length = 1

    if left != 0:
        L = catalan_generator(left - 1, right)

    if left < right:
        R = catalan_generator(left, right - 1)

    return length + L + R


def generate_catalan_num(n):
    return catalan_generator(n, n)


def f(n, arr):
    # печатаем нулевую последовательность
    print(arr)
    while True:
        ind = n - 1
        cnt = 0
        while ind >= 0:
            if arr[ind] == ')':
                cnt -= 1
            if arr[ind] == '(':
                cnt += 1
            if cnt < 0 and arr[ind] == '(':
                break
            ind -= 1
        # если не нашли, то алгоритм заканчивает работу
        if ind < 0:
            break
        # заменяем на закр. скобку
        arr[ind] = ')'
        # заменяем на самую лексикографическую минимальную
        for i in range(ind + 1, n):
            if i <= (n - ind + cnt) / 2 + ind:
                arr[i] = '('
            else:
                arr[i] = ')'
        print(arr)


if __name__ == '__main__':
    # n = 6
    # arr = ['(' for _ in range(n // 2)] + [')' for _ in range(n // 2)]
    # f(n, arr)
    for n in range(0, 20):
        catalan_num = generate_catalan_num(n)
        print(n, catalan_num, sep=' - ')


