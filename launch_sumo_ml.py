#!/usr/bin/env python3

"""Launch file for SUMO simulation with ML bridge and rosbag recording."""

from pathlib import Path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    """Create launch description for SUMO ML setup."""
    # Declare all launch arguments with defaults
    sumocfg_arg = DeclareLaunchArgument(
        'sumocfg',
        default_value=str(Path.home() / 'testing/test.sumocfg'),
        description='Path to SUMO configuration file'
    )
    
    port_arg = DeclareLaunchArgument(
        'port',
        default_value='1337',
        description='Remote port for SUMO-ROS communication'
    )
    
    bag_name_arg = DeclareLaunchArgument(
        'bag_name',
        default_value='sumo_run',
        description='Name for the recorded rosbag'
    )
    
    # SUMO-GUI process with remote control and auto-start
    sumo_process = ExecuteProcess(
        cmd=['sumo-gui',
             '-c', LaunchConfiguration('sumocfg'),
             '--remote-port', LaunchConfiguration('port'),
             '--start',
             '--quit-on-end',
             '--window-size', '1280,720'],
        name='sumo_gui',
        output='screen',
        on_exit=[
            ExecuteProcess(
                cmd=['killall', 'ros2', 'bag'],
                name='cleanup_rosbag',
                shell=True
            )
        ]
    )
    
    # Bridge node
    bridge_node = Node(
        package='sumo_bridge',
        executable='bridge',
        name='sumo_bridge',
        parameters=[{'port': LaunchConfiguration('port')}],
        output='screen'
    )
    
    # Rosbag recorder
    rosbag_process = ExecuteProcess(
        cmd=['ros2','bag','record','-o', LaunchConfiguration('bag_name'), 
             '--compression-mode','file','--compression-format','zstd', 
             '/odom','/traffic_signals'],
        name='rosbag_recorder',
        output='screen'
    )
    
    return LaunchDescription([
        sumocfg_arg,
        port_arg,
        bag_name_arg,
        sumo_process,
        bridge_node,
        rosbag_process
    ])
