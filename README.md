# Network-Programming-and-Bluetooth-Client-Server-Communication
A Python implementation of Bluetooth client-server communication using RFCOMM sockets for real-time bidirectional messaging.
# 🔵 Bluetooth Client-Server Communication

A Python implementation of Bluetooth client-server communication using RFCOMM sockets for real-time bidirectional messaging.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project demonstrates how to establish a Bluetooth connection between two devices using Python's socket programming. The implementation uses the RFCOMM protocol to create a reliable, bidirectional communication channel similar to serial port communication.

**Key Components:**
- **Server**: Listens for incoming Bluetooth connections
- **Client**: Initiates connection and communicates with the server
- **Protocol**: RFCOMM (Serial Port Profile) over Bluetooth

## ✨ Features

- 🔗 **Bidirectional Communication**: Both client and server can send and receive messages
- 🛡️ **Error Handling**: Robust exception handling for connection failures
- 📡 **RFCOMM Protocol**: Uses Bluetooth Serial Port Profile for reliable data transmission
- 🔄 **Real-time Messaging**: Interactive chat-like communication
- 🖥️ **Cross-platform**: Works on Linux, Windows, and macOS (with proper Bluetooth support)
- 🚀 **Easy Setup**: Simple configuration with MAC address and channel

## 📋 Requirements

### System Requirements
- Python 3.6 or higher
- Bluetooth adapter on both devices
- Operating System with Bluetooth support:
  - **Linux**: BlueZ stack
  - **Windows**: Windows Bluetooth stack
  - **macOS**: Built-in Bluetooth support

### Python Dependencies
```bash
# No additional pip packages required
# Uses built-in socket module
```

### Hardware Requirements
- Bluetooth-enabled devices (computers, Raspberry Pi, etc.)
- Bluetooth version 2.0 or higher recommended

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bluetooth-client-server.git
   cd bluetooth-client-server
   ```

2. **Verify Bluetooth Support**
   ```bash
   # Linux
   hciconfig
   
   # Windows
   # Check Device Manager for Bluetooth adapters
   
   # macOS
   # Check System Preferences > Bluetooth
   ```

3. **Get your Bluetooth MAC Address**
   ```bash
   # Linux
   hciconfig
   
   # Windows
   ipconfig /all
   
   # macOS
   system_profiler SPBluetoothDataType
   ```

## 🎮 Usage

### Step 1: Configure MAC Address
Edit both `server.py` and `client.py` files to use your device's MAC address:

```python
# Replace with your server device's MAC address
server.bind(("YOUR_MAC_ADDRESS_HERE", 4))
```

### Step 2: Start the Server
```bash
python server.py
```
You should see:
```
Waiting for connection...
```

### Step 3: Start the Client
```bash
python client.py
```
You should see:
```
Connecting to server...
Connected successfully!
```

### Step 4: Start Messaging
- Type messages in either terminal
- Press Enter to send
- Type 'quit' in client to exit gracefully

## 📁 Project Structure

```
bluetooth-client-server/
│
├── server.py              # Bluetooth server implementation
├── client.py              # Bluetooth client implementation
├── README.md              # Project documentation
├── presentation/          # Educational materials
│   ├── bluetooth_networking.html
│   └── slides_content.md
├── examples/              # Example usage scripts
│   ├── basic_server.py
│   └── basic_client.py
└── docs/                  # Additional documentation
    ├── troubleshooting.md
    └── protocol_details.md
```

## 🔧 How It Works

### Server Architecture
```python
# 1. Create Bluetooth RFCOMM socket
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# 2. Bind to MAC address and channel
server.bind(("MAC_ADDRESS", 4))

# 3. Listen for connections
server.listen(1)

# 4. Accept client connection
client, addr = server.accept()
```

### Client Architecture
```python
# 1. Create matching socket
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# 2. Connect to server
client.connect(("SERVER_MAC_ADDRESS", 4))

# 3. Send/receive data
client.send(message.encode('utf-8'))
data = client.recv(1024)
```

### Communication Flow
1. **Server Setup**: Binds to MAC address and listens on channel 4
2. **Client Connection**: Connects to server using MAC address
3. **Data Exchange**: Bidirectional message exchange
4. **Graceful Shutdown**: Proper socket cleanup on exit

## 🛠️ Troubleshooting

### Common Issues

#### "Connection Refused" Error
```bash
# Solution 1: Check if server is running first
python server.py

# Solution 2: Verify MAC address is correct
hciconfig  # Linux
```

#### "Bluetooth not available" Error
```bash
# Linux: Start Bluetooth service
sudo systemctl start bluetooth

# Check Bluetooth status
sudo systemctl status bluetooth
```

#### "Permission denied" Error
```bash
# Linux: Add user to bluetooth group
sudo usermod -a -G bluetooth $USER

# Or run with sudo (not recommended for production)
sudo python server.py
```

#### "Device not found" Error
- Ensure both devices have Bluetooth enabled
- Check if devices are discoverable
- Verify MAC address format: `XX:XX:XX:XX:XX:XX`

### Debug Mode
Enable debug output by uncommenting print statements in the code:

```python
print("Waiting for connection...")
print(f"Accepted connection from {addr}")
print(f"Message: {data.decode('utf-8')}")
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Include error handling
- Test on multiple platforms
- Update documentation

## 📚 Educational Resources

- [Bluetooth Protocol Stack](docs/protocol_details.md)
- [RFCOMM Specification](https://www.bluetooth.com/specifications/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)
- [Interactive Presentation](presentation/bluetooth_networking.html)

## 🔍 Advanced Usage

### Multiple Clients
To support multiple clients, modify the server to use threading:

```python
import threading

def handle_client(client_socket, address):
    # Handle individual client
    pass

# Accept multiple connections
while True:
    client, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client, addr))
    client_thread.start()
```

### Security Considerations
- Implement authentication mechanisms
- Use encryption for sensitive data
- Validate input data
- Implement rate limiting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Python Socket Programming Documentation
- Bluetooth SIG for protocol specifications
- Community contributors and testers

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/voltaireishimwe/bluetooth-client-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/voltaireishimwe/bluetooth-client-server/discussions)
- **Email**: voltaireishimwe@gmail.com

---

**⭐ If this project helped you, please give it a star!**

**🔄 Made with Python and Bluetooth by Voltaire ISHIMWE**
