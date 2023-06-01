from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import yaml
from yaml import load, Loader

def generate_launch_description():
    commonFilePath = os.path.join(get_package_share_directory('cpp_safetyserver'), 'launch/common.yaml')
    with open(commonFilePath, 'r') as f:
        data = yaml.load(f, Loader=Loader)
    return LaunchDescription([
        Node(
            package="cpp_safetyserver",
            namespace=data['node_prop']['namespace'],
            executable="server",
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    "service_Safety_nodeName" : data['service_Safety']['nodeName'], 
                    "service_Safety_serviceName" : data['service_Safety']['serviceName'], 
                    "mainNodeName" : data['node_prop']['nodeName'], 
                    "mainNamespace" : data['node_prop']['namespace'], 
                }
            ]
        )
    ])