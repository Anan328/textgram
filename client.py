try:
    import socket
    c=socket.socket()
    c.connect(("localhost",9999))
    print(c.recv(1024).decode())
    print(c.recv(1024).decode())
    name=input("enter your username:")
    print("welcome",name)
    c.send(bytes(name,"utf-8"))
    while True:
        text2=c.recv(1024).decode()
        print("server:",text2)
        text = input("you:")
        c.send(bytes(text, "utf-8"))
except Exception as e:
    print("following went wrong:",e)


