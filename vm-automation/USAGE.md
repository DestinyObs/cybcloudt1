# CyberCloud VM Automation Examples
# Purpose: Example commands for creating different types of VMs

## 1. Create RHEL VM (Default)
```bash
ansible-playbook main.yml -e "cybercloud_password=YOUR_PASSWORD"
```

## 2. Create Ubuntu VM
```bash
ansible-playbook main.yml -e "vm_type=ubuntu cybercloud_password=YOUR_PASSWORD"
```

## 3. Create Windows VM
```bash
ansible-playbook main.yml -e "vm_type=windows cybercloud_password=YOUR_PASSWORD"
```

## 4. Create VM with Custom Name and Specs
```bash
ansible-playbook main.yml -e "
  vm_type=rhel
  vm_name=my-custom-rhel-server
  vm_memory=4096
  vm_cpu=4
  cybercloud_password=YOUR_PASSWORD
"
```

## 5. Create VM in Different VDC
```bash
ansible-playbook main.yml -e "
  vm_type=ubuntu
  vdc_name=Different-VDC
  cybercloud_password=YOUR_PASSWORD
"
```

## Variables You Can Override:
- `vm_type`: rhel, ubuntu, windows (default: rhel)
- `vm_name`: Custom VM name (default: auto-generated)
- `vm_memory`: Memory in MB (default: 2048)
- `vm_cpu`: Number of CPUs (default: 2)
- `vdc_name`: VDC name (default: Ceph-Management-Cluster)
- `cybercloud_org`: Organization name (default: ceph-Management-Cluster)
- `cybercloud_password`: **REQUIRED** - Your CyberCloud password

## Prerequisites:
1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your CyberCloud account has access to:
   - Portal: portal.cybercloud.net.ng
   - VDC: Ceph-Management-Cluster
   - Network: CephLAN
   - Templates in Public Catalog

## Output:
The playbook will create a VM and display:
- VM Name
- VM Type
- vApp Container
- VDC Location
- Network Assignment
- Creation Status

The VM will be automatically powered on and ready for use with DHCP networking.
