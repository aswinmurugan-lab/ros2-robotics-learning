
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.executors import MultiThreadedExecutor
from example_interfaces.action import Fibonacci


class RobotActionServer(Node):

    def __init__(self):
        super().__init__('aswinbot_action_server')

        self.action_server = ActionServer(
            self,
            Fibonacci,
            '/aswinbot/fibonacci',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        self.get_logger().info('AswinBot Action Server Ready')

    def goal_callback(self, goal_request):
        self.get_logger().info(
            f'Received goal: {goal_request.order}'
        )
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancellation request')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):

        self.get_logger().info('Executing Fibonacci goal')

        feedback_msg = Fibonacci.Feedback()
        result = Fibonacci.Result()

        sequence = [0, 1]

        for i in range(2, goal_handle.request.order):

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result.sequence = sequence[:goal_handle.request.order]
                self.get_logger().info('Goal canceled')
                return result

            time.sleep(1.0)

            sequence.append(sequence[i - 1] + sequence[i - 2])

            feedback_msg.sequence = sequence.copy()
            goal_handle.publish_feedback(feedback_msg)

            self.get_logger().info(f'Feedback: {sequence}')

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
            result.sequence = sequence[:goal_handle.request.order]
            return result

        result.sequence = sequence[:goal_handle.request.order]

        goal_handle.succeed()

        self.get_logger().info(f'Final result: {result.sequence}')

        return result


def main(args=None):

    rclpy.init(args=args)

    node = RobotActionServer()

    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(node)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
