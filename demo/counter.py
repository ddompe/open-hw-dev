# (C) Copyright 2020 Hewlett Packard Enterprise Development LP.

import argparse
import os
from migen import *

# This is an example that an state machine using Python Migen 
######################################################################
#         _____________
#        |             |
#        |             |
#        |   DEFAULT   |
#        |_____________|  
# 
#              |
#         _____________
#        |             |
#        |   INIT      |  <---------------|                
#        | counter_b + |                  |
#        |_____________|                  |
#                                         |
#               |  (counter_b==5)?        |
#         _____________                   |
#        |             |                  |
#        |             |                  |
#        |   WAIT      |                  |
#        |_____________|                  |
#                                         |
#               | push?                   |
#         _____________                   |
#        |             |                  |
#        |   COUNT     |                  |
#        | counter_a + |                  |
#        |_____________|                  |
#                                         |
#               |  (counter_b==10)?       |
#         _____________                   |
#        |             |                  |
#        |             | _________________|
#        | COUNT_DONE  |
#        |_____________|
#
######################################################################
# To declare module use classes with keyword module inside
class State_Machine(Module):
    def __init__(self):
        
        #No reset,clock declaration are needed they are done by default
        #inputs and outputs are infered
        
        #Signal declarations
        #By default all signals values are zero 
        self.s    = Signal()
        self.init = Signal()
        self.counting = Signal()
        #Give the reset value at signal declaration
        self.green = Signal(reset=1)
        self.red   = Signal()
        self.push  = Signal()
        self.counter_a = Signal(8)
        self.counter_b = Signal(8)
        
        #Create 7 diferents Signals: a0, a1,.... a6
        x = Array(Signal(name="a") for i in range(7))

        #Use the function to create a FSM() state machine
        myfsm = FSM()
        self.submodules += myfsm

        # Describe each of the FSM states
        myfsm.act("DEFAULT",
            self.s.eq(1),
            self.red.eq(0),
            NextState("INIT")
        )
        myfsm.act("INIT",
            self.s.eq(1),
            self.init.eq(1),
            If(self.counter_b== 5,
                NextState("WAIT"),
            ).Else(
                NextValue(self.counter_b, self.counter_b + 1),
                NextState("INIT"),
            )
        )
        myfsm.act("WAIT",
            If(self.push,
                NextState("COUNT"),
            ).Else(
                NextState("WAIT"),
            )
        )
    
        myfsm.act("COUNT",
            self.init.eq(0),
            self.red.eq(1),
            self.green.eq(0),
            NextValue(x[self.counter_a], 1),
            If(self.counter_a == 10,
                NextState("COUNT_DONE"),
            ).Else(
                NextValue(self.counter_a, self.counter_a + 1),
                NextState("COUNT"),
            )
        )
        myfsm.act("COUNT_DONE",
            self.s.eq(0),
            NextValue(self.counter_a, 0),
            NextValue(self.counter_b, 0),
            NextState("INIT")
        )
        
        #This are fsm functions that allows us give values to signals
        #depending which state is the State_Machine
        #as example yellow will high just the cycle before entering to COUNT state
        self.yellow = myfsm.before_entering("COUNT")
        self.be = myfsm.before_entering("FOO")
        self.ae = myfsm.after_entering("FOO")
        self.bl = myfsm.before_leaving("FOO")
        self.al = myfsm.after_leaving("FOO")
######################################################################
#    
#    LASCAS Febreary  2020 
#
######################################################################
