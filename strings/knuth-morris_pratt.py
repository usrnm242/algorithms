def kmp(pattern: str, text: str) -> 'tuple | -1':
    """
    Returns
        tuple (start_index, end_index)
        of -1 if not found
    """
    pattern = str(pattern)
    text = str(text)

    pattern_len = len(pattern)
    text_len = len(text)

    failure: list = __get_failure_array(pattern)

    text_idx, pattern_idx = 0, 0  # index into text, pattern
    while text_idx < text_len:
        if pattern[pattern_idx] == text[text_idx]:
            if pattern_idx == (pattern_len - 1):
                return (text_idx + 1 - pattern_len, text_idx + 1)
            pattern_idx += 1

        # if it is prefix in pattern
        # go back enough to continue
        elif pattern_idx > 0:
            pattern_idx = failure[pattern_idx - 1]
            continue
        text_idx += 1
    return -1


def __get_failure_array(pattern: str) -> list:
    """
    calc new index we should go to if we fail a comparison
    """
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure


if __name__ == "__main__":
    # Test 1)
    pattern = "QWERTY"
    text = "0123456QWERTYmmmmmmm"
    start, end = kmp(pattern, text)
    print(text[start:end])
