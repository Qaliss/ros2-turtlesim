import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleMirror(Node):
    def __init__(self):
        super().__init__('turtle_follow')

        #Subscribe to turtle1's cmd_vel topic
        self.subscription = self.create_subscription(Twist, 'turtle1/cmd_vel', self.listener_callback, 10)

        #Publish commands to turtle2's cmd_vel topic
        self.publisher = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Mirroring: Linear = {msg.linear.x}, Angular = {msg.angular.z}')
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMirror()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == 'main':
    main()