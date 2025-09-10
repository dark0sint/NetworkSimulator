import socket
from server_utils import handle_client
from logger import setup_logger

def main():
    logger = setup_logger('server.log')
    host = '0.0.0.0'
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        logger.info(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            logger.info(f"Connected by {addr}")
            handle_client(conn, logger)

if __name__ == "__main__":
    main()
