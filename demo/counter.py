import argparse
import os
from migen import *


# Our simple counter, which increments at every cycle.
class Counter(Module):
    def __init__(self):
        self.count = Signal(4)

        # At each cycle, increase the value of the count signal.
        # We do it with convertible/synthesizable FHDL code.
        self.sync += self.count.eq(self.count + 1)


# Simply read the count signal and print it.
# The output is:
# Count: 0
# Count: 1
# Count: 2
# ...

class State_Machine(Module):
    def __init__(self):
        self.s = Signal()
        self.counter = Signal(8)
        x = Array(Signal(name="a") for i in range(7))

        myfsm = FSM()
        self.submodules += myfsm

        myfsm.act("FOO",
            self.s.eq(1),
            NextState("BAR")
        )
        myfsm.act("BAR",
            self.s.eq(0),
            NextValue(self.counter, self.counter + 1),
            NextValue(x[self.counter], 89),
            NextState("FOO")
        )

        self.be = myfsm.before_entering("FOO")
        self.ae = myfsm.after_entering("FOO")
        self.bl = myfsm.before_leaving("FOO")
        self.al = myfsm.after_leaving("FOO")