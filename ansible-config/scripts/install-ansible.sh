#!/bin/bash
set -euo pipefail

echo "Checking Ansible installation on Red Hat-based system..."

# Function to check if Ansible is installed
check_ansible() {
    if command -v ansible >/dev/null 2>&1; then
        echo "Ansible is already installed:"
        ansible --version
        return 0
    else
        return 1
    fi
}

# Check if Ansible is already installed
if check_ansible; then
    echo "Ansible installation check complete - already installed."
    exit 0
fi

echo "Ansible not found. Installing Ansible via pip..."

# Install system packages required for Ansible & Python dependencies
echo "Installing system dependencies..."
sudo yum install -y gcc libffi-devel python3-devel openssl-devel python3-pip

# (Optional) Install development tools group
echo "Installing development tools..."
sudo yum groupinstall -y "Development Tools"

# Upgrade pip and related tools
echo "Upgrading pip and tools..."
sudo pip3 install --upgrade pip setuptools wheel

# Install Ansible via pip
echo "Installing Ansible..."
sudo pip3 install ansible

# Verify installation
echo "Verifying Ansible installation..."
if check_ansible; then
    echo "Ansible installation completed successfully!"
else
    echo "ERROR: Ansible installation failed!"
    exit 1
fi