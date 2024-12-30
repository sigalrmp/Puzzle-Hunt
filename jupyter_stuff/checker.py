from collections.abc import Callable
import io
from dataclasses import dataclass
from typing import Any
from contextlib import redirect_stdout


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
    user_f: Callable, correct_f: Callable, example_inputs: list[Any], real_input: Any
):
    if is_correct_on_inputs(user_f, correct_f, example_inputs):
        print(f"\033[32m{user_f(real_input)}\033[0m")
    else:
        print("\033[31mIncorrect :(\033[0m")
