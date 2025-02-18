# MecInTouch_workshop
## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Troubleshoot](#troubleshoot)


## Prerequisites
pre requisitos (windows 11 Home 64 bit)
Instalar PyChamr community edition (https://www.jetbrains.com/pycharm/download/?section=windows) é preciso fazer scroll down
Configurar WSL2
Download Ubuntu 20.04.2 LTS
Entrar no ubuntu (definir user e password)

## Installation
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update
sudo apt install ros-noetic-moveit ros-noetic-industrial-robot-status-interface ros-noetic-scaled-controllers ros-noetic-pass-through-controllers ros-noetic-ur-client-library ros-noetic-ur-msgs ros-noetic-velocity-controllers ros-noetic-force-torque-sensor-controller socat
sudo apt-get install xterm
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make 
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export LIBGL_ALWAYS_SOFTWARE=1" >> ~/.bashrc 
echo "export LIBGL_ALWAYS_INDIRECT=0" >> ~/.bashrc 
source ~/.bashrc
```
Close Ubuntu (Linux) terminal: ``exit``
Reopen Ubuntu (Linux) terminal.

```echo $ROS_PACKAGE_PATH```

It should return something like this: /home/youruser/catkin_ws/src:/opt/ros/noetic/share
ITS NOT RETURNING!!!!
```
cd ~/catkin_ws/src
git clone https://github.com/afonsocastro/MecInTouch_workshop.git
cd ~/catkin_ws/
catkin_make
```

# Troubleshoot
if 
```
[ INFO] [1739396956.584309934]: Initializing urdriver 
/usr/bin/env: ‘python3\r’: No such file or directory 
[gripper_action_server-9] process has died [pid 42678, exit code 127
```

you should 
```
sudo apt-get install dos2unix
dos2unix /home/afonsocastro/catkin_ws/src/larcc_drivers/gripper_action_server/src/gripper_action_server_node.py
```
and verify the shebang line of the file:
```
#!/usr/bin/env python3
```
Lastly:
```
chmod +x /home/afonsocastro/catkin_ws/src/larcc_drivers/gripper_action_server/src/gripper_action_server_node.py
cd /home/afonsocastro/catkin_ws
catkin_make
source devel/setup.bash
```

OTHER thing, maybe you should be looking for this:
```
sudo ip route add 192.168.56.0/24 via 172.19.96.1
```
and then see ```ip route```
this should always be working
```
ping 192.168.56.2
```