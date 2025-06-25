
import socket

# Client setup
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_address = ("cc:f9:e4:f9:99:93", 4)

try:
    while True:
        # Get input from the user to send a message
        message = input("Enter message: ")
        
        # Encode and send the message to the server
        client.send(message.encode('utf-8'))

        # Receive data from the server
        data = client.recv(1024)
        if not data:
            print("Server disconnected.")
            break
        # Decode and print the received message
        print(f"Message: {data.decode('utf-8')}")

except OSError as e:
    pass 
finally:
    if client:
        client.close()
        #print("Client connection closed.")

