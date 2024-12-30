#!/bin/bash

sudo yum install python pip
pip install jupyterlab jupyterhub dockerspawner

sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl start docker

curl -sL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo yum install -y nodejs
sudo npm install -g configurable-http-proxy
