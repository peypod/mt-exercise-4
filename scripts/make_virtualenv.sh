#! /bin/bash

# virtualenv must be installed on your system, install with e.g.
# pip install virtualenv

scripts=$(dirname "$0")
base=$scripts/..

mkdir -p $base/venvs

# python3 needs to be installed on your system

C:/Users/peapo/AppData/Local/Programs/Python/Python310/python.exe -m virtualenv -p python3.10 $base/venvs/torch3

echo "To activate your environment:"
echo "    source $base/venvs/torch3/Scripts/activate"
