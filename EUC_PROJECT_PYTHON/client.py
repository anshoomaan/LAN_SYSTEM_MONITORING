import socket
import time
import random
import psutil

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))
    print("[CLIENT] Connected to server on port 5555")
    
    try:
        while True:
            
            cpu=psutil.cpu_percent(4)
            ram=psutil.virtual_memory()[2]
            
            client_socket.send(str(cpu).encode())
            client_socket.send(str(ram).encode())
            print(f"[CLIENT] Sent: {cpu,ram}")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n[CLIENT] Disconnected from server.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()