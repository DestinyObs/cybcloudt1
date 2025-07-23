#!/bin/bash

# GitLab deployment script for RHEL 8

echo "Starting GitLab deployment on RHEL 8..."

# Navigate to ansible-config directory (parent of scripts)
cd "$(dirname "$0")/.."

# Check if we're in the right directory
if [ ! -f "site.yml" ]; then
    echo "Error: site.yml not found. Make sure the ansible-config structure is correct."
    exit 1
fi

# Install Ansible collections
echo "Installing required Ansible collections..."
ansible-galaxy collection install -r requirements.yml

# Run the main playbook
echo "Running GitLab deployment playbook..."
ansible-playbook site.yml -v

echo ""
echo "Deployment complete!"
echo "Access GitLab at: http://10.10.10.7"
echo "Username: root"
echo "Password: Check /etc/gitlab/initial_root_password"
echo ""
echo "Useful commands:"
echo "  sudo gitlab-ctl status    # Check GitLab status"
echo "  sudo gitlab-ctl restart   # Restart GitLab"
echo "  sudo gitlab-ctl tail      # View logs"
