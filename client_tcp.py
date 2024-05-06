import socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 8080))
while True:
    message = input("You: ")
    if message.lower() == 'quit':
        break
    tcp_socket.sendall(message.encode())
    data = tcp_socket.recv(1024)
    print("server:", data.decode())
tcp_socket.close()
