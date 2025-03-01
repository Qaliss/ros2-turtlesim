from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'turtlesim',
            executable = 'turtlesim_node',
            name = 'turtlesim'
        ),

        ExecuteProcess(
            cmd=['ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn',
            '{"x": 4.0, "y": 4.0, "theta": 0.0, "name": "turtle2"}'],
            output = 'screen'
        ),

        Node(
            package = 'multi_turtle',
            executable = 'turtle_follow',
            name = 'turtle_follow'
        ),

        ExecuteProcess(
            cmd=['ros2', 'run', 'turtlesim', 'turtle_teleop_key'],
            output = 'screen'
        ),
    ])
