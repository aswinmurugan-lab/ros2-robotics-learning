import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatus(Node):

    def __init__(self):
        super().__init__('aswinbot_status')

        self.declare_parameter('robot_name', 'AswinBot')
        self.declare_parameter('speed', 0.5)

        self.publisher = self.create_publisher(
            String,
            '/aswinbot/status',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

    def publish_status(self):

        robot_name = self.get_parameter('robot_name').value
        speed = self.get_parameter('speed').value

        msg = String()
        msg.data = f'{robot_name} is operational. Speed: {speed}'

        self.publisher.publish(msg)

        self.get_logger().info(f'Published: {msg.data}')


def main(args=None):

    rclpy.init(args=args)

    node = RobotStatus()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
