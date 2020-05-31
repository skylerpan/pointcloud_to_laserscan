import yaml

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        # Node(
        #     package='tf2_ros',
        #     node_executable='static_transform_publisher',
        #     node_name='static_transform_publisher0',
        #     arguments='-0.15 0.15 0.15 0 0 0 1 laser_frame0 laser_frame'
        # ),
        # Node(
        #     package='tf2_ros',
        #     node_executable='static_transform_publisher',
        #     node_name='static_transform_publisher1',
        #     arguments='0.15 0.15 0.15 0 0 0 1 laser_frame0 laser_frame'
        # ),
        Node(
            package='pointcloud_to_laserscan',
            executable='laserscan_to_pointcloud_node',
            name='laserscan_to_pointcloud_node_0',
            remappings=[('scan_in', '/scan0'),
                        ('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
            parameters=[{'target_frame': 'laser_frame0', 'transform_tolerance': 0.1}]
        ),
        Node(
            package='pointcloud_to_laserscan',
            executable='laserscan_to_pointcloud_node',
            name='laserscan_to_pointcloud_node_1',
            remappings=[('scan_in', '/scan1'),
                        ('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
            parameters=[{'target_frame': 'laser_frame0', 'transform_tolerance': 0.1}]
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', [LaunchConfiguration(variable_name='scanner'), '/cloud']),
                        ('scan','/scan')],
            parameters=[{
                'target_frame': 'laser_frame0',
                'transform_tolerance': 0.01,
                'min_height': 0.0,
                'max_height': 1.0,
                'angle_min': -1.5708,  # -M_PI/2
                'angle_max': 1.5708,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.45,
                'range_max': 4.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )

    ])
