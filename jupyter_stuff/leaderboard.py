import socket
import os
from typing import Dict, Tuple, Set
from tabulate import tabulate

LEADERBOARD_PORT = 8100


def encode_msg(name: str, puzzle_completed: str) -> str:
    name_len = len(name)
    return str(name_len) + " " + name + puzzle_completed


def decode_msg(msg) -> Tuple[str, str]:
    name_len_idx = msg.find(" ")
    name_len = int(msg[:name_len_idx])
    rest_of_msg = msg[name_len_idx + 1 :]
    return rest_of_msg[:name_len], rest_of_msg[name_len:]


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def display_leaderboard(puzzles_completed: Dict[str, Set[str]]) -> None:
    leaderboard = [
        [name, len(individual_puzzles_completed)]
        for name, individual_puzzles_completed in puzzles_completed.items()
    ]
    headers = ["Group Name", "Puzzles Completed"]
    clear_screen()
    print(tabulate(leaderboard, headers=headers, tablefmt="simple"))


def run_learboard_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", LEADERBOARD_PORT))
    server.listen(1)

    puzzles_completed: Dict[str, Set[str]] = {}

    while True:
        display_leaderboard(puzzles_completed)
        conn, _add = server.accept()
        data = conn.recv(1024).decode()
        conn.close()
        name, puzzle_completed = decode_msg(data)
        if name not in puzzles_completed:
            puzzles_completed[name] = set()
        puzzles_completed[name].add(puzzle_completed)


def update_leaderboard(name: str, puzzle_completed: str):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("host.docker.internal", LEADERBOARD_PORT))
    client.send(encode_msg(name, puzzle_completed).encode())
    client.close()


if __name__ == "__main__":
    run_learboard_server()