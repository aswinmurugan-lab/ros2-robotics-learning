import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotPublisher(Node):

    def __init__(self):
        super().__init__('robot_publisher')

        self.publisher = self.create_publisher(
            String,
            'robot_status',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        msg = String()
        msg.data = 'Robot is operational!'

        self.publisher.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    robot = RobotPublisher()

    rclpy.spin(robot)

    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
