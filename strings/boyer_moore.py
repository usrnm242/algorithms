class BoyerMooreSearch:
    def __init__(self, text: str, pattern: str):
        self.text: str = str(text)
        self.pattern: str = str(pattern)
        self.text_len: int = len(text)
        self.pattern_len: int = len(pattern)

    def search(self) -> list:
        return self._bad_character_heuristic()

    def _match_in_pattern(self, char) -> int:
        for i in range(self.pattern_len - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1

    def _mismatch_in_text(self, current_pos) -> int:
        for i in range(self.pattern_len - 1, -1, -1):
            if self.pattern[i] != self.text[current_pos + i]:
                return current_pos + i
        return -1

    def _bad_character_heuristic(self) -> list:
        # searches pattern in text and returns index positions
        positions = []

        for i in range(self.text_len - self.pattern_len + 1):
            mismatch_index = self._mismatch_in_text(i)

            if mismatch_index == -1:
                positions.append(i)

            else:
                match_index = self._match_in_pattern(self.text[mismatch_index])
                i = (mismatch_index - match_index)
                # shifting index lgtm [py/multiple-definition]

        return positions


if __name__ == '__main__':
    text = "ABAABA"
    pattern = "ABA"
    bms = BoyerMooreSearch(text, pattern)
    positions = bms.search()

    if len(positions) == 0:
        print("No match found")
    else:
        print("Pattern found in following positions: ")
        print(positions)
