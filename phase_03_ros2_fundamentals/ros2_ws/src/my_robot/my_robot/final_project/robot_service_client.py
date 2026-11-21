import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class RobotServiceClient(Node):

    def __init__(self):
        super().__init__('aswinbot_service_client')

        self.client = self.create_client(
            Trigger,
            '/aswinbot/check_status'
        )

        self.get_logger().info('Waiting for AswinBot service...')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

    def send_request(self):

        request = Trigger.Request()

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(self, future)

        return future.result()


def main(args=None):

    rclpy.init(args=args)

    node = RobotServiceClient()

    response = node.send_request()

    if response is not None:
        node.get_logger().info(
            f'Success: {response.success}, Message: {response.message}'
        )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

