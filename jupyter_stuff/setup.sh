#!/bin/bash

sudo yum install python pip
sudo pip install jupyterlab jupyterhub dockerspawner jupyterhub-dockerspawner 
pip install tabulate

sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl start docker

sudo pip install --upgrade docker --user

curl -sL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo yum install -y nodejs
sudo npm install -g configurable-http-proxy

sudo docker network create jupyterhub
