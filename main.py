from typing import List


class StateException(Exception):
    ...


class ParserException(Exception):
    ...


class State:

    def __init__(self, remainders: dict = None):
        if remainders is None:
            remainders = {}
        self.remainders = remainders

    def set_value(self, pos: int, value: int):
        if pos not in self.remainders:
            self.remainders[pos] = value
        self.remainders[pos] = min(self.remainders[pos], value)

    def items(self):
        return self.remainders.items()

    def concatenate(self, s: 'State', k: int) -> 'State':
        result = State()

        for remainder, value in self.items():
            for s_remainder, s_value in s.items():
                result.set_value((remainder + s_remainder) % k, value + s_value)

        return result

    def multiply(self, s: 'State') -> 'State':
        result = State()

        for remainder, value in self.items():
            result.set_value(remainder, value)

        for remainder, value in s.items():
            result.set_value(remainder, value)

        return result

    def star(self, k: int) -> 'State':
        if not self.remainders.keys():
            raise StateException('State is empty. You cannot use star.')

        items = []

        for remainder, value in self.items():
            for cnt in range(0, k):
                weight = (remainder * cnt) % k
                cost = value * cnt
                items.append((weight, cost))

        dp = [['INF' for i in range(len(items))] for j in range(len(items))]

        for index, item in enumerate(items):
            dp[index][item[0]] = item[1]

        for i in range(1, len(items)):
            weight = items[i][0]
            cost = items[i][1]
            for w in range(len(items)):
                if dp[i - 1][w] != 'INF':
                    dp[i][w] = dp[i - 1][w]
            for w in range(weight, len(items)):
                if dp[i - 1][w - weight] != 'INF':
                    if dp[i][w] == 'INF' or dp[i][w] > dp[i - 1][w - weight] + cost:
                        dp[i][w] = dp[i - 1][w - weight] + cost

        result = State()

        for i in range(len(items)):
            for j in range(len(items)):
                if dp[i][j] != 'INF':
                    result.set_value(j % k, dp[i][j])

        return result

    def fetch_answer(self, pos: int):
        if pos not in self.remainders:
            return 'INF'
        return self.remainders[pos]


class Parser:

    def __init__(self, regular: str, k: int):
        self.regular = regular
        self.k = k
        self.final_state = None

    def _calc(self) -> State:
        stack: List[State] = []
        regular = self.regular

        for c in regular:
            try:
                if c in 'abc':
                    stack.append(State({1: 1}))
                elif c == '1':
                    stack.append(State({0: 0}))
                elif c == '*':
                    current_state = stack.pop()
                    stack.append(current_state.star(self.k))
                elif c == '+':
                    first_state = stack.pop()
                    second_state = stack.pop()
                    stack.append(first_state.multiply(second_state))
                elif c == '.':
                    first_state = stack.pop()
                    second_state = stack.pop()
                    stack.append(first_state.concatenate(second_state, self.k))
            except Exception as e:
                raise ParserException(f"Error occurred while parsing regular expression: {repr(e)}")

        if len(stack) == 1:
            return stack[0]
        else:
            raise ParserException("Error occurred while parsing regular expression")

    def get_answer(self, pos: int):
        if self.final_state is None:
            self.final_state = self._calc()

        return self.final_state.fetch_answer(pos)


if __name__ == '__main__':
    input_data = input().split()
    regular = input_data[0]
    k = int(input_data[1])
    print(Parser(regular, k).get_answer(int(input_data[2])))
