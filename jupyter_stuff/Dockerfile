
# Dockerfile
FROM jupyter/base-notebook:latest

RUN pip install --upgrade jupyterhub==5.2.1
RUN pip install tabulate

COPY --chown=jovyan:users  Coding_Puzzle_Hunt.ipynb /home/jovyan/work/
COPY --chown=jovyan:users  checker.py /home/jovyan/work/
COPY --chown=jovyan:users  submission.py /home/jovyan/work/
COPY --chown=jovyan:users  compile.py /home/jovyan/work/
COPY --chown=jovyan:users  leaderboard.py /home/jovyan/work/

