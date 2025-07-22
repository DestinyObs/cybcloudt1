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

### Method 1: Using Script
```bash
chmod +x ../scripts/install-ansible.sh
sudo ../scripts/install-ansible.sh
chmod +x ../scripts/run-deployment.sh
../scripts/run-deployment.sh
```

### Method 2: Manual Ansible
```bash
# Install collections
ansible-galaxy collection install -r requirements.yml

# Run deployment
ansible-playbook site.yml
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

## Troubleshooting
```bash
sudo gitlab-ctl status
sudo gitlab-ctl restart
sudo gitlab-ctl tail
sudo gitlab-ctl reconfigure
```
