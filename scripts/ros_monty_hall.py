#!/usr/bin/env python

# monty hall example
# https://github.com/eBay/bayesian-belief-networks/blob/master/docs/tutorial/tutorial.rst
# rosservice call /monty_hall/query []
# rosservice call /monty_hall/query [[guest_door,A]]
# rosservice call /monty_hall/query [[guest_door,A],[monty_door,B]]

import imp; imp.find_module('bayesian_belief_networks')
from bayesian_belief_networks.ros_utils import *

import rospy


def f_prize_door(prize_door):
    return 1.0 / 3

def f_guest_door(guest_door):
    return 1.0 / 3


def f_monty_door(prize_door, guest_door, monty_door):
    if prize_door == guest_door:
        if prize_door == monty_door:
            return 0
        else:
            return 0.5
    elif prize_door == monty_door:
        return 0
    elif guest_door == monty_door:
        return 0
    return 1

rospy.init_node('monty_hall')
g = ros_build_bbn(
    f_prize_door,
    f_guest_door,
    f_monty_door,
    domains=dict(
        prize_door=['A', 'B', 'C'],
        guest_door=['A', 'B', 'C'],
        monty_door=['A', 'B', 'C']))

rospy.spin()


