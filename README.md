# MecInTouch Workshop Robótica
## Índice

1. [Pre-requisitos](#prerequisites)
2. [Instalação](#installation)
3. [Troubleshoot](#troubleshoot)


## Pre-requisitos

Entrar no ubuntu (definir user e password)

## Instalação
No terminal Ubuntu (Linux), correr cada um dos seguintes commandos, um a um:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt-get install dos2unix
sudo rosdep init
rosdep update
sudo apt install ros-noetic-moveit ros-noetic-industrial-robot-status-interface ros-noetic-scaled-controllers ros-noetic-pass-through-controllers ros-noetic-ur-client-library ros-noetic-ur-msgs ros-noetic-velocity-controllers ros-noetic-force-torque-sensor-controller socat
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make 
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export LIBGL_ALWAYS_SOFTWARE=1" >> ~/.bashrc 
echo "export LIBGL_ALWAYS_INDIRECT=0" >> ~/.bashrc 
source ~/.bashrc
```
Fechar o terminal Ubuntu (Linux): ``exit``

Re-abrir o terminal Ubuntu (Linux), e correr o comando:
```echo $ROS_PACKAGE_PATH``` que deve retornar o seguinte path:
```/home/[your_user]/catkin_ws/src:/opt/ros/noetic/share``` . 
Se sim, então pode-se executar os seguintes 4 comandos:
```
cd ~/catkin_ws/src
git clone https://github.com/afonsocastro/MecInTouch_workshop.git
cd ~/catkin_ws/
catkin_make
```

# Troubleshoot
Cada novo script python criado deve conter SEMPRE, na sua primeira linha: ```#!/usr/bin/env python3```. 
Para além disso, antes de poder ser executado (principalmente quando se inicializa um novo ROS Node), necessita das 2 seguintes permissões:

```
chmod 777 [file_name].py
dos2unix [file_name].py
```
Após estes 2 comandos, já se pode lançar o novo ROS Node (python script):

```
rosrun [package_name] [file_name].py
```