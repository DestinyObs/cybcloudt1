#!/usr/bin/env python3

"""
Simple VM Creator for CyberCloud
Creates VMs using Selenium web automation
"""

import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# VM Templates
VM_TEMPLATES = {
    'rhel': {
        'os_family': 'Linux',
        'os': 'Red Hat Enterprise Linux 8 (64-bit)',
        'boot_image': 'rhel-8.7-x86_64-dvd.iso',
        'size': 'Medium'  # 2 CPU, 4GB RAM
    },
    'ubuntu': {
        'os_family': 'Linux', 
        'os': 'Ubuntu Linux (64-bit)',
        'boot_image': 'ubuntu-20.04-server-amd64.iso',
        'size': 'Medium'
    },
    'windows': {
        'os_family': 'Windows',
        'os': 'Microsoft Windows Server 2019 (64-bit)',
        'boot_image': 'windows-server-2019.iso',
        'size': 'Large'  # 4 CPU, 8GB RAM
    }
}

def create_vm(username, password, vm_name, vm_type):
    """Create VM on CyberCloud platform"""
    
    if vm_type not in VM_TEMPLATES:
        raise ValueError(f"Unsupported VM type: {vm_type}")
    
    template = VM_TEMPLATES[vm_type]
    
    # Setup Firefox driver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    
    try:
        print(f"Creating {vm_type} VM: {vm_name}")
        
        # Login to portal
        driver.get("https://portal.cybercloud.net.ng/tenant/ceph-Management-Cluster/vdcs")
        
        # Login form
        wait = WebDriverWait(driver, 15)
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(username)
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        print("Logged in successfully")
        
        # Navigate to VM creation
        time.sleep(3)
        vms_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Virtual Machines")))
        vms_link.click()
        
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create VM')]")))
        create_button.click()
        
        print("Navigated to VM creation")
        
        # Fill VM details
        name_field = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.send_keys(vm_name)
        
        # Select "New" type
        new_radio = driver.find_element(By.XPATH, "//input[@value='New']")
        new_radio.click()
        
        # Power on
        power_checkbox = driver.find_element(By.NAME, "powerOn")
        if not power_checkbox.is_selected():
            power_checkbox.click()
        
        # Select OS Family
        os_family_dropdown = Select(driver.find_element(By.NAME, "osFamily"))
        os_family_dropdown.select_by_visible_text(template['os_family'])
        time.sleep(2)
        
        # Select OS
        os_dropdown = Select(driver.find_element(By.NAME, "operatingSystem"))
        os_dropdown.select_by_visible_text(template['os'])
        time.sleep(2)
        
        # Select boot image
        boot_dropdown = Select(driver.find_element(By.NAME, "bootImage"))
        boot_dropdown.select_by_visible_text(template['boot_image'])
        
        print(f"Configured OS: {template['os']}")
        
        # Set size
        size_radio = driver.find_element(By.XPATH, f"//input[@value='{template['size']}']")
        size_radio.click()
        
        # Network settings
        network_dropdown = Select(driver.find_element(By.NAME, "network"))
        network_dropdown.select_by_visible_text("CephLAN")
        
        ip_mode_dropdown = Select(driver.find_element(By.NAME, "ipMode"))
        ip_mode_dropdown.select_by_visible_text("DHCP")
        
        print("Configured network: CephLAN (DHCP)")
        
        # Submit creation
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]")
        submit_button.click()
        
        print(f"VM {vm_name} creation submitted successfully")
        
        # Wait a bit to see if creation starts
        time.sleep(5)
        
        return True
        
    except Exception as e:
        print(f"Error creating VM: {e}")
        return False
        
    finally:
        driver.quit()

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 create_vm.py <username> <password> <vm_name> <vm_type>")
        print("VM types: rhel, ubuntu, windows")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2] 
    vm_name = sys.argv[3]
    vm_type = sys.argv[4]
    
    success = create_vm(username, password, vm_name, vm_type)
    
    if success:
        print("VM creation completed successfully")
        sys.exit(0)
    else:
        print("VM creation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
