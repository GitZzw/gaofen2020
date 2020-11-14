#!/usr/bin/python
# coding: utf-8

import socket
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import PoseStamped

target_corner_msg = PoseStamped()

def clint():
    rospy.init_node('yolo_clint', anonymous=True)
    yolo_target_pub = rospy.Publisher('yolo_target_corner', PoseStamped, queue_size=1)

    rate = rospy.Rate(30)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    print ('connect state: ', s.connect_ex(('127.0.0.1', 8000)))

    while not rospy.is_shutdown():
        target_get_flag = False
        receive_msg = s.recv(120).decode()
        # print (receive_msg)
        if(len(receive_msg)==0):
            continue
        msg = receive_msg.split(',')
        #print(msg)
        if msg[0] == '1':
            target_get_flag = True
            #print ("target corner")
            """ QuaternionStamped.x, y, z, w = xmin, ymin, xmax, ymax,   x = time, z= id """
            #target_corner_msg.header.stamp = rospy.get_rostime()
            target_corner_msg.pose.orientation.x = float(msg[1])
            target_corner_msg.pose.orientation.y = float(msg[2])
            target_corner_msg.pose.orientation.z = float(msg[3])
            target_corner_msg.pose.orientation.w = float(msg[4])
            target_corner_msg.pose.position.x = float(msg[5]) #time
            target_corner_msg.pose.position.z = float(msg[6]) #id

        if not target_get_flag:
           # print (" target not found ... ")
            #target_corner_msg.header.stamp = rospy.get_rostime()
            target_corner_msg.pose.orientation.x = -1
            target_corner_msg.pose.orientation.y = 0
            target_corner_msg.pose.orientation.z = 0
            target_corner_msg.pose.orientation.w = 0
            target_corner_msg.pose.position.x = -1
            target_corner_msg.pose.position.z = -1

        yolo_target_pub.publish(target_corner_msg)
        rate.sleep()


if __name__ == "__main__":
    clint()
