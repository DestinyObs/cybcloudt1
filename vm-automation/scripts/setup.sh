#!/bin/bash

# Simple setup for VM automation on RHEL
# Run this on your RHEL VM (10.10.10.7)

echo "Setting up CyberCloud VM Automation..."

# Install Selenium (Firefox already comes with RHEL)
pip3 install --user selenium

echo "Setup completed!"
echo ""
echo "Usage:"
echo "1. Create RHEL VM:"
echo "   ansible-playbook playbooks/create-vm.yml -e vm_name=test-rhel -e vm_type=rhel -e cybercloud_password=YOUR_PASSWORD"
echo ""
echo "2. Create Ubuntu VM:"
echo "   ansible-playbook playbooks/create-vm.yml -e vm_name=test-ubuntu -e vm_type=ubuntu -e cybercloud_password=YOUR_PASSWORD"
echo ""
echo "3. Create Windows VM:"
echo "   ansible-playbook playbooks/create-vm.yml -e vm_name=test-windows -e vm_type=windows -e cybercloud_password=YOUR_PASSWORD"
