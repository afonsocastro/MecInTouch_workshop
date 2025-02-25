#!/usr/bin/env python3

import rospy  # Import ROS Python library
from std_msgs.msg import String  # Import standard message type
from UR10eArm import UR10eArm

if __name__ == '__main__':
    rospy.init_node('my_node', anonymous=True)  # Initialize the node
    pub = rospy.Publisher('/chatter', String, queue_size=10)  # Create a publisher
    rate = rospy.Rate(1)  # Set loop rate to 1 Hz (1 message per second)
    manipulator = UR10eArm()
    move_group = manipulator.move_group

    while not rospy.is_shutdown():

        current_pose = move_group.get_current_pose().pose
        print("current_pose")
        print(current_pose)

        current_joints = move_group.get_current_joint_values()
        print("current_joints")
        print(current_joints)

        rate.sleep()  # Wait for the next iteration