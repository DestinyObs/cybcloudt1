# GitLab CE Installation - Ansible Configuration

## Overview
Complete Ansible automation for GitLab Community Edition installation on RHEL 8.

## Structure
```
ansible-config/
├── ansible.cfg              # Ansible configuration
├── requirements.yml          # Required collections
├── site.yml                 # Main deployment playbook
├── run-deployment.sh        # Deployment script
├── install-ansible.sh       # Ansible installation script
├── inventory/
│   └── hosts.yml            # Host inventory
├── group_vars/
│   └── all.yml              # Global variables
└── roles/
    ├── server_config/       # Server configuration role
    │   ├── defaults/main.yml
    │   └── tasks/main.yml
    └── gitlab/              # GitLab installation role
        ├── defaults/main.yml
        └── tasks/main.yml
```

## Prerequisites
- RHEL 8.6 server deployed
- SSH access to the server
- Internet connectivity

## Quick Deployment

### Method 1: One-Command Deployment
```bash
chmod +x install-ansible.sh run-deployment.sh
sudo ./install-ansible.sh
./run-deployment.sh
```

### Method 2: Step by Step
```bash
# Install Ansible
chmod +x install-ansible.sh
sudo ./install-ansible.sh

# Install collections
ansible-galaxy collection install -r requirements.yml

# Run deployment
ansible-playbook site.yml
```

## RHEL 8 Compatibility Features

### Packages Verified for RHEL 8
- Removed `htop` (not in default repos)
- Added `bind-utils`, `tar`, `unzip`
- Added `policycoreutils-python-utils`
- Added `tzdata` for GitLab

### SELinux Configuration
- Set to permissive mode for GitLab compatibility
- Can be changed to enforcing after GitLab configuration

### Firewall Configuration
- Automatic firewall rules for HTTP, HTTPS, SSH
- Error handling for firewall configuration

## Troubleshooting

### Common Issues
```bash
# Check GitLab status
sudo gitlab-ctl status

# Restart GitLab
sudo gitlab-ctl restart

# View GitLab logs
sudo gitlab-ctl tail

# Reconfigure GitLab
sudo gitlab-ctl reconfigure
```

### Package Issues
If packages fail to install:
```bash
# Update system first
sudo yum update -y

# Install EPEL
sudo yum install -y epel-release

# Re-run deployment
ansible-playbook site.yml
```

### GitLab Access Issues
```bash
# Check GitLab URL configuration
sudo cat /etc/gitlab/gitlab.rb | grep external_url

# Check firewall
sudo firewall-cmd --list-all

# Check SELinux
getenforce
```

## Access Information
- **URL:** http://10.10.10.7
- **Username:** root
- **Initial Password:** `/etc/gitlab/initial_root_password`

## Post-Installation
1. Change root password immediately
