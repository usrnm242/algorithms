def kmp(pattern: str, text: str) -> list:
    """
    Returns
        list of pattern indices start in text
        or [] if not
    """
    pattern = str(pattern)
    text = str(text)

    pattern_len = len(pattern)
    text_len = len(text)

    failure: list = __get_failure_array(pattern)

    matches_indices = []

    pattern_idx = 0
    for text_idx in range(text_len):
        while pattern_idx and text[text_idx] != pattern[pattern_idx]:
            pattern_idx = failure[pattern_idx - 1]

        if text[text_idx] == pattern[pattern_idx]:
            pattern_idx += 1

            if pattern_idx == pattern_len:
                matches_indices.append(text_idx - pattern_len + 1)
                pattern_idx = failure[pattern_idx - 1]

    return matches_indices


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
    pattern = "QWERTY"
    text = "0123456QWERTYmmmmmmmQWERTY"
    a = kmp(pattern, text)
    print(a)
    # print(text[start:end])
