import subprocess
import socket
import subprocess

server_ip = input('Enter Server IP Address')

def scan_local_network():
    local_ips = []

    scanningIP = server_ip.split(".")[2]
    IP = "192.168."+scanningIP+".0/24"

    try:
        nmap_output = subprocess.check_output(
            ["nmap", "-sn", IP])
        nmap_output = nmap_output.decode("utf-8")

        # Parse nmap output to extract available IP addresses
        lines = nmap_output.split("\n")
        for line in lines:
            if "Nmap scan report" in line:
                ip = line.split()[-1]
                local_ips.append(ip)
    except Exception as e:
        print("Error:", e)

    return local_ips


def main():
    print("Scanning local network for available IP addresses...")
    available_ips = scan_local_network()
    print("Available IP addresses on the local network:", available_ips)

    if not available_ips:
        print("No available IP addresses found on the local network.")
        return

    server_port = 12340
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))  # Server IP Address
    print("Connected to server")

    ip_to_send = input('Enter IP Address ')
    client_socket.sendall(ip_to_send.encode())

    ip_address = client_socket.recv(1024).decode()
    print("Connection Successful!!")
    subprocess.run(['python', 'Sender.py',ip_address])

    
    

if __name__ == "__main__":
    main()
