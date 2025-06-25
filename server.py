import socket

# Server setup
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("cc:f9:e4:f9:99:93", 4))
server.listen(1)

print("Waiting for connection...")
client, addr = server.accept()
print(f"Accepted connection from {addr}")
print("*************************************************")
try:
    while True:
        # Receive data from client
        data = client.recv(1024)
        if not data:
            print("Client disconnected.")
            break

        print(f"Received      : {data.decode('utf-8')}")

        # Get input from the user to send a response
        message = input("Enter response: ")
        
        # Send response back to client
        client.send(message.encode("utf-8"))

except KeyboardInterrupt:
    print("\nServer shutting down...")
except OSError as e:
    print(f"Server error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    try:
        client.close()
        server.close()
        print("Server closed.")
    except:
        pass