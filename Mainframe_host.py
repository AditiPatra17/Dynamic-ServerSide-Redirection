import socket


def main():
    host = socket.gethostbyname(socket.gethostname())
    port = 12346
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_socket.bind((host, port))
    host_socket.listen(5)
    print("Host listening on", host, "port", port)

    client_socket, addr = host_socket.accept()
    print("Connection from", addr)
    client_socket.send("Welcome to the host!".encode())

    client_socket.close()


if __name__ == "__main__":
    main()
