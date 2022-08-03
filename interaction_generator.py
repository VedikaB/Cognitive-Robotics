#!/usr/bin/env python

import rospy
import random
from cr_week8_test.msg import object_info
from cr_week8_test.msg import human_info

def talker():
    count=0
    pub = rospy.Publisher('object_info',object_info,queue_size=10)
    pub2 = rospy.Publisher('human_info',human_info,queue_size=10)
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.05)
    #rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg1=object_info()
        msg2=human_info()
        msg1.id=count+1 
        msg2.id=msg1.id
        msg1.object_size=int(random.uniform(1,2))
        msg2.human_action=int(random.uniform(1,3))
        msg2.human_expression=int(random.uniform(1,3))
        pub.publish(msg1)
        pub2.publish(msg2)
        rate.sleep()

if __name__ == '__main__':
    print('inside point')
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
