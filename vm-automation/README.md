# CyberCloud VM Deployment Automation

## Overview
Dynamic Ansible playbooks for automated VM deployment on CyberCloud platform.

## Purpose
This automation framework allows for:
- Dynamic VM creation on cloud platform
- Multi-OS support (RHEL, CentOS, Ubuntu, Windows)
- Scalable resource allocation
- Reusable deployment templates
- Application-specific configurations

## Structure
```
vm-automation/
├── README.md
├── playbooks/
│   ├── deploy-vm.yml              # Main VM deployment
│   ├── deploy-web-server.yml      # Web server deployment
│   ├── deploy-database.yml        # Database server deployment
│   └── deploy-gitlab-stack.yml    # Complete GitLab stack
├── roles/
│   ├── vm-create/                 # VM creation role
│   ├── os-config/                 # OS configuration
│   ├── app-install/               # Application installation
│   └── monitoring/                # Monitoring setup
├── inventory/
│   ├── vm-templates.yml           # VM template definitions
│   └── environments/              # Environment-specific configs
├── templates/
│   ├── vm-specs/                  # VM specification templates
│   └── cloud-init/                # Cloud-init configurations
└── vars/
    ├── vm-defaults.yml            # Default VM settings
    └── platform-config.yml       # Platform-specific settings
```

## Quick Start

### Deploy Single VM
```bash
ansible-playbook playbooks/deploy-vm.yml \
  -e vm_name=web-server-01 \
  -e vm_os=rhel9 \
  -e vm_cpu=2 \
  -e vm_memory=4096 \
  -e vm_disk=50
```

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
