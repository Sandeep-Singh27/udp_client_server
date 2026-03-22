import socket
from dotenv import load_dotenv
import sys,os

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_server:
    udp_server.bind((SERVER_IP,SERVER_PORT))
    print(f"[*]Started Listening on {SERVER_IP}:{SERVER_PORT}...")
    while True:
        data,address = udp_server.recvfrom(4096)
        data.strip()
        print(f"Recieved data:{data.decode()} | address:{address}")
        udp_server.sendto("I am the server accepting connections...".encode(),address)
