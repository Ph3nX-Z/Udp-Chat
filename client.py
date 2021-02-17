import socket

username = input("Your username :")
adress = ("192.168.1.14", 1234)
packetsize = 1024
socket1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:

    to_send = str.encode(username+":"+input("Your Message >> "))
    socket1.sendto(to_send, adress)
    from_server = socket1.recvfrom(packetsize)
    msg = "Message from Server {}".format(from_server[0])

    print(msg)
