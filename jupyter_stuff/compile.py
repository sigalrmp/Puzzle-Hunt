import py_compile

files = ["checker.py", "leaderboard.py", "submission.py"]

for file in files:
    py_compile.compile(file, cfile=file + "c")
