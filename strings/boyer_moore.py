def boyer_moore(pattern: str, text: str):
    text: str = str(text)
    pattern: str = str(pattern)
    text_len: int = len(text)
    pattern_len: int = len(pattern)

    positions = []

    for i in range(text_len - pattern_len + 1):
        mismatch_index = _mismatch_in_text(i, pattern_len, pattern, text)

        if mismatch_index == -1:
            positions.append(i)

        else:
            match_index = _match_in_pattern(text[mismatch_index],
                                            pattern_len,
                                            pattern)
            i = (mismatch_index - match_index)

    return positions


def _match_in_pattern(char, pattern_len, pattern) -> int:
    for i in range(pattern_len - 1, -1, -1):
        if char == pattern[i]:
            return i
    return -1


def _mismatch_in_text(current_pos, pattern_len, pattern, text) -> int:
    for i in range(pattern_len - 1, -1, -1):
        if pattern[i] != text[current_pos + i]:
            return current_pos + i
    return -1


if __name__ == '__main__':
    text = "ABAABA"
    pattern = "ABA"
    positions = boyer_moore(pattern, text)

    if len(positions) == 0:
        print("No match found")
    else:
        print("Pattern found in following positions: ")
        print(positions)
