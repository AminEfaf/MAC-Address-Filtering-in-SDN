# Implementing MAC Address Filtering in Software-Defined Networking (SDN)

Software-Defined Networking (SDN) has revolutionized the networking landscape by decoupling the control plane from the data plane, allowing for more flexible and efficient network management. This separation facilitates centralized control, dynamic configuration, and improved scalability, making it an ideal architecture for modern network environments.

In traditional networking, MAC (Media Access Control) address filtering is a fundamental security measure used to control access to the network at the data link layer. By allowing or denying network access based on the MAC addresses of devices, administrators can enhance network security, prevent unauthorized access, and manage network resources more effectively.

This project aims to implement MAC address filtering within an SDN framework. By integrating MAC address filtering capabilities into the SDN controller, we leverage the centralized control and programmability of SDN to enforce security policies more dynamically and efficiently. This approach not only simplifies the management of network access controls but also enhances the adaptability of the network to changing security requirements.

---

## Project Overview

This project focuses on integrating traditional MAC address filtering into an SDN environment by developing a dynamic and centralized solution. The main components include:

- **SDN Controller**: Implements logic for MAC address filtering and communicates with network devices to enforce defined rules.
- **Switch Simulator**: Simulates network switches to test and validate the MAC address filtering functionality.

By combining these components, this project demonstrates the flexibility and efficiency of using SDN to enhance traditional network security measures.

---

## Features

1. Centralized control of MAC address filtering rules.
2. Dynamic addition and removal of allowed or denied MAC addresses.
3. Real-time enforcement of security policies.
4. Simulation environment for testing and validation.

---

## Requirements

- Python 3.6 or later.
- Basic understanding of Software-Defined Networking concepts.

---

## How to Use

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd mac_filtering_sdn
    ```

2. **Run the SDN Controller:**

    ```bash
    python3 sdn_controller.py
    ```

3. **Run the Switch Simulator:**

    ```bash
    python3 switch_simulator.py
    ```

4. Modify the SDN Controller’s configuration to add or remove MAC addresses for filtering.

---

## Feedback

We’d love to hear your thoughts and suggestions! Feel free to reach out or open an issue in this repository.
