Mostly ROS2 functions are in voice_rec folder

SocketROSNode
The SocketROSNode is a ROS 2 node that establishes a socket server to receive data from a client and publishes the received data as ROS 2 messages.

Prerequisites
ROS 2 installed and configured
Python 3 installed
Dependencies: rclpy, std_msgs
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd <project_directory>
Usage
Launching the Node
Ensure that your ROS 2 environment is sourced:

bash
Copy code
source /path/to/ros2/install/setup.bash
Run the node:

bash
Copy code
python socket_ros_node.py
Configuration
You can configure the node by providing the host IP address and port when initializing the SocketROSNode class. By default, the host is set to '0.0.0.0' (all available interfaces), and the port is set to 12345.

python
Copy code
# Example: Initialize SocketROSNode with a specific host and port
socket_ros_node = SocketROSNode(host='192.168.1.100', port=12345)
Customization
Feel free to customize the node according to your specific requirements. You can modify the message type or add additional processing steps for the received data.

Node Behavior
The node initializes a ROS 2 publisher to publish messages to the 'socket_ros_topic'.
A socket server is set up to listen for incoming connections on the specified host and port.
Once a client connects, the received data is processed and published as ROS 2 messages.
Cleaning Up
The node gracefully shuts down when interrupted (e.g., using Ctrl + C). It also cleans up resources, ensuring a proper shutdown.

Contributing
If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
