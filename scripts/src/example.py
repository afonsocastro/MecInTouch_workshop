#!/usr/bin/env python3

import rospy  # Import ROS Python library
from UR10eArm import UR10eArm

# Funções disponíveis:
#
# manipulator.get_current_pose().pose:
# retorna o valor da posição (x,y,z) e da rotação (x,y,z,w) do tool0 em relação ao world
#
# manipulator.get_current_joint_values():
# retorna o valor das 6 juntas do manipulador (em radianos)
#
# manipulator.go_to_joint_state(j1, j2, j3, j4, j5, j6, vel, a):
# comanda o robô para se deslocar até ao destino definido das 6 juntas (j1,j2,j3,j4,j5,j6) em radianos.
# É possível escolher a velocidade e aceleração (vel, a) com que o robô fará esse percurso (entre 0 e 1).
#
# manipulator.go_to_pose_goal(trans_x, trans_y, trans_z, q1, q2, q3, q4, vel, a):
# comanda o robô para se deslocar até ao destino definido pelas coordenadas do tool0 (x,y,z,q1,q2,q3,q4).
# É possível escolher a velocidade e aceleração (vel, a) com que o robô fará esse percurso (entre 0 e 1).

if __name__ == '__main__':

    # Initialization------------------------------------------------
    rospy.init_node('my_node', anonymous=True)  # Initialize the node
    rate = rospy.Rate(1)
    manipulator = UR10eArm()
    # --------------------------------------------------------------

    #  Your code should start from here:

    current_pose = manipulator.move_group.get_current_pose().pose
    print("\nActual TCP Pose: ")
    print(current_pose)

    rospy.sleep(2) #Comando para "dormir" 2 segundos. Pode ser útil se quiserem fazer um compasso de espera entre alguma tarefa."

    current_joints = manipulator.move_group.get_current_joint_values()
    print("\nActual Joint Values:")
    print(current_joints)


    manipulator.go_to_joint_state(0.69, -0.91, 0.84, -1.91, 1.41, -0.08, 0.2, 0.2)
    print("\nCheguei!! :D\n")

    current_joints = manipulator.move_group.get_current_joint_values()
    print("\nNew Joint Values:")
    for n in range(0,6):
        print(current_joints[n])


    rospy.spin()
