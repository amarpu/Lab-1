from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    publisher_node = Node(
        package='mypubsub',
        executable='publisher',
        name='pub1',
        remappings=[('chatter', 'chatter1')]
    )

    subscriber_node = Node(
        package='mypubsub',
        executable='subscriber',
        name='sub1',
        remappings=[('chatter', 'chatter1')]
        
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
