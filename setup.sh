#!/usr/bin/env bash

# Author = dAYOShACKER505
# Aim = To create STRONG passwords and protect from hackers
# VERSION = 1.0

# NOTE: USE THIS TOOL  ONLY FOR EDUCATIONAL PURPOSE 

clear
echo -ne "Installation Begins ###"
for i in 1 2 3 4 5
do
    echo -ne "#"
    sleep 0.5
done
echo -e "\n"

echo "Checking for system update"
apt update && apt upgrade -y

echo -e "\n"

echo "Checking for python and it's updates"
sleep 0.5
apt-get install python -y
sleep 0.5
python3 -m pip install --upgrade pip

echo -e "\n"
sleep 0.5
echo "Checking for Required Python Pakages"
sleep 1
pip install -r requirements.txt

sleep 0.5

echo "Installation Completed"
echo  "Type python mahakal.py"

