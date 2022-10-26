from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(): #Function name must be the same as written here for the ros functionality to launch the program.
    ld = LaunchDescription()

    remap_number_topic = ("number","my_number")

    number_publisher_node = Node(
        package="activity_three",
        executable="number_publisher",
        name="my_number_publisher",
        remappings=[
            remap_number_topic
        ],
        parameters=[
            {"number_to_publish":4},
            {"publish_frequency":5.0}
        ]
    )#Services and topics are mapped in a same way. Both are mapped as tuples. Parameters are mapped similarly but as dictionary.

    number_counter_node = Node(
        package="activity_three",
        executable="number_counter",
        name="my_number_counter",
        remappings=[
            remap_number_topic,
            ("number_count", "my_number_count")
        ]
    )

    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)
    
    return ld