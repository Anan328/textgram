try:
    import socket
    s=socket.socket()
    print("textgram-connect with friends!".upper()," ",end="")
    print("owned by:","ANAN")
    s.bind(("localhost",9999))
    s.listen(4)
    print("waiting for connection...")
    while True:
        (c,address)=s.accept()
        c.send(bytes("welcome to textgram-connect with friends! ".upper(),"utf-8"))
        c.send(bytes("owned by: ANAN","utf-8"))
        name = c.recv(1024).decode()
        print("connected with", address, name)
        while True:
            text2 = input("you:")
            c.send(bytes(text2, "utf-8"))
            text=c.recv(1024).decode()
            print(name+":",text)

        c.close()
except Exception as e:
    print("following went wrong:",e)
