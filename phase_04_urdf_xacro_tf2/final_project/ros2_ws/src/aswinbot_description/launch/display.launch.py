from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    robot_description = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('aswinbot_description'),
            'urdf',
            'aswinbot.urdf.xacro'
        ])
    ])

    return LaunchDescription([
	Node(
   	 package='robot_state_publisher',
   	 executable='robot_state_publisher',
   	 name='robot_state_publisher',
   	 parameters=[{
       		 'robot_description': robot_description
   	 }]
    ),
	Node(
   	 package='joint_state_publisher_gui',
   	 executable='joint_state_publisher_gui',
   	 name='joint_state_publisher_gui'
    ),
	Node(
   	 package='rviz2',
   	 executable='rviz2',
   	 name='rviz2',
	 arguments=[
		'-d',
		PathJoinSubstitution([
			FindPackageShare('aswinbot_description'),
			'rviz',
			'aswinbot.rviz'
		])
	]
    ),
 ])
