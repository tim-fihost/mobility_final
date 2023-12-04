import rclpy
from std_msgs.msg import String
import socket

class SocketROSNode:

    def init(self, host='0.0.0.0', port=12345):
        self.node = rclpy.create_node('socket_ros_node')
        self.publisher = self.node.create_publisher(String, 'socket_ros_topic', 10)

        # Set up the socket server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()

        self.node.get_logger().info(f"Socket server listening on {host}:{port}")

        # Accept a connection from a client
        self.client_socket, self.client_address = self.server_socket.accept()
        self.node.get_logger().info(f"Accepted connection from {self.client_address}")

    def receive_data(self):
        try:
            while rclpy.ok():
                data = self.client_socket.recv(1024)
                if not data:
                    break

                # Process the received data
                decoded_data = data.decode('utf-8')
                self.node.get_logger().info(f"Received data: {decoded_data}")

                # Publish the data as a ROS 2 message
                msg = String()
                msg.data = decoded_data
                self.publisher.publish(msg)

        except Exception as e:
            self.node.get_logger().error(f"Error receiving data: {str(e)}")

    def run(self):
        try:
            self.receive_data()
        finally:
            # Clean up resources when the node is shut down
            self.node.destroy_node()
            rclpy.shutdown()

if name == 'main':
    rclpy.init()
    # Use the IP address of your computer running the ROS 2 node
    host_ip_address = '192.168.1.100'  # Replace with your computer's IP address
    socket_ros_node = SocketROSNode(host=host_ip_address)
    socket_ros_node.run()