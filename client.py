#client program
import socket


if __name__ == "__main__":
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP, PORT))

    print("welcome to the python DB menu")
    print("\n")

    key = False
    while key == False:
        print(
            "1.find customer\n2.add customer\n3.delete customer\n4.update customer age\n5.update customer address\n6.update customer phone\n7.print report\n8.exit")
        selection = input("enter selection:")
        if selection == "1":
            x = input('Enter name of customer:')
            server.send(bytes(selection, "utf-8"))
            server.send(bytes(x, "utf-8"))
            response = server.recv(1024)
            response = response.decode("utf-8")
            print(f"Server: {response}")

            # pairAnswer=(selection+"::"+x)
            # server.send(bytes(pairAnswer, "utf-8"))


    buffer =server.recv(1024)
    buffer=buffer.decode("utf-8")
    buffer2 = server.recv(1024)
    buffer2 = buffer2.decode("utf-8")
    print(f"Server: {buffer}")
    print(f"Server: {buffer2}")


