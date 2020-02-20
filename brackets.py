def brackets_generator(left, right, string):
    lst = []

    if left == right == 0:
        lst.append(string)

    if left != 0:
        L = brackets_generator(left - 1, right, string + '(')
        lst.extend(L)

    if left < right:
        R = brackets_generator(left, right - 1, string + ')')
        lst.extend(R)

    return lst


def generate_brackets(n):
    return brackets_generator(n, n, "")


def brackets_iterative_generation(n, string):
    lst = []
    lst.append(string)

    while True:
        ind = 2 * n - 1
        print(ind)
        cnt = 0
        # находим откр. скобку, которую можно заменить
        while ind >= 0:
            if string[ind] == ')':
                cnt -= 1
            if string[ind] == '(':
                cnt += 1
            if cnt < 0 and string[ind] == '(':
                break
            ind -= 1
        # если не нашли, то алгоритм заканчивает работу
        if ind < 0:
            break
        # заменяем на закр. скобку
        string[ind] = ')'
        # заменяем на самую лексикографическую минимальную
        for i in range(ind + 1, n):
            if i <= (n - ind + cnt) / 2 + ind:
                string[i] = '('
            else:
                string[i] = ')'

        lst.append(string)

    return lst


def iteratively_generate_brackets(n) -> list:
    start_str = '(' * n + ')' * n
    return brackets_iterative_generation(n, start_str)


if __name__ == '__main__':
    n = 6
    brackets = iteratively_generate_brackets(n)
    print(brackets)
    # brackets = generate_brackets(n)
    # print(brackets, len(brackets),
    #       len(brackets) == len(set(brackets)), sep='\n')
