# CyberCloud VM Automation

## Purpose
Ansible playbook to automate VM creation on CyberCloud platform.

## VM Types Supported
- **rhel** - Red Hat Enterprise Linux 8 (2 CPU, 4GB RAM)
- **ubuntu** - Ubuntu 20.04 Server (2 CPU, 4GB RAM) 
- **windows** - Windows Server 2019 (4 CPU, 8GB RAM)

All VMs use CephLAN network with DHCP for automatic IP assignment.

## Setup

1. Transfer this folder to your RHEL VM (10.10.10.7):
```bash
scp -r vm-automation root@10.10.10.7:/root/
```

2. SSH to RHEL VM and setup:
```bash
ssh root@10.10.10.7
cd vm-automation/scripts
chmod +x setup.sh
./setup.sh
```

## Usage

Create VMs using the playbook:

```bash
# Create RHEL VM
ansible-playbook playbooks/create-vm.yml \
  -e vm_name=my-rhel-vm \
  -e vm_type=rhel \
  -e cybercloud_password=YOUR_PASSWORD

# Create Ubuntu VM  
ansible-playbook playbooks/create-vm.yml \
  -e vm_name=my-ubuntu-vm \
  -e vm_type=ubuntu \
  -e cybercloud_password=YOUR_PASSWORD

# Create Windows VM
ansible-playbook playbooks/create-vm.yml \
  -e vm_name=my-windows-vm \
  -e vm_type=windows \
  -e cybercloud_password=YOUR_PASSWORD
```

## Files
- `playbooks/create-vm.yml` - Main Ansible playbook
- `scripts/selenium/create_vm.py` - Python script for web automation
- `scripts/setup.sh` - Setup script for RHEL VM

That's it. Simple VM creation automation for CyberCloud platform.

### Deploy Application Stack
```bash
ansible-playbook playbooks/deploy-gitlab-stack.yml \
  -e environment=production \
  -e vm_count=3
```

### Deploy Multiple VMs
```bash
ansible-playbook playbooks/deploy-vm.yml \
  -e @vars/bulk-deployment.yml
```

## Features

### Dynamic VM Creation
- Automated VM provisioning on cloud platform
- Template-based deployment
- Resource scaling based on requirements

### Multi-OS Support
- RHEL 8/9
- CentOS Stream
- Ubuntu 20.04/22.04
- Windows Server 2019/2022

### Application Stacks
- Web servers (Apache, Nginx)
- Database servers (MySQL, PostgreSQL)
- GitLab CE/EE
- Docker containers
- Kubernetes clusters

### Cloud Platform Integration
- VMware vCloud Director
- OpenStack
- AWS EC2
- Azure VMs
- Google Compute Engine

## Usage Examples

### Example 1: Web Server Farm
Deploy 3 web servers with load balancer:
```bash
ansible-playbook playbooks/deploy-web-server.yml \
  -e server_count=3 \
  -e load_balancer=true \
  -e environment=production
```

### Example 2: Development Environment
Deploy complete dev environment:
```bash
ansible-playbook playbooks/deploy-dev-environment.yml \
  -e developer_name=john-doe \
  -e project_name=webapp-v2
```

### Example 3: Database Cluster
Deploy MySQL cluster with replication:
```bash
ansible-playbook playbooks/deploy-database.yml \
  -e db_type=mysql \
  -e cluster_size=3 \
  -e replication=true
```

## Configuration

All deployments are configured through YAML variables:
- VM specifications
- Network settings
- Security configurations
- Application parameters

## Integration

This automation integrates with:
- CyberCloud platform APIs
- Monitoring systems
- Backup solutions
- Security scanning tools
