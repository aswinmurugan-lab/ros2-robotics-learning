import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class RobotServiceServer(Node):

    def __init__(self):
        super().__init__('aswinbot_service_server')

        self.service = self.create_service(
            Trigger,
            '/aswinbot/check_status',
            self.check_status_callback
        )

        self.get_logger().info('AswinBot Service Server Ready')

    def check_status_callback(self, request, response):

        response.success = True
        response.message = 'AswinBot is operational!'

        self.get_logger().info('Status request received')

        return response


def main(args=None):

    rclpy.init(args=args)

    node = RobotServiceServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
