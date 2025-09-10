def send_message(sock, message):
    message = message.encode('utf-8')
    length = len(message).to_bytes(4, byteorder='big')
    sock.sendall(length + message)

def receive_message(sock):
    length_bytes = sock.recv(4)
    if not length_bytes:
        return ''
    length = int.from_bytes(length_bytes, byteorder='big')
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            break
        data += more
    return data.decode('utf-8')
