import os
import socket
import sys

def check_requirements():
    print("This script requires the following packages: nmap, requests")
    confirm = input("Do you want to continue? (y/n) ")
    if confirm.lower() != 'y':
        print("Sorry, the script cannot run without your permission.")
        sys.exit(0)

def gather_device_info():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname:", host_name)
    print("IP address:", host_ip)

def ping_sweep(ip_range):
    for i in range(1, 255):
        response = os.system("ping -c 1 " + ip_range + str(i))
        if response == 0:
            print(ip_range + str(i) + " is up")
        else:
            print(ip_range + str(i) + " is down")

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
        sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to the server.")

def main():
    print("Welcome to my network automation script.")
    print("Please choose an option:")
    print("1. Ping sweep")
    print("2. Port scanner")
    print("3. Network device information gathering")
    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice == 1:
        ip_range = input("Enter the IP range to scan (e.g. 192.168.0.): ")
        ping_sweep(ip_range)
    elif choice == 2:
        host = input("Enter the host to scan: ")
        port = int(input("Enter the port to scan: "))
        port_scanner(host, port)
    elif choice == 3:
        gather_device_info()
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
