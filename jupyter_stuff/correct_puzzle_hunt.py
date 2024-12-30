import checker


def puzzle_1(var_int):
    return chr(var_int + 3)


def run_puzzle_1(f, input):
    checker.attempt_solution(f, puzzle_1, [10, 2, 83], input)
