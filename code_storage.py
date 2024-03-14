jkff_tb = '''
module tb_jkff;

 // Inputs
 reg clk, reset;
 reg [1:0]jk;

 // Output
 wire Q;

 // DUT instantiation
 jkff dut (.clk(clk), .reset(reset), .jk(jk), .Q(Q));

 // Clock generation
 always #5 clk = ~clk; // Toggle clock every 5 time units

 // Test case generation
 initial begin
  $dumpfile("jkff_simulation.vcd"); // Replace with desired filename
  $dumpvars(0, dut);         // Dump all signals of the DUT

  clk = 0;
  reset = 0;
  jk = 2'b00;
  #10 reset =1;
  #10 reset =0;
  #10 jk = 2'b01;
  #10 jk = 2'b10;
  #10 jk = 2'b11; 

  $finish;
 end

 // Monitor (optional, for debugging)
 initial begin
  $monitor("Time: %d, clk: %b, reset: %b, jk: %b, Q: %b", $time, clk, reset, jk, Q);
 end

endmodule
'''

jkff = '''
module jkff (
    input clk,
    input reset,
    input [1:0] jk,
    output reg Q
);

    // Synchronous reset (active low)
  always @(negedge clk)
        if (reset) // Active low reset
            Q <= 1'b0; // Reset Q to logic 1
  else if (!reset) // Active low reset
            Q <= 1'b1;
        else case (jk)
                2'b00: Q <= Q;    // Hold
                2'b01: Q <= 1'b0;  // Set
                2'b10: Q <= 1'b1;  // Reset
                2'b11: Q <= ~Q;    // Toggle
                default: Q <= 1'b0; // Unassigned JK combination (optional)
            endcase
endmodule
'''

dff = '''
module dff (
    input clk,
    input reset,
    input d,
    output reg q
);

    // Synchronous reset (active low)
    always @(posedge clk)
        if (!reset)
            q <= 1'b0; // Reset q to logic 0
        else
            q <= d; // Assign input d to q

endmodule
'''

dff_tb = '''
module tb_dff;

    // Inputs
    reg clk, reset, d;

    // Output
    wire q;

    // DUT instantiation
    dff dut (.clk(clk), .reset(reset), .d(d), .q(q));

    // Clock generation
    always #5 clk = ~clk; // Toggle clock every 5 time units

    // Test case generation
    initial begin
        $dumpfile("dff_simulation.vcd"); // Replace with desired filename
        $dumpvars(0, dut); // Dump all signals of the DUT
        clk = 0;
        reset = 0;
        d = 0;

        #10 reset = 1;
        #10 d = 1;
        #10 d = 0;
        #10 reset = 0;
        #10 d = 1;
        #10 d = 0;

        $finish;
    end

    // Monitor (optional, for debugging)
    initial begin
        $monitor("Time: %d, clk: %b, reset: %b, d: %b, q: %b", $time, clk, reset, d, q);
    end

endmodule
'''

mux8x1 = '''

module mux81(i, s, y);

  input [7:0] i;
  input [2:0] s;
  output reg y;

  always @ (s or i) begin
    case (s)
      3'b000: y = i[0];
      3'b001: y = i[1];
      3'b010: y = i[2];
      3'b011: y = i[3];
      3'b100: y = i[4];
      3'b101: y = i[5];
      3'b110: y = i[6];
      3'b111: y = i[7];
      default: y = 1'bz;
    endcase
  end

endmodule

'''

mux8x1_tb = '''
module tb_mux81;

// Inputs
reg [7:0] i;
reg [2:0] s;

// Output
wire y;

// DUT instantiation
mux81 dut (.i(i), .s(s), .y(y));

// Test case generation
initial begin
    $dumpfile("mux81_simulation.vcd"); // Replace with desired filename
    $dumpvars(0, dut); // Dump all signals of the DUT

    i = 8'b10101010;
  
    s = 3'b000;
    #10;
    s = 3'b001;
    #10;
    s = 3'b010;
    #10;
  s = 3'b011;
    #10;
  s = 3'b100;
    #10;
  s = 3'b101;
    #10;
  s = 3'b110;
    #10;
  s = 3'b111;
    #10;
  
    $finish;
end

// Monitor (optional, for debugging)
initial begin
    $monitor("Time: %d, i: %b, s: %b, y: %b", $time, i, s, y);
end

endmodule
'''

decoder24 = '''
module decoder24(i, y);

input [1:0] i;
output [3:0] y;
reg [3:0] y;

always @(i)
begin
    case (i)
        2'b00: y = 4'b0001;
        2'b01: y = 4'b0010;
        2'b10: y = 4'b0100;
        2'b11: y = 4'b1000;
        default: y = 4'b0000;
    endcase
end

endmodule

'''
decoder24_tb = '''
module tb_decoder24;

// Inputs
reg [1:0] i;

// Output
wire [3:0] y;

// DUT instantiation
decoder24 dut (.i(i), .y(y));

// Test case generation
initial begin
    $dumpfile("decoder24_simulation.vcd"); // Replace with desired filename
    $dumpvars(0, dut); // Dump all signals of the DUT

    // Test case 1
    i = 2'b00;
    #10;

    // Test case 2
    i = 2'b01;
    #10;

    // Test case 3
    i = 2'b10;
    #10;

    // Test case 4
    i = 2'b11;
    #10;

    $finish;
end

// Monitor (optional, for debugging)
initial begin
    $monitor("Time: %d, i: %b, y: %b", $time, i, y);
end

endmodule
'''

encoder83 = '''

module enc83(En, d, b);

  input En;
  input [7:0] d;
  output [2:0] b;
  reg [2:0] b;

  always @ (d, En) begin
    if (En)
      b = 3'b000;
    else begin
      case (d)
        8'b00000001: b = 3'b000;
        8'b00000010: b = 3'b001;
        8'b00000100: b = 3'b010;
        8'b00001000: b = 3'b011;
        8'b00010000: b = 3'b100;
        8'b00100000: b = 3'b101;
        8'b01000000: b = 3'b110;
        8'b01100000: b = 3'b111;
        default: b = 3'bZZZ;
      endcase
    end
  end

endmodule
'''
encoder83_tb = '''
module tb_enc83;

// Inputs
reg En;
reg [7:0] d;

// Output
wire [2:0] b;

// DUT instantiation
enc83 dut (.En(En), .d(d), .b(b));

// Test case generation
initial begin
    $dumpfile("enc83_simulation.vcd"); // Replace with desired filename
    $dumpvars(0, dut); // Dump all signals of the DUT

    // Test case 1 (En = 1)
    En = 1'b1;
    d = 8'b00000000;
    #10;

    // Test case 2 (En = 0, d = 8'b00000001)
    En = 1'b0;
    d = 8'b00000001;
    #10;

    // Test case 3 (En = 0, d = 8'b00000010)
    d = 8'b00000010;
    #10;

    // Test case 4 (En = 0, d = 8'b00000100)
    d = 8'b00000100;
    #10;
  d = 8'b00001000;
    #10;
  d = 8'b00010000;
    #10;
  d = 8'b00100000;
    #10;
  d = 8'b01000000;
    #10;
  d = 8'b10000000;
    #10;

    $finish;
end

// Monitor (optional, for debugging)
initial begin
    $monitor("Time: %d, En: %b, d: %b, b: %b", $time, En, d, b);
end

endmodule
'''

priority_enc = '''
module penc83(en, d, b);

  input en;
  input [7:0] d;
  output [2:0] b;
  reg [2:0] b;

  always @ (d, en)
  begin
    if (en)
      b = 3'd0;
    else if (d[7])
      b = 3'd7;
    else if (d[6])
      b = 3'd6;
    else if (d[5])
      b = 3'd5;
    else if (d[4])
      b = 3'd4;
    else if (d[3])
      b = 3'd3;
    else if (d[2])
      b = 3'd2;
    else if (d[1])
      b = 3'd1;
    else
      b = 3'd0;
  end

endmodule

'''

priority_enc_tb = '''
module tb_penc83;

// Inputs
reg en;
reg [7:0] d;

// Output
wire [2:0] b;

// DUT instantiation
penc83 dut (.en(en), .d(d), .b(b));

// Test case generation
initial begin
    $dumpfile("penc83_simulation.vcd"); // Replace with desired filename
    $dumpvars(0, dut); // Dump all signals of the DUT

    // Test case 1 (en = 1)
    en = 1'b1;
    d = 8'b00000000;
    #10;

    en = 1'b0;
    d = 8'b00000001;
    #10;

    d = 8'b00000010;
    #10;

    d = 8'b00000100;
    #10;

    d = 8'b00001000;
    #10;

    d = 8'b00010000;
    #10;

    d = 8'b00100000;
    #10;

    d = 8'b01000000;
    #10;

    d = 8'b10000000;
    #10;

    $finish;
end

// Monitor (optional, for debugging)
initial begin
    $monitor("Time: %d, en: %b, d: %b, b: %b", $time, en, d, b);
end

endmodule
'''