import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("You: ")
    if message.lower() == 'quit':
        break
    udp_socket.sendto(message.encode(), ('localhost', 9090))
    data, addr = udp_socket.recvfrom(1024)
    print("server:", data.decode())
udp_socket.close()
