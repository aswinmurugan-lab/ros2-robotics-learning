import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotSubscriber(Node):

    def __init__(self):
        super().__init__('aswinbot_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/aswinbot/status',
            self.status_callback,
            10
        )

        self.get_logger().info('AswinBot Subscriber Started')

    def status_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')


def main(args=None):

    rclpy.init(args=args)

    node = RobotSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

