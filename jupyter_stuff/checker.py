from collections.abc import Callable
import io
from dataclasses import dataclass
from typing import Any
from contextlib import redirect_stdout


@dataclass
class TestCase:
    input: Any
    output: Any


def is_correct_on_input(user_f: Callable, correct_f: Callable, input: Any):
    with redirect_stdout(io.StringIO()):
        correct_output = correct_f(input)
        their_output = user_f(input)
    return correct_output == their_output


def verify_function(user_f: Callable, correct_f: Callable, example_inputs: list[Any]):
    return all(
        is_correct_on_input(user_f, correct_f, input) for input in example_inputs
    )
