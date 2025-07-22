#!/bin/bash

# Simple Ansible installation script for RHEL 8.6
# Run as root or with sudo

# Update system
yum update -y

# Install EPEL repository
yum install -y epel-release

# Install Python3 and pip
yum install -y python3 python3-pip

# Install Ansible
pip3 install ansible

# Install additional collections
ansible-galaxy collection install community.general
ansible-galaxy collection install ansible.posix

# Verify installation
ansible --version

echo "Ansible installation completed"
