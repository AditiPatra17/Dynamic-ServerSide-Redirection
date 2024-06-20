import socket
import subprocess

def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 12346
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_socket.bind((host, port))
    host_socket.listen(5)
    print("Host listening on", host, "port", port)

    client_socket, addr = host_socket.accept()
    print("Connection from", addr)
    client_socket.send(host.encode())
    subprocess.run(['python', 'Reciever.py'])


def start_program_with_ip(ip_address):
    try:
        # Replace 'program_to_start.py' with the name of your Python program
        # that you want to start
        subprocess.Popen(['python', 'Reciever.py', ip_address])
        print("Started program with IP:", ip_address)
    except Exception as e:
        print("Error starting program:", e)

    



if __name__ == "__main__":
    main()
