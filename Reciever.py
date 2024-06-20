import tkinter as tk
import socket
import threading
import sys

class ReceiverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Receiver")
        
        self.chat_label = tk.Label(master, text="Chat:")
        self.chat_label.pack()
        
        self.chat_text = tk.Text(master, height=20, width=50)
        self.chat_text.pack()
        self.chat_text.config(state=tk.DISABLED)
        
        self.message_label = tk.Label(master, text="Message:")
        self.message_label.pack()
        
        self.message_entry = tk.Entry(master, width=50)
        self.message_entry.pack()
        
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()
        
        self.bye_button = tk.Button(master, text="Bye", command=self.close_connection)
        self.bye_button.pack()
        
        self.server_ip = socket.gethostbyname(socket.gethostname())  # Change this to the receiver's IP address
        self.server_port = 12345
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.server_ip, self.server_port))
        self.socket.listen(1)
        
        self.client_socket, self.client_address = self.socket.accept()
        
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_text.config(state=tk.NORMAL)
                self.chat_text.insert(tk.END, message + "\n")
                self.chat_text.config(state=tk.DISABLED)
                self.chat_text.see(tk.END)
            except ConnectionAbortedError:
                break
                
    def send_message(self):
        message = self.message_entry.get()
        self.client_socket.send(message.encode('utf-8'))
        self.message_entry.delete(0, tk.END)
        
    def close_connection(self):
        self.client_socket.close()
        sys.exit()

def start_receiver():
    root = tk.Tk()
    app = ReceiverApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_receiver()
