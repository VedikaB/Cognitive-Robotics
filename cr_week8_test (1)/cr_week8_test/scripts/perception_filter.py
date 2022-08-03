#!/usr/bin/env python

import rospy
import random
from cr_week8_test.msg import object_info,human_info,perceived_info
objectid=0
object_size=0
human_expression=0
human_action=0
def callback1(data):
    global size_object
    size_object=data.object_size
def callback2(data):
    global objectid
    objectid=data.id
    global human_expression
    human_expression=data.human_expression
    global human_action
    human_action=data.human_expression
def filterperception():
    rospy.init_node('filterperception')
    rospy.Subscriber("object_info",object_info, callback1)
    rospy.Subscriber("human_info",human_info, callback2)
   

if __name__ == '__main__':
    filterperception()
    pub=rospy.Publisher('perceived_info',perceived_info,queue_size=10)
    rate=rospy.Rate(0.1)
    filtered_data=perceived_info()
    while not rospy.is_shutdown():
        filtered_data.id=objectid
        filtered_data.human_action=human_action
        filtered_data.human_expression=human_expression
        filtered_data.object_size=object_size
        selection=int(random.uniform(1,8))
        if selection==1:
            filtered_data.object_size=0
        elif selection==2:
            filtered_data.human_action=0
        elif selection==3:
            filtered_data.human_expression=0
        elif selection==4:
            filtered_data.object_size=0
            filtered_data.human_action=0
        elif selection==5:
            filtered_data.object_size=0
            filtered_data.human_expression=0
        elif selection==6:
            filtered_data.human_expression=0
            filtered_data.human_action=0
        elif selection==7:
            filtered_data.object_size=0
            filtered_data.human_action=0
            filtered_data.human_expression=0
        pub.publish(filtered_data)
        rate.sleep()

