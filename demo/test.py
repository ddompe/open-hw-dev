# (C) Copyright 2020 Hewlett Packard Enterprise Development LP.

import argparse
import os
from counter import *

from migen import *
from migen.fhdl import verilog

######################################################################
#   Test function
# Instead of clock cycles Python uses yield to create concurrency 
# every yield can see that advance 1 clock cycle 
def sm_test(dut):
    for i in range(6):
        yield
    yield dut.push.eq(1)
    yield
    yield dut.push.eq(0)
    for i in range(20):
        yield  
        
######################################################################
# create verilog code
if __name__ == "__main__":
    dut = State_Machine()

    create_verilog = 1
    if(create_verilog):
        #dut.s, dut.counter_a ... are the inputs/outputs that I want to have in the verilog 
        verilog.convert(dut, {dut.s, dut.counter_a, dut.be, dut.ae, dut.bl, dut.al}).write("my_machine.v")
######################################################################
# Run the simulation
if __name__ == "__main__":
    dut = State_Machine()
    #gtkawave is create from Python code
    run_simulation(dut, sm_test(dut), vcd_name="state_machine.vcd")
    
######################################################################
#    
#    LASCAS Febreary  2020 
#
######################################################################
