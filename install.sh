#!/bin/bash

if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Cannot determine the Linux distribution. Exiting."
    exit 1
fi

echo "Detected distribution: $DISTRO"

# Detect if running inside WSL
if [ -f /proc/sys/fs/binfmt_misc/WSLInterop ]; then
    echo "Running inside WSL"
    IS_WSL=true
else
    IS_WSL=false
fi

if [ "$IS_WSL" = true ]; then
    echo "Detected Windows Subsystem for Linux (WSL)."
    echo "Adding NVIDIA Container toolkit for GPU Support"
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
        sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
        sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    sudo apt-get update
    sudo apt-get install -y nvidia-container-toolkit
fi

# Run commands based on the detected distribution
case "$DISTRO" in
    ubuntu)
        echo "Running Ubuntu-specific installation..."
        sudo apt update
        sudo apt install -y software-properties-common
        sudo add-apt-repository -y ppa:apptainer/ppa
        sudo apt update
        sudo apt install -y apptainer
        ;;
    debian)
        echo "Running Debian-specific installation..."
        sudo apt update
        sudo apt install -y wget
        cd /tmp
        wget https://github.com/apptainer/apptainer/releases/download/v1.4.0/apptainer_1.4.0_amd64.deb
        sudo apt install -y ./apptainer_1.4.0_amd64.deb
        ;;
    *)
        echo "Unknown or unsupported distribution."
        echo "Manual installation of 'apptainer' is required."
        echo "See apptainer docs: https://apptainer.org/docs/admin/latest/installation.html"
        ;;
esac

REPO_URL="https://github.com/harleylara/a2s-cli.git"
TARGET_DIR="$HOME/a2s-cli"

if [ ! -d "$TARGET_DIR" ]; then
    echo "Cloning repository..."
    git clone $REPO_URL $TARGET_DIR
fi

cd $TARGET_DIR

echo "Running pip install..."
pip install .
