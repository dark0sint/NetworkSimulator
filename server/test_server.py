import socket
from server_utils import handle_client
from client_utils import send_message, receive_message

def test_handle_client():
    s1, s2 = socket.socketpair()
    import threading

    def server_thread():
        handle_client(s1, print)

    t = threading.Thread(target=server_thread)
    t.start()

    send_message(s2, "Hello Server")
    response = receive_message(s2)
    assert response == "Server received: Hello Server"
    print("Test passed: handle_client")

    s2.close()
    t.join()

if __name__ == "__main__":
    test_handle_client()
