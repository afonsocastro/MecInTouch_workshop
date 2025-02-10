# MecInTouch_workshop

pre requisitos (windows 11 Home 64 bit)
Instalar PyChamr community edition (https://www.jetbrains.com/pycharm/download/?section=windows) é preciso fazer scroll down
Configurar WSL2
Download Ubuntu 20.04.2 LTS
Entrar no ubuntu (definir user e password)



sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc


sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt install python3-rosdep
sudo rosdep init
rosdep update



mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH Objetivo: /home/youruser/catkin_ws/src:/opt/ros/noetic/share


cd ~/catkin_ws/src
git clone https://github.com/afonsocastro/MecInTouch_workshop.git
cd ~/catkin_ws/
catkin_make


