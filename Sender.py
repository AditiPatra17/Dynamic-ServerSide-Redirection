import tkinter as tk
import socket
import threading
import sys

class SenderApp:
    def __init__(self, master):
        
        ip_address = sys.argv[1]
        self.master = master
        self.master.title("Sender")
        
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
        
        self.server_ip = ip_address  # Change this to the receiver's IP address
        self.server_port = 12345
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_ip, self.server_port))
        
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        
    def send_message(self):
        message = self.message_entry.get()
        self.socket.send(message.encode('utf-8'))
        self.message_entry.delete(0, tk.END)
        
    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                self.chat_text.config(state=tk.NORMAL)
                self.chat_text.insert(tk.END, message + "\n")
                self.chat_text.config(state=tk.DISABLED)
                self.chat_text.see(tk.END)
            except ConnectionAbortedError:
                break
                
    def close_connection(self):
        self.socket.close()
        sys.exit()

def start_sender():
    root = tk.Tk()
    app = SenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_sender()
