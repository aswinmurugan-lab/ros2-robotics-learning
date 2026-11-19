import rclpy
from rclpy.node import Node


class RobotStatus(Node):

    def __init__(self):
        super().__init__('robot_status')

        self.timer = self.create_timer(1.0, self.status_callback)

    def status_callback(self):
        self.get_logger().info('Robot is operational!')


def main(args=None):
    rclpy.init(args=args)

    robot = RobotStatus()

    rclpy.spin(robot)

    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
