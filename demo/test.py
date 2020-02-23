# (C) Copyright 2020 Hewlett Packard Enterprise Development LP.

import argparse
import os
from counter import *

from migen import *
from migen.fhdl import verilog



#def counter_test(dut):
#    for i in range(20):
#        print((yield dut.count))  # read and print
#        yield  # next clock cycle
#    # simulation ends with this generator

#if __name__ == "__main__":
#    dut = Counter()
    #run_simulation(dut, counter_test(dut), vcd_name="basic1.vcd")


def sm_test(dut):
    for i in range(20):
        #print((yield dut))  # read and print
        yield  # next clock cycle
    # simulation ends with this generator

# create verilog code
if __name__ == "__main__":
    dut = State_Machine()

    create_verilog = 1
    if(create_verilog):
        verilog.convert(dut, {dut.s, dut.counter, dut.be, dut.ae, dut.bl, dut.al}).write("my_machine.v")

# Run the simulation
if __name__ == "__main__":
    dut = State_Machine()
    run_simulation(dut, sm_test(dut), vcd_name="state_machine.vcd")
