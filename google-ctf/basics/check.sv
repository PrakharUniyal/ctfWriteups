// Verilog code is pretty easy. Every module is like a function that takes in both inputs and outputs and arguments.
module check(
    input clk,
    input [6:0] data,
    output wire open_safe
);

// reg and wire are just two kinds of variables that are used to hold data.

// memory is a 8 length array of 7 bit values.
reg [6:0] memory [7:0];
// idx is a 3 bit value initialized as 0(000)
reg [2:0] idx = 0;
// magic is a 56 bit value created by concatenating differently ordered memeory elements
wire [55:0] magic = {
    {memory[0], memory[5]},
    {memory[6], memory[2]},
    {memory[4], memory[3]},
    {memory[7], memory[1]}
};
// kittens is a reoredered variation of magic. The last 10 bits have come to front while first 14 have gone to the back.
wire [55:0] kittens = { magic[9:0],  magic[41:22], magic[21:10], magic[55:42] };

// kittens is compared with a 56 bit number.
assign open_safe = kittens == 56'd3008192072309708;

// this is a process which represents functioning of a flip-flop. It is triggered at positive edge clk signal
always_ff @(posedge clk) begin
    // 7 bits coming from a character in the password are stored in one of memory's element.
    memory[idx] <= data;
    // idx shifts by 5. So it goes like 0->5->2->7->4->1->6->3
    idx <= idx + 5;
end

// So we have to reverse this whole function and find the appropriate password that will make open_safe true.
endmodule

