#!/bin/bash

# Simple Ansible installation script for RHEL9
# Run as root or with sudo

# Update system
dnf update -y

# Install EPEL repository
dnf install -y epel-release

# Install Python3 and pip
dnf install -y python3 python3-pip

# Install Ansible
pip3 install ansible

# Install additional collections
ansible-galaxy collection install community.general
ansible-galaxy collection install ansible.posix

# Verify installation
ansible --version

echo "Ansible installation completed"
