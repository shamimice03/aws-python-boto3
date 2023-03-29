#!/bin/bash

# Update the package manager
sudo yum update -y

# Install dependencies
sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget

# Download Python 3.9 source code
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz

# Extract the downloaded file
tar xzf Python-3.9.0.tgz

# Change to the extracted directory
cd Python-3.9.0

# Configure the installation
./configure --enable-optimizations

# Compile the source code
make -j 4

# Install Python 3.9
sudo make altinstall

# Verify the installation
python3.9 --version
