import socket
from client_utils import send_message, receive_message
from logger import setup_logger

def main():
    logger = setup_logger('client.log')
    host = '127.0.0.1'  # Ganti dengan IP server
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        logger.info(f"Connected to server {host}:{port}")

        send_message(s, "Hello Server!")
        response = receive_message(s)
        logger.info(f"Received from server: {response}")

if __name__ == "__main__":
    main()
