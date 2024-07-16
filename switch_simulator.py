import socket
import json
import time

# Define the SDN controller address and port
controller_address = ('localhost', 12345)

# List of MAC addresses to test (include some from the whitelist and some not)
mac_addresses = ['00:00:00:00:00:01', '00:00:00:00:00:02', '00:00:00:00:00:03']

try:
    # Connect to the SDN controller
    switch_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    switch_socket.connect(controller_address)
    print(f"Connected to SDN controller at {controller_address}")

    for mac_address in mac_addresses:
        # Send MAC address to the SDN controller in JSON format
        data = json.dumps({'mac_address': mac_address}).encode()
        switch_socket.sendall(data)

        # Receive response from the SDN controller
        response = switch_socket.recv(1024).decode()
        print(f"Received response for MAC {mac_address}: {response}")

        # Simulate delay between sending MAC addresses
        time.sleep(1)

finally:
    print("Closing connection to SDN controller...")
    switch_socket.close()


Connected to SDN controller at ('localhost', 12345)
Received response for MAC 00:00:00:00:00:01: {"status": "allowed"}
Received response for MAC 00:00:00:00:00:02: {"status": "allowed"}
Received response for MAC 00:00:00:00:00:03: {"status": "denied"}
Closing connection to SDN controller...
