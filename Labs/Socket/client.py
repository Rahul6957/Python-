import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server's IP address
client.connect(("192.168.1.90", 5000))

print("Connected to server!")


# Function to receive messages
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                print("Server disconnected.")
                break

            print("\nServer:", message)

        except:
            break


# Start receiving messages in background
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


# Client sends messages
while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())


client.close()