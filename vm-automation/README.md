# CyberCloud VM Provisioning Service
# Customer service interface for VM automation

## Standard OS Support
- Ubuntu (default: Ubuntu20-Template)
- Windows (default: Windows2019-Template)  
- Red Hat Enterprise Linux (default: RHEL8-Template)
- CentOS (default: CentOS8-Template)
- Debian (default: Debian11-Template)

## Custom OS Support
For any OS not listed above, the system will attempt to provision using:
- Template name: {OS_NAME}-Template
- Generic guest OS type assignment

## Set environment variables for company data and credentials 
```bash
export CYBERCLOUD_USER="your-username"
export CYBERCLOUD_PASSWORD="your-password"
export CYBERCLOUD_HOST="your-host"
export CYBERCLOUD_ORG="your-org"'
```

```bash
export CYBERCLOUD_USER=""
export CYBERCLOUD_PASSWORD=""
export CYBERCLOUD_HOST="portal.cybercloud.net.ng/tenant/ceph-Management-Cluster/vdcs"
export CYBERCLOUD_ORG="ceph-Management-Cluster"
```
These variables are read automatically by the playbook. No secrets or company info are hardcoded.

## Customer Usage Examples

### Standard VM Requests
```bash
# Ubuntu VM (most common)
ansible-playbook main.yml -e "vm_type=ubuntu cybercloud_password=PASSWORD"

# Windows Server
ansible-playbook main.yml -e "vm_type=windows cybercloud_password=PASSWORD"

# Red Hat Enterprise Linux
ansible-playbook main.yml -e "vm_type=rhel cybercloud_password=PASSWORD"
```

### Custom VM Specifications
```bash
# High-performance VM
ansible-playbook main.yml -e "
  vm_type=ubuntu
  requested_memory=8192
  requested_cpu=4
  vm_name=customer-web-server
  cybercloud_password=PASSWORD
"

# Custom OS (if template exists)
ansible-playbook main.yml -e "
  vm_type=rocky
  cybercloud_password=PASSWORD
"

# Specific VDC and network
ansible-playbook main.yml -e "
  vm_type=windows
  target_vdc=Customer-VDC
  target_network=Customer-Network
  cybercloud_password=PASSWORD
"
```

### Advanced Custom Template
```bash
# Use specific template name
ansible-playbook main.yml -e "
  custom_template={'template_name': 'Custom-OS-Template', 'guest_os': 'otherLinux64Guest'}
  vm_name=special-application-server
  cybercloud_password=PASSWORD
"
```

## Required Parameters
- cybercloud_password: CyberCloud account password

## Optional Parameters
- vm_type: OS type (ubuntu, windows, rhel, centos, debian, or custom)
- vm_name: Custom VM name
- requested_memory: Memory in MB (default: 2048)
- requested_cpu: Number of CPUs (default: 2)
- target_vdc: Target VDC (default: Ceph-Management-Cluster)
- target_network: Target network (default: CephLAN)
- catalog_name: Source catalog (default: Public Catalog)

## System Capabilities
1. Provisions VMs from existing templates
2. Automatically handles DHCP networking
3. Powers on VMs after creation
4. Supports any OS if template exists in catalog
5. Provides fallback for unknown OS types
6. Scales across multiple VDCs and networks

## Prerequisites
- pyvcloud SDK installed (`pip install -r requirements.txt`)
- CyberCloud account access
- Target VDC permissions
- Network access permissions

## Python Environment Setup

Run these commands to set up Python and a virtual environment:

```bash
# Install Python 3 and pip (if not already installed)
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

# Create and activate a virtual environment
python3 -m venv venv/vm
source venv/vm/bin/activate

# Install required Python packages
pip install -r requirements.txt
```