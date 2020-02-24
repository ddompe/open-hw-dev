# (C) Copyright 2020 Hewlett Packard Enterprise Development LP.

import argparse
import os
from migen import *


# Simple state machine 
class State_Machine(Module):
    def __init__(self):
        self.s    = Signal()
        self.init = Signal()
        self.counting = Signal()
        self.green = Signal(reset=1)
        self.red   = Signal()
        self.push  = Signal()
        self.counter_a = Signal(8)
        self.counter_b = Signal(8)
        
        #Create 7 diferent Signals
        x = Array(Signal(name="a") for i in range(7))

        myfsm = FSM()
        self.submodules += myfsm

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
        

        self.yellow = myfsm.before_entering("COUNT")
        self.be = myfsm.before_entering("FOO")
        self.ae = myfsm.after_entering("FOO")
        self.bl = myfsm.before_leaving("FOO")
        self.al = myfsm.after_leaving("FOO")
