#!/bin/bash
set -euxo pipefail

echo "Installing Ansible via pip on Red Hat-based system..."

# Install system packages required for Ansible & Python dependencies
sudo yum install -y gcc libffi-devel python3-devel openssl-devel python3-pip

# (Optional) Install development tools group
sudo yum groupinstall -y "Development Tools"

# Upgrade pip and related tools
sudo pip3 install --upgrade pip setuptools wheel

# Install Ansible via pip
sudo pip3 install ansible

# Show Ansible version to confirm
ansible --version

echo "Ansible installation complete."