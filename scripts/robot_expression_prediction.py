#!/usr/bin/env python

# monty hall example
# https://github.com/eBay/bayesian-belief-networks/blob/master/docs/tutorial/tutorial.rst
# rosservice call /monty_hall/query []
# rosservice call /monty_hall/query [[guest_door,A]]
# rosservice call /monty_hall/query [[guest_door,A],[monty_door,B]]

import imp; imp.find_module('bayesian_belief_networks')
from bayesian_belief_networks.ros_utils import *

import rospy


def f_object_size(object_size):
    return 1.0 / 2

def f_human_expression(human_expression):
    return 1.0 / 3

def f_human_action(human_action):
    return 1.0 / 3


def f_robot_expression(object_size,human_expression,human_action,robot_expression):
    if object_size=='1' and human_expression=='1' and human_action=='1' and robot_expression=='1':
        return 0.8
    if object_size=='2' and human_expression=='1' and human_action=='1' and robot_expression=='1':
        return 1.0
    if object_size=='1' and human_expression=='1' and human_action=='2' and robot_expression=='1' :
        return 0.8
    if object_size=='2' and human_expression=='1' and human_action=='2' and robot_expression=='1':
        return 1.0
    if object_size=='1' and human_expression=='1' and human_action=='3' and robot_expression=='1' :
        return 0.6
    if object_size=='2' and human_expression=='1' and human_action=='3' and robot_expression=='1':
        return 0.8
    if object_size=='1' and human_expression=='2' and human_action=='1' and robot_expression=='1':
        return 0.0
    if object_size=='2' and human_expression=='2' and human_action=='1' and robot_expression=='1':
        return 0.0
    if object_size=='1' and human_expression=='2' and human_action=='2' and robot_expression=='1':
        return 0.0
    if object_size=='2' and human_expression=='2' and human_action=='2' and robot_expression=='1':
        return 0.1
    if object_size=='1' and human_expression=='2' and human_action=='3' and robot_expression=='1':
        return 0.0
    if object_size=='2' and human_expression=='2' and human_action=='3' and robot_expression=='1':
        return 0.2
    if object_size=='1' and human_expression=='3' and human_action=='1' and robot_expression=='1':
        return 0.7
    if object_size=='2' and human_expression=='3' and human_action=='1' and robot_expression=='1':
        return 0.8
    if object_size=='1' and human_expression=='3' and human_action=='2' and robot_expression=='1':
        return 0.8
    if object_size=='2' and human_expression=='3' and human_action=='2' and robot_expression=='1':
        return 0.9
    if object_size=='1' and human_expression=='3' and human_action=='3' and robot_expression=='1':
        return 0.6
    if object_size=='2' and human_expression=='3' and human_action=='3' and robot_expression=='1':
        return 0.7

    if object_size=='1' and human_expression=='1' and human_action=='1' and robot_expression=='2':
        return 0.2
    if object_size=='2' and human_expression=='1' and human_action=='1' and robot_expression=='2':
        return 0.0
    if object_size=='1' and human_expression=='1' and human_action=='2' and robot_expression=='2' :
        return 0.2
    if object_size=='2' and human_expression=='1' and human_action=='2' and robot_expression=='2':
        return 0.0
    if object_size=='1' and human_expression=='1' and human_action=='3' and robot_expression=='2' :
        return 0.2
    if object_size=='2' and human_expression=='1' and human_action=='3' and robot_expression=='2':
        return 0.2
    if object_size=='1' and human_expression=='2' and human_action=='1' and robot_expression=='2':
        return 0.0
    if object_size=='2' and human_expression=='2' and human_action=='1' and robot_expression=='2':
        return 0.0
    if object_size=='1' and human_expression=='2' and human_action=='2' and robot_expression=='2':
        return 0.1
    if object_size=='2' and human_expression=='2' and human_action=='2' and robot_expression=='2':
        return 0.1
    if object_size=='1' and human_expression=='2' and human_action=='3' and robot_expression=='2':
        return 0.2
    if object_size=='2' and human_expression=='2' and human_action=='3' and robot_expression=='2':
        return 0.2
    if object_size=='1' and human_expression=='3' and human_action=='1' and robot_expression=='2':
        return 0.3
    if object_size=='2' and human_expression=='3' and human_action=='1' and robot_expression=='2':
        return 0.2
    if object_size=='1' and human_expression=='3' and human_action=='2' and robot_expression=='2':
        return 0.2
    if object_size=='2' and human_expression=='3' and human_action=='2' and robot_expression=='2':
        return 0.1
    if object_size=='1' and human_expression=='3' and human_action=='3' and robot_expression=='2':
        return 0.2
    if object_size=='2' and human_expression=='3' and human_action=='3' and robot_expression=='2':
        return 0.2

    if object_size=='1' and human_expression=='1' and human_action=='1' and robot_expression=='3':
        return 0.0
    if object_size=='2' and human_expression=='1' and human_action=='1' and robot_expression=='3':
        return 0.0
    if object_size=='1' and human_expression=='1' and human_action=='2' and robot_expression=='3' :
        return 0.0
    if object_size=='2' and human_expression=='1' and human_action=='2' and robot_expression=='3':
        return 0.0
    if object_size=='1' and human_expression=='1' and human_action=='3' and robot_expression=='3' :
        return 0.2
    if object_size=='2' and human_expression=='1' and human_action=='3' and robot_expression=='3':
        return 0.0
    if object_size=='1' and human_expression=='2' and human_action=='1' and robot_expression=='3':
        return 1.0
    if object_size=='2' and human_expression=='2' and human_action=='1' and robot_expression=='3':
        return 1.0
    if object_size=='1' and human_expression=='2' and human_action=='2' and robot_expression=='3':
        return 0.9
    if object_size=='2' and human_expression=='2' and human_action=='2' and robot_expression=='3':
        return 0.8
    if object_size=='1' and human_expression=='2' and human_action=='3' and robot_expression=='3':
        return 0.8
    if object_size=='2' and human_expression=='2' and human_action=='3' and robot_expression=='3':
        return 0.6
    if object_size=='1' and human_expression=='3' and human_action=='1' and robot_expression=='3':
        return 0.0
    if object_size=='2' and human_expression=='3' and human_action=='1' and robot_expression=='3':
        return 0.0
    if object_size=='1' and human_expression=='3' and human_action=='2' and robot_expression=='3':
        return 0.0
    if object_size=='2' and human_expression=='3' and human_action=='2' and robot_expression=='3':
        return 0.0
    if object_size=='1' and human_expression=='3' and human_action=='3' and robot_expression=='3':
        return 0.2
    if object_size=='2' and human_expression=='3' and human_action=='3' and robot_expression=='3':
        return 0.1



    
if __name__ == '__main__':
 rospy.init_node('robot_expression_prediction')
 g = ros_build_bbn(
    f_object_size,
    f_human_expression,
    f_human_action,
    f_robot_expression,
    domains=dict(
        object_size=['1','2'],
        human_expression=['1','2','3'],
        human_action=['1','2','3'],
        robot_expression=['1','2','3']))

rospy.spin()


