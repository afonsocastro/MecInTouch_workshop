#! /usr/bin/python3

from UR10eArm import UR10eArm
import rospy

if __name__ == '__main__':
    rospy.init_node("move_group_python_interface", anonymous=True)
    # --------------------------------------------------------------------
    # -------------------------initialization-----------------------------
    # --------------------------------------------------------------------
    tutorial = UR10eArm()
    move_group = tutorial.move_group

    current_pose = move_group.get_current_pose().pose
    print("current_pose")
    print(current_pose)

    current_joints = move_group.get_current_joint_values()
    print("current_joints")
    print(current_joints)

    state = tutorial.go_to_joint_state(0.01725006103515625, -1.9415461025633753, 1.8129728476153772,
                                       -1.5927173099913539, -1.5878670851336878, 0.03150486946105957, 1, 1)


    rospy.spin()
