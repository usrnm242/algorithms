# -*- coding: utf-8 -*-

alphabet_size = 256
modulus = 1000003


def rabin_karp(patterns: list, text: str) -> list:
    """
    Returns
        list of indices of pattern in the text
        if not found returns []
    """

    text = str(text)

    pattern_len = len(patterns[0])
    text_len = len(text)

    matches = {pattern: [] for pattern in patterns}

    if pattern_len > text_len:
        return matches

    p_hash = 0
    p_hashes = [0 for _ in range(len(patterns))]
    text_hash = 0
    modulus_power = 1

    #[[] for _ in range(len(patterns))]

    # calculating hash of pattern and substring of text
    for i in range(pattern_len):
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus

        for p_idx, pattern in enumerate(patterns):
            p_hashes[p_idx] = (ord(pattern[i]) + p_hashes[p_idx] * alphabet_size) % modulus

        if i == pattern_len - 1:
            continue

        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, text_len - pattern_len + 1):
        for p_idx, pattern in enumerate(patterns):
            if text_hash == p_hashes[p_idx] and text[i:i + pattern_len] == pattern:
                matches[pattern].append(i)

        if i == text_len - pattern_len:
            continue
        # rolling hash
        text_hash = (
            (text_hash - ord(text[i]) * modulus_power) * alphabet_size +
            ord(text[i + pattern_len])
            ) % modulus

    return matches


def test_rabin_karp():
    pattern = "QWERTY"
    text = "QWERTYmmmmQWERTYmmmmmmQWERTY"
    print("\ntext:", text)
    print("pattern:", pattern)
    index = rabin_karp([pattern], text)
    print("index is", index)
    # print("text starting from match:", text[index:], '\n')


if __name__ == "__main__":
    test_rabin_karp()
