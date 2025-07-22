#!/bin/bash

echo "Installing Ansible on Red Hat-based system..."

# Ensure EPEL repo is enabled (Extra Packages for Enterprise Linux)
sudo yum install -y epel-release

# Install Ansible
sudo yum install -y ansible

# Verify installation
ansible --version

echo "Ansible installation complete."