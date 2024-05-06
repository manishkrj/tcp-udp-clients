import socket
import select
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(('localhost', 8080))
tcp_socket.listen(5)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('localhost', 9090))
sockets_list = [tcp_socket, udp_socket]
while True:
    read_sockets, _, _ = select.select(sockets_list, [], [])
    for sock in read_sockets:
        if sock == tcp_socket:
            client_socket, address = tcp_socket.accept()
            print(f"New TCP connection from {address}")
            sockets_list.append(client_socket)
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed with {sock.getpeername()}")
                sockets_list.remove(sock)
                sock.close()
            else:
                print(f"TCP client: {data.decode('utf-8')}")
            message=input("You: ")
            client_socket.send(message.encode('utf-8'))
        elif sock == udp_socket:
            data, addr = udp_socket.recvfrom(1024)
            print(f"UDP client: {data.decode('utf-8')}")
            message=input("You: ")
            udp_socket.send(message.encode('utf-8'))

