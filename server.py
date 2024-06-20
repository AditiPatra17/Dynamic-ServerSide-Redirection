import sys
import socket
import socket


def redirect_connection(client_socket):
    # Implement redirection logic here
    redirectionIP = input('Enter Redirection Address')
    redirected_address = redirectionIP  # Example redirected address
    redirected_port = 12346  # Example redirected port
    redirected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    redirected_socket.connect((redirected_address, redirected_port))
    print("Connection redirected to:", redirected_address)
    data = redirected_socket.recv(4096).decode()
    client_socket.send(data.encode())
    

def main():

    host = socket.gethostbyname(socket.gethostname())
    port = 12340
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    mainframeIP = input("Enter the MainFrame IP Address ->")
    print("Server listening on", host, "port", port)

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)
        data = client_socket.recv(1024).decode()

        if (data == mainframeIP):
            redirect_connection(client_socket)
        else:
            print("Bypass unsuccessful")




if __name__ == "__main__":

    main()
