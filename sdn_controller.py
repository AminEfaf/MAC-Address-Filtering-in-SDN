import socket
import json

# Define the SDN controller address and port
controller_address = ('localhost', 12345)

# Define the MAC address whitelist (example)
mac_whitelist = ['00:00:00:00:00:01', '00:00:00:00:00:02']

# Create a socket to listen for incoming connections from switches
controller_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
controller_socket.bind(controller_address)
controller_socket.listen(1)

print(f"SDN Controller listening on {controller_address[0]}:{controller_address[1]}...")

try:
    # Accept incoming connections
    switch_socket, switch_address = controller_socket.accept()
    print(f"Switch connected: {switch_address}")

    while True:
        data = switch_socket.recv(1024)
        if not data:
            break
        received_data = json.loads(data.decode())
        print(f"Received data: {received_data}")

        # Extract MAC address from received data
        if 'mac_address' in received_data:
            mac_address = received_data['mac_address']
            print(f"MAC Address: {mac_address}")

            # Check if MAC address is in the whitelist
            if mac_address in mac_whitelist:
                response = {'status': 'allowed'}
            else:
                response = {'status': 'denied'}

            # Send response back to the switch
            switch_socket.sendall(json.dumps(response).encode())

finally:
    print("Closing connections...")
    switch_socket.close()
    controller_socket.close()






