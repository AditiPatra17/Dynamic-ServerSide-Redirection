import tkinter as tk
import sys
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
    redirected_socket.send((client_socket.recv(1024).decode()).encode())
    while True:
        client_socket.send((redirected_socket.recv(1024).decode()).encode())
        redirected_socket.send((client_socket.recv(1024).decode()).encode())


def run_server(ip_address):
    root = tk.Tk()
    root.title("Server GUI")
    root.geometry("400x200")
    ip_label = tk.Label(root, text=f"Mainframe IP: {ip_address}")
    ip_label.pack(pady=10)


    host = socket.gethostbyname(socket.gethostname())
    port = 12340
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    mainframeIP = ip_address
    print("Server listening on", host, "port", port)

    ip_label = tk.Label(root, text=f"Server listening on, {host}, port, {port}")
    ip_label.pack(pady=10)

    def connect(ip_address):
        ip_label = tk.Label(root, text=f"Connection From: {ip_address}")
        ip_label.pack(pady=10)
        print("0")
        root.mainloop()

    root.mainloop()

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)
        print("0")
        connect(addr)
        data = client_socket.recv(1024).decode()

        if (data == mainframeIP):
            redirect_connection(client_socket)
        else:
            print("Bypass unsuccessful")
    


def start_action():
    ip_address = ip_entry.get()
    root.destroy()
    run_server(ip_address)


# Create the main window
root = tk.Tk()
root.title("Server GUI")

root.geometry("400x200")



ip_label = tk.Label(root, text="Enter Mainframe IP:")
ip_label.pack(pady=10)

ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)

# Create and position widgets
start_button = tk.Button(root, text="Start", command=start_action)
start_button.pack(pady=10)


# Start the GUI event loop
root.mainloop()
