from client_utils import receive_message, send_message

def handle_client(conn, logger):
    with conn:
        while True:
            msg = receive_message(conn)
            if not msg:
                logger.info("Client disconnected")
                break
            logger.info(f"Received message: {msg}")
            response = f"Server received: {msg}"
            send_message(conn, response)
