// This is some unknown header file.
#include "obj_dir/Vcheck.h"

#include <iostream>
#include <memory>

int main(int argc, char *argv[]) {
    // Verilated gives hint of verilator which is a tool to convert Verilog to a cycle-accurate behavioral model in C++.
    // Verilog is a hardware description language used to model electronic circuits like a multiplier circuit or a whole ALU.
    Verilated::commandArgs(argc, argv);
    std::cout << "Enter password:" << std::endl;

    //Not sure about this.
    auto check = std::make_unique<Vcheck>();

    // So this loop runs at most 100 times meaning it is max password length.
    // check->open_safe is checked after every iteration meaning it is a signal for the right password.
    for (int i = 0; i < 100 && !check->open_safe; i++) {
        // A character is read
        int c = fgetc(stdin);
        if (c == '\n' || c < 0) break;

        // AND with 01111111 to zero down the MSB
        check->data = c & 0x7f;

        // This seems like an implementation of a positive edge clock signal(that is used in flip-flops,etc)
        // Every time signal goes from 0 to 1, state of the device changes.
        check->clk = false;
        check->eval();
        check->clk = true;
        check->eval();
    }
    
    if (check->open_safe) {
        std::cout << "CTF{real flag would be here}" << std::endl;
    } else {
        std::cout << "=(" << std::endl;
    }

    // So check is probably an implementation of a device that takes password as input and works with a clock signal.
    // Depending on the value of password it modifies the value of open_safe variable which we need to make true in order to get the flag.
    // Working of this device can be understood by analysing its verilog code(check.sv)
    return 0;
}

