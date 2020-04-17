from collections import deque


class Automaton:
    def __init__(self, patterns):
        self.adlist = list()
        self.adlist.append(
            {"value": "", "next_states": [], "fail_state": 0, "output": []})

        for pattern in patterns:
            self.add_pattern(pattern)

        self.set_fail_transitions()

        self.indices = {pattern: [] for pattern in patterns}

    def find_next_state(self, current_state, char):
        for state in self.adlist[current_state]["next_states"]:
            if char == self.adlist[state]["value"]:
                return state

        return None

    def add_pattern(self, pattern):
        current_state = 0

        for character in pattern:
            if self.find_next_state(current_state, character):
                current_state = self.find_next_state(current_state, character)

            else:
                self.adlist.append({"value": character,
                                    "next_states": [],
                                    "fail_state": 0,
                                    "output": []})

                self.adlist[current_state]["next_states"].append(len(self.adlist) - 1)
                current_state = len(self.adlist) - 1

        self.adlist[current_state]["output"].append(pattern)

    def set_fail_transitions(self):
        q = deque()

        for node in self.adlist[0]["next_states"]:
            q.append(node)
            self.adlist[node]["fail_state"] = 0

        while q:
            r = q.popleft()

            for child in self.adlist[r]["next_states"]:
                q.append(child)
                state = self.adlist[r]["fail_state"]

                while (
                    self.find_next_state(state, self.adlist[child]["value"]) is None
                    and state != 0
                ):
                    state = self.adlist[state]["fail_state"]

                self.adlist[child]["fail_state"] = \
                    self.find_next_state(state, self.adlist[child]["value"])

                if self.adlist[child]["fail_state"] is None:
                    self.adlist[child]["fail_state"] = 0

                self.adlist[child]["output"] = (self.adlist[child]["output"] + \
                    self.adlist[self.adlist[child]["fail_state"]]["output"])

    def search_in(self, string):
        current_state = 0

        for i in range(len(string)):
            while (self.find_next_state(current_state, string[i]) is None
                   and current_state != 0):
                current_state = self.adlist[current_state]["fail_state"]

            current_state = self.find_next_state(current_state, string[i])

            if current_state is None:
                current_state = 0

            else:
                for key in self.adlist[current_state]["output"]:
                    if not (key in self.indices):
                        self.indices[key] = []

                    self.indices[key].append(i - len(key) + 1)

        return self.indices


if __name__ == "__main__":
    A = Automaton(["QWERTY", "mm"])
    res = A.search_in("QWERTYmmmmQWERTYmmmmmmQWERTY")
    print(res)
