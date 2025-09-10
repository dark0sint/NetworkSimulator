import socket
from client_utils import send_message, receive_message

def test_send_receive():
    # Simulasi socket dengan socket.socketpair untuk testing
    s1, s2 = socket.socketpair()

    try:
        send_message(s1, "Test Message")
        msg = receive_message(s2)
        assert msg == "Test Message"
        print("Test passed: send_message and receive_message")
    finally:
        s1.close()
        s2.close()

if __name__ == "__main__":
    test_send_receive()
