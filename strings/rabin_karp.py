# -*- coding: utf-8 -*-

alphabet_size = 256
modulus = 1000003


def rabin_karp(pattern: str, text: str) -> list:
    """
    Returns
        list of indices of pattern in the text
        if not found returns []
    """

    pattern = str(pattern)
    text = str(text)

    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len > text_len:
        return -1

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    matches = []

    # calculating hash of pattern and substring of text
    for i in range(pattern_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == pattern_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, text_len - pattern_len + 1):
        if text_hash == p_hash and text[i:i + pattern_len] == pattern:
            matches.append(i)
            # return i
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
    index = rabin_karp(pattern, text)
    print("index is", index)
    # print("text starting from match:", text[index:], '\n')

if __name__ == "__main__":
    test_rabin_karp()
