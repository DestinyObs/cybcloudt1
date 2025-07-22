#!/bin/bash

# GitLab deployment script

echo "Starting GitLab deployment..."

# Navigate to playbooks directory
cd playbooks/

# Run the main playbook
ansible-playbook site.yml

echo "Deployment complete."
echo "Access GitLab at: http://10.10.10.7"
echo "Username: root"
echo "Password: Check /etc/gitlab/initial_root_password"
