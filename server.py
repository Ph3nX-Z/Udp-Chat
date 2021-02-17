import socket
from multiprocessing import Process
import time

from flask import Flask
import os
from flask import Flask, session, request, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET','POST'])                     
def index():
    liste = []
    with open("log.log",'r') as file:
        data = file.read().split("\n")
    for i in data:
        if i!="":
            print(i.split(":"))
            user = i.split(':')[0]
            message = i.split(':')[1]
            time = i.split(':')[2]
            liste.append((user, message, time))
    return render_template("index.html", liste_message=liste)


def start_flask():
    app.run(port=80,threaded=True,host="0.0.0.0")


if __name__=="__main__":

    proc = Process(target=start_flask)
    proc.start()
    print("Server ok")
    ip=""
    port=1234
    bufferSize  = 1024



    to_send = "Received Ok".encode()

    socket1 = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    socket1.bind((ip, port))

    print("Udp chat online")

    while True:
        bytes = socket1.recvfrom(bufferSize)
        message = bytes[0].decode('utf-8')
        address = bytes[1]
        with open("log.log",'a') as logfile:
            logfile.write(message + ":"+str(time.time())+"\n")
        from_client = f"{message.split(':')[0]} >> {message.split(':')[1]}"
        print(from_client)
        socket1.sendto(to_send, address)

    proc.join()