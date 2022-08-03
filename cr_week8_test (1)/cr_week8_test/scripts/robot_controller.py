#!/usr/bin/env python

import rospy
import random
from cr_week8_test.msg import object_info,human_info,perceived_info,robot_info
from cr_week8_test.srv import predict_robot_expression,predict_robot_expressionRequest
from bayesian_belief_networks.msg import Observation
from bayesian_belief_networks.srv import Query

size_object=None
def callback(data):
    #rospy.loginfo(data.p0, data.pf,data.v0,data.vf,data.t0,data.tf)
    rospy.wait_for_service('{}'.format('robot_expression_prediction/query'))
    try:
        query=rospy.ServiceProxy('robot_expression_prediction/query',Query)
        msg=[]
        o = Observation()
        if data.object_size!=0:
            o = Observation('object_size',str(data.object_size))
            msg.append(o)
    
        if data.human_expression!=0:
            o = Observation('human_expression',str(data.human_expression))
            msg.append(o)
 
        if data.human_action!=0:
            o = Observation('human_action',str(data.human_action))
            msg.append(o)
        
        response=query(msg)
        print(response.results)
        result=[None,None,None]
        temp_result = [x for x in response.results if x.node=='robot_expression']
        for res in temp_result:
            result[int(res.Value)-1]=res.Marginal     
        pub2=rospy.Publisher('topic4',robot_info,queue_size=10)
        pub2.publish(data.id,result[0],result[1],result[2])
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
   
   
    
        
def listener():

    rospy.init_node('robot_controller', anonymous=True)
    rospy.Subscriber("perceived_info",perceived_info, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

