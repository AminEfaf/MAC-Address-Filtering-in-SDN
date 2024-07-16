### Implementing MAC Address Filtering in Software-Defined Networking (SDN)

Software-Defined Networking (SDN) has revolutionized the networking landscape by decoupling the control plane from the data plane, allowing for more flexible and efficient network management. This separation facilitates centralized control, dynamic configuration, and improved scalability, making it an ideal architecture for modern network environments. 🌐

In traditional networking, MAC (Media Access Control) address filtering is a fundamental security measure used to control access to the network at the data link layer. By allowing or denying network access based on the MAC addresses of devices, administrators can enhance network security, prevent unauthorized access, and manage network resources more effectively. 🔒

This project aims to implement MAC address filtering within an SDN framework. By integrating MAC address filtering capabilities into the SDN controller, we leverage the centralized control and programmability of SDN to enforce security policies more dynamically and efficiently. This approach not only simplifies the management of network access controls but also enhances the adaptability of the network to changing security requirements. ⚙️

### Objectives

1. **Design and Development**: Develop an SDN controller that can implement MAC address filtering rules, allowing for the dynamic addition and removal of allowed and denied MAC addresses.
   
2. **Simulation and Testing**: Create a switch simulator to test the SDN controller’s functionality, ensuring that the MAC address filtering rules are enforced correctly.

3. **Evaluation**: Assess the performance and security benefits of the implemented MAC address filtering in a simulated network environment, demonstrating the effectiveness and flexibility of SDN-based security controls.

### Components of the Project

- **SDN Controller** (`sdn_controller.py`): This component is responsible for managing the network's control plane, implementing the logic for MAC address filtering, and communicating with the network devices to enforce the defined rules. 🖥️

- **Switch Simulator** (`switch_simulator.py`): A simulated network switch that interacts with the SDN controller, used to test and validate the functionality of the MAC address filtering implementation. 🖧

By combining these components, this project provides a comprehensive solution for integrating MAC address filtering into an SDN environment, enhancing both the security and manageability of modern networks. The resulting system will demonstrate how SDN can be leveraged to implement traditional network security measures in a more flexible and dynamic manner. 🌟
