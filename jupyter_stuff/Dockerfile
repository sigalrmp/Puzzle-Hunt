
# Dockerfile
FROM jupyter/base-notebook:latest

RUN pip install --upgrade jupyterhub==5.2.1

COPY --chown=jovyan:users  Coding_Puzzle_Hunt.ipynb /home/jovyan/work/
