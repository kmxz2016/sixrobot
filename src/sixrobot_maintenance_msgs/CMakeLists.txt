cmake_minimum_required(VERSION 2.8.3)
project(sixrobot_maintenance_msgs)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(DIRECTORY msg FILES
  CalibrateArmData.msg
  CalibrateArmEnable.msg
  TareData.msg
  TareEnable.msg
  UpdateSource.msg
  UpdateSources.msg
  UpdateStatus.msg
)

generate_messages(DEPENDENCIES
  std_msgs
)

catkin_package(CATKIN_DEPENDS
  message_runtime
  std_msgs
)
