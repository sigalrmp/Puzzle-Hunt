from collections.abc import Callable
import io
from dataclasses import dataclass
from typing import Any
from contextlib import redirect_stdout
import leaderboard
import os

user = os.environ["JUPYTERHUB_USER"]


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
    user_f: Callable, correct_f: Callable, example_inputs: set[Any]
) -> bool:
    return all(
        is_correct_on_input(user_f, correct_f, input) for input in example_inputs
    )


def attempt_solution(
    puzzle_name: str,
    user_f: Callable,
    correct_f: Callable,
    example_inputs: set[Any],
    expected_real_input: Any,
    real_input: Any,
):
    example_inputs.add(expected_real_input)
    if is_correct_on_inputs(user_f, correct_f, example_inputs):
        if expected_real_input == real_input:
            leaderboard.update_leaderboard(user, puzzle_name)
            print("\033[32mCorrect!\033[0m")
        else:
            print(f"\033[31mIncorrect Input. Expected {expected_real_input}\033[0m")
        print(f"\033[32m{user_f(real_input)}\033[0m")
    else:
        print("\033[31mIncorrect :(\033[0m")
