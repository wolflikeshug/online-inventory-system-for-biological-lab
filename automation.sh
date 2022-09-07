#! /bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3.10-venv -y
sudo apt update
sudo apt upgrade -y
sudo apt install git python3.10 python3-pip -y
python3 -m pip3 install --upgrade pip
git clone https://github.com/wolflikeshug/CITS3200-repo.git ~/CITS3200-repo
pip3 install -r ~/CITS3200-repo/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 wsgi.py