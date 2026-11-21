import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from example_interfaces.action import Fibonacci


class RobotActionClient(Node):

    def __init__(self):
        super().__init__('aswinbot_action_client')

        self.action_client = ActionClient(
            self,
            Fibonacci,
            '/aswinbot/fibonacci'
        )

        self.finished = False

    def send_goal(self):

        goal_msg = Fibonacci.Goal()
        goal_msg.order = 5

        self.get_logger().info('Sending Fibonacci goal: 5')

        self.action_client.wait_for_server()

        self.send_goal_future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        self.send_goal_future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            self.finished = True
            return

        self.get_logger().info('Goal accepted')

        self.result_future = goal_handle.get_result_async()

        self.result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback.sequence

        self.get_logger().info(f'Feedback: {feedback}')

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Final result: {result.sequence}'
        )

        self.finished = True


def main(args=None):

    rclpy.init(args=args)

    node = RobotActionClient()

    node.send_goal()

    while rclpy.ok() and not node.finished:
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
