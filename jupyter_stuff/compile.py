import py_compile

files = ["checker.py", "leaderboard.py", "correct_puzzle_hunt.py"]

for file in files:
    py_compile.compile(file, cfile=file + "c")
