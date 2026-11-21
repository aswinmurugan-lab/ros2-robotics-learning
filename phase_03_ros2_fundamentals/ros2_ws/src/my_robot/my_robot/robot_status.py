import rclpy
from rclpy.node import Node


class RobotStatus(Node):

    def __init__(self):
        super().__init__('robot_status')

        self.declare_parameter('robot_name', 'TurtleBot')
        self.declare_parameter('speed', 0.5)

        self.timer = self.create_timer(1.0, self.status_callback)

    def status_callback(self):
        robot_name = self.get_parameter('robot_name').value
        speed = self.get_parameter('speed').value

        self.get_logger().info(
            f'{robot_name} is operational! Speed: {speed}'
        )


def main(args=None):
    rclpy.init(args=args)

    robot = RobotStatus()

    rclpy.spin(robot)

    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
