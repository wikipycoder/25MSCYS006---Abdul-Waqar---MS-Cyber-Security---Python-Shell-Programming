#!/bin/bash

system_info() {
    echo "-------------------------------------"
    echo "   SYSTEM INFORMATION"
    echo "-------------------------------------"
    echo "Hostname: $(hostname)"
    echo "Current User: $USER"
    echo "Operating System: $(uname -o)"
    echo "Kernel Version: $(uname -r)"
    echo "Uptime: $(uptime -p)"
    echo
}

security_check() {
    echo "-------------------------------------"
    echo "   BASIC SECURITY CHECK"
    echo "-------------------------------------"

    if command -v ufw >/dev/null 2>&1; then
        STATUS=$(sudo ufw status | grep -o "active")
        echo "Firewall (UFW): ${STATUS:-inactive}"
    else
        echo "Firewall (UFW): Not installed"
    fi

    echo
    echo "World-writable files in /etc:"
    find /etc -perm -0002 -type f 2>/dev/null
    echo
}

menu() {
    echo "-------------------------------------"
    echo "   PYTHON & SHELL PROGRAMMING TOOL"
    echo "-------------------------------------"
    echo "1) Show System Information"
    echo "2) Run Security Check"
    echo "3) Show Disk Usage"
    echo "4) Exit"
    echo
}

disk_usage() {
    echo "-------------------------------------"
    echo "   DISK USAGE"
    echo "-------------------------------------"
    df -h /
    echo
}

while true; do
    menu
    read -p "Select an option (1-4): " choice

    case $choice in
        1) system_info ;;
        2) security_check ;;
        3) disk_usage ;;
        4) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid option. Try again." ;;
    esac
done
