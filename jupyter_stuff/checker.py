from collections.abc import Callable
import io
from dataclasses import dataclass
from typing import Any
from contextlib import redirect_stdout
import leaderboard


@dataclass
class TestCase:
    input: Any
    output: Any


def is_correct_on_input(user_f: Callable, correct_f: Callable, input: Any) -> bool:
    with redirect_stdout(io.StringIO()):
        correct_output = correct_f(input)
        their_output = user_f(input)
    return correct_output == their_output


def is_correct_on_inputs(
    user_f: Callable, correct_f: Callable, example_inputs: list[Any]
) -> bool:
    return all(
        is_correct_on_input(user_f, correct_f, input) for input in example_inputs
    )


def attempt_solution(
    username: str,
    puzzle_name: str,
    user_f: Callable,
    correct_f: Callable,
    example_inputs: list[Any],
    real_input: Any,
):
    if is_correct_on_inputs(user_f, correct_f, example_inputs):
        leaderboard.update_leaderboard(username, puzzle_name)
        print(f"\033[32m{user_f(real_input)}\033[0m")
    else:
        print("\033[31mIncorrect :(\033[0m")
