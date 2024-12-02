import socket
import threading
import os
import time

def print_data(cpu,ram,client_address):
    c=float(cpu)
    c=int(c/10)
    r=float(ram)
    r=int(r/10)
    
    print(f"USER IP: {client_address}")
    
    print(f"CPU USAGE: {cpu} :",end='')
    for i in range(c):
        print("#",end='')
    for i in range(10-c):
        print("-",end='')
    
    print("          ",end='') #10 spaces
    
    print(f"RAM USAGE: {ram} :",end='')
    for i in range(r):
        print("#",end='')
    for i in range(10-r):
        print("-",end='')
        
    print(" ")
    
    return 0

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        while True:
            
            cpu = client_socket.recv(1024).decode()
            if not cpu:
                break
            # print(f"[{client_address}] Sent: {cpu}")
            
            ram = client_socket.recv(1024).decode()
            if not ram:
                break
            # print(f"[{client_address}] Sent: {ram}")
            
            print_data(cpu,ram,client_address)
            
            time.sleep(4)
            os.system('cls')
            
    except ConnectionResetError:
        print(f"[DISCONNECTED] {client_address} disconnected.")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(5)
    print("[SERVER] Server is listening on port 5555")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
