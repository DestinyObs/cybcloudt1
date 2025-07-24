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
    # Remove headless mode for debugging
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Firefox(options=options)
    
    try:
        print(f"Creating {vm_type} VM: {vm_name}")
        
        # Login to portal
        driver.get("https://portal.cybercloud.net.ng/tenant/ceph-Management-Cluster/vdcs")
        
        # Login form - wait for page to load
        wait = WebDriverWait(driver, 20)
        time.sleep(3)  # Let page fully load
        
        # Try different possible selectors for username field
        username_field = None
        for selector in [
            (By.ID, "username"),
            (By.NAME, "username"), 
            (By.XPATH, "//input[@type='text']"),
            (By.XPATH, "//input[contains(@placeholder, 'username') or contains(@placeholder, 'Username')]")
        ]:
            try:
                username_field = wait.until(EC.presence_of_element_located(selector))
                break
            except:
                continue
                
        if not username_field:
            raise Exception("Could not find username field")
            
        username_field.clear()
        username_field.send_keys(username)
        
        # Try different selectors for password field
        password_field = None
        for selector in [
            (By.ID, "password"),
            (By.NAME, "password"),
            (By.XPATH, "//input[@type='password']")
        ]:
            try:
                password_field = driver.find_element(*selector)
                break
            except:
                continue
                
        if not password_field:
            raise Exception("Could not find password field")
            
        password_field.clear()
        password_field.send_keys(password)
        
        # Try different selectors for login button
        login_button = None
        for selector in [
            (By.XPATH, "//button[@type='submit']"),
            (By.XPATH, "//input[@type='submit']"),
            (By.XPATH, "//button[contains(text(), 'Log') or contains(text(), 'Sign')]"),
            (By.ID, "loginButton")
        ]:
            try:
                login_button = driver.find_element(*selector)
                break
            except:
                continue
                
        if not login_button:
            raise Exception("Could not find login button")
            
        login_button.click()
        
        print("Logged in successfully")
        
        # Wait for dashboard/main page to load
        time.sleep(5)
        
        # Navigate to VM creation - try multiple approaches
        try:
            # Try clicking Virtual Machines in sidebar
            vms_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Virtual Machines') or contains(text(), 'VMs')]")))
            vms_link.click()
        except:
            try:
                # Try alternative navigation
                vms_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Virtual Machines')]")
                vms_link.click()
            except:
                # Try clicking on vApps or Applications first
                try:
                    apps_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Applications') or contains(text(), 'vApps')]")
                    apps_link.click()
                    time.sleep(2)
                    vms_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Virtual Machines')]")
                    vms_link.click()
                except:
                    raise Exception("Could not navigate to Virtual Machines")
        
        time.sleep(3)
        
        # Look for Create VM button
        create_button = None
        for selector in [
            (By.XPATH, "//button[contains(text(), 'Create VM') or contains(text(), 'ADD') or contains(text(), 'New')]"),
            (By.XPATH, "//a[contains(text(), 'Create VM') or contains(text(), 'ADD')]"),
            (By.ID, "createVM"),
            (By.CLASS_NAME, "create-vm")
        ]:
            try:
                create_button = wait.until(EC.element_to_be_clickable(selector))
                break
            except:
                continue
                
        if not create_button:
            raise Exception("Could not find Create VM button")
            
        create_button.click()
        
        print("Navigated to VM creation")
        
        # Wait for Create VM dialog to load
        time.sleep(3)
        
        # Fill VM details - try multiple selectors for name field
        name_field = None
        for selector in [
            (By.NAME, "name"),
            (By.ID, "vmName"),
            (By.XPATH, "//input[@placeholder='Name' or @placeholder='VM Name']"),
            (By.XPATH, "//label[contains(text(), 'Name')]/following-sibling::input"),
            (By.XPATH, "//label[contains(text(), 'Name')]/..//input")
        ]:
            try:
                name_field = wait.until(EC.presence_of_element_located(selector))
                break
            except:
                continue
                
        if not name_field:
            raise Exception("Could not find VM name field")
            
        name_field.clear()
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
        
        # Take screenshot for debugging
        try:
            driver.save_screenshot("/tmp/vm_creation_error.png")
            print("Screenshot saved to /tmp/vm_creation_error.png")
        except:
            pass
            
        # Print page source for debugging
        try:
            with open("/tmp/page_source.html", "w") as f:
                f.write(driver.page_source)
            print("Page source saved to /tmp/page_source.html")
        except:
            pass
            
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
