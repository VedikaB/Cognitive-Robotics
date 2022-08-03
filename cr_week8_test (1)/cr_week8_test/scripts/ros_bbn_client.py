#!/usr/bin/env python

'''
e.g. usage

rosrun PACKAGE ros_bbn_client.py "monty_hall/query" guest_door A
rosrun PACKAGE ros_bbn_client.py "monty_hall/query" guest_door A monty_door B ...

'''

import sys
import rospy

import imp; imp.find_module('bayesian_belief_networks')
from bayesian_belief_networks.ros_utils import *
from bayesian_belief_networks.msg import Observation, Result
from bayesian_belief_networks.srv import Query

def ros_bbn_client(bbn_name, obss):
    rospy.wait_for_service('{}'.format(bbn_name))
    try:
        query = rospy.ServiceProxy(bbn_name, Query)
        msg = []
        for obs in obss:
            o = Observation()
            o.node = obs[0]
            o.evidence = obs[1]
            msg.append(o)
        resp1 = query(msg)
        return resp1.results
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [bbn_name node evidence ...]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        bbn_name = sys.argv[1]
        obs = []
        for i in range(2, len(sys.argv), 2):
            obs.append(sys.argv[i:i+2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s: %s"% (bbn_name, obs)
    print "%s" % (ros_bbn_client(bbn_name, obs))