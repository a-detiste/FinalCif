#!/bin/bash

# Ubuntu installer script
#
# This script either installs FinalCif vom the source repository or simply runs FinalCif.
# Prior to installation, a recent Python version is needed.
#
# Commandline Options:
#
# ./finalcif-start.sh [-option]
#
# -pyinst  :  Adds a Python repository (deadsnakes) and installs Python3.9
# -install :  Install FinalCif from GitHub
#
# without any option: Run FinalCif
#


if [ "$1" == "-pyinst" ]; then
    # Add python repository and install new Python3.9
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt install python3.9
    sudo apt install python3.9-venv
    exit
fi

if [ "$1" == "-install" ]; then
    echo 
    echo Which version number of FinalCif should be installed? 
    read version
    # Get the FinalCif code. Update the version number when needed:
    git clone --depth 1 --branch Version-$version https://github.com/dkratzert/FinalCif.git
fi

# Create a virtual environment and activate it:
cd FinalCif
python3.9 -m venv venv
source venv/bin/activate

if [ "$1" == "-install" ]; then
    # Install required Python packages:
    pip3 install pip -U
    pip3 install -r requirements.txt -U
    echo ""
    echo Installation finished! Run FinalCif with './finalcif-start.sh'
    exit
fi

# Finally, run FinalCif
python3 finalcif.py


