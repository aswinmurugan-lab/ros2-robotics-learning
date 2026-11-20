import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class RobotServiceServer(Node):

    def __init__(self):
        super().__init__('robot_service_server')

        self.service = self.create_service(
            AddTwoInts,
            'add_two_numbers',
            self.add_numbers_callback
        )

        self.get_logger().info('Addition service is ready!')

    def add_numbers_callback(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f'Received: {request.a} + {request.b}'
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    robot = RobotServiceServer()

    rclpy.spin(robot)

    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
