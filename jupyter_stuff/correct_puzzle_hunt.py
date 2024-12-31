import checker


def run_puzzle_1(f, input):
    def puzzle_1(var_int):
        return chr(var_int + 3)

    checker.attempt_solution("puzzle_1", f, puzzle_1, {2, 83}, 10, input)
