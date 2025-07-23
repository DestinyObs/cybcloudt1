# CyberCloud Technical - RHEL 8.6 GitLab Deployment Project

## Project Overview
CyberAcademy internship project to deploy a RHEL 8.6 server with GitLab-CE and develop automation playbooks.

### RHEL 8.6 Server Requirements
- **CPU:** 2 vCPU
- **RAM:** 4GB
- **Storage:** 128GB
- **OS:** Red Hat Enterprise Linux 8.6
- **Hostname:** gitlabce.local
- **IP Address:** 10.10.10.7

### GitLab-CE Features
- DevOps and Agile methodology support
- Central repository for codes and playbooks
- Version Control capabilities
- CI/CD pipeline management

## Access Information
- **Portal:** https://portal.cybercloud.net.ng/tenant/ceph-Management-Cluster/vdcs
- **GitLab URL:** http://10.10.10.7
- **Default Username:** root
- **Password Location:** /etc/gitlab/initial_root_password

## Quick Deployment

### GitLab Installation (Tasks 1 & 2)
```bash
cd ansible-config/
chmod +x scripts/install-ansible.sh scripts/run-deployment.sh
sudo scripts/install-ansible.sh
scripts/run-deployment.sh
```

### VM Automation (Task 3)
```bash
cd vm-automation/
ansible-playbook playbooks/deploy-vm.yml -e vm_name=test-server
```

## Manual Installation Commands

### Install Ansible
```bash
sudo yum update -y
sudo yum install -y epel-release
sudo yum install -y python3 python3-pip
pip3 install ansible
ansible-galaxy collection install community.general ansible.posix community.crypto
```

### Configure Server
```bash
sudo hostnamectl set-hostname gitlabce.local
echo "10.10.10.7 gitlabce.local" | sudo tee -a /etc/hosts
sudo yum update -y
sudo yum install -y vim wget curl git htop net-tools
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

### Install GitLab
```bash
sudo yum install -y curl policycoreutils openssh-server perl postfix
sudo systemctl start sshd && sudo systemctl enable sshd
sudo systemctl start postfix && sudo systemctl enable postfix
sudo firewall-cmd --permanent --add-service={http,https,ssh}
sudo firewall-cmd --reload
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
sudo EXTERNAL_URL="http://10.10.10.7" yum install -y gitlab-ce
sudo gitlab-ctl reconfigure
sudo gitlab-ctl start
```

### Access GitLab
```bash
sudo cat /etc/gitlab/initial_root_password
```
- **URL:** http://10.10.10.7
- **Username:** root
- **Password:** From file above

## Project Status

### ✅ Tasks Completed
1. **RHEL 8.6 Server Deployment** - Server deployed with exact specifications
2. **GitLab-CE Installation** - Automated playbooks ready and tested

### 🚧 Task 3: VM Deployment Automation
The third requirement is **dynamic VM deployment automation**:
- **Location:** `vm-automation/` folder
- **Purpose:** Create new VMs automatically on CyberCloud platform
- **Features:** Multi-OS support, scalable resources, reusable templates
- **Integration:** VMware vCloud Director API integration

### 📋 Project Structure
```
cybcloudt1/
├── ansible-config/          # GitLab installation (COMPLETE)
│   ├── site.yml
│   ├── scripts/
│   │   ├── run-deployment.sh
│   │   └── install-ansible.sh
│   └── roles/
├── vm-automation/           # VM deployment automation (NEW)
│   ├── playbooks/
│   └── templates/
└── docs/                   # Project documentation
```

### 🎯 Final Deliverable
Complete automation framework supporting:
- Single VM deployment
- Multi-VM application stacks
- Environment-specific configurations
- Dynamic resource scaling

## Troubleshooting
```bash
sudo gitlab-ctl status
sudo gitlab-ctl restart
sudo gitlab-ctl tail
sudo gitlab-ctl reconfigure
```
