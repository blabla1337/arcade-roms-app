#!/bin/bash

# Function to automatically accept SSH fingerprint
ssh-keyscan -H batocera.local >> ~/.ssh/known_hosts

# SSH into the remote machine and run commands
ssh root@batocera.local <<'ENDSSH'
    # Download and run the get-pip.py script
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 

    # Install Flask
    pip3 install flask

    # remove old instance if exits
    rm -rf arcade-roms-app-main/
    rm arcade-roms-app.zip

    # Download the arcade-roms-app repository and run the app
    wget https://github.com/blabla1337/arcade-roms-app/archive/refs/heads/main.zip -O arcade-roms-app.zip
    unzip arcade-roms-app.zip
    cd arcade-roms-app-main/iconicarcade
    python3 app.py
ENDSSH