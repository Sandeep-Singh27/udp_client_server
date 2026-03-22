import socket
from dotenv import load_dotenv
import sys,os

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
    while True:
        message = input("Enter the message: ")
        udp_client.sendto(bytes(message,encoding="utf-8"),(SERVER_IP,SERVER_PORT))
        response,address = udp_client.recvfrom(4000)
        print(f"[*]From {address} recieved : {response.decode("utf-8")}")

