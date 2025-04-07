---
title: "Sine Lookup"
author: Cooper Shapard
date: 2024-11-07
category: Jekyll
layout: post
---


Here is the sine lookup table from Example 12.1 of the book, modified to work with your Red Pitaya:
```asm
@ Registers used:
@ R0 = return value in Q31 notation
@ R1 = sin argument (in degrees, from 0 to 360)
@ R2 = temp
@ R4 = starting address of sine table
@ R7 = copy of argument

.global _start
_start:
    MOV R1, =#theNumberYouWantToLookup(I would recommend 30, which should spit out 0x40000000)

    MOV R7, R1          @ Make a copy of the argument
    LDR R2, =#270       @ Constant won’t fit into rotation scheme
    LDR R4, =sin_data   @ Load address of sin table

    CMP R1, #90         @ Determine quadrant
    BLE retvalue        @ First quadrant? If so, just lookup

    CMP R1, #180
    RSBLE R1, R1, #180  @ Second quadrant? If so, lookup 180 - yourArgument
    BLE retvalue

    CMP R1, R2
    SUBLE R1, R1, #180  @ Third quadrant? If so, lookup yourArgument - 180
    BLE retvalue

    RSB R1, R1, #360    @ Otherwise, it is fourth. Lookup 360 - yourArgument

retvalue:               @ Get sin value from table
    LDR R0, [R4, R1, LSL #2]    @ LSL #2 because each data is 4 bytes
    CMP R7, #180
    RSBGT R0, R0, #0    @ Negate the value if yourArgument > 180

done:
    MOV R0, #0          @ End the program
    MOV R7, #1
    SVC 0

.data
sin_data: .word 0x00000000,0x023BE164,0x04779630,0x06B2F1D8,
                0x08EDC7B0,0x0B27EB50,0x0D613050,0x0F996A30,
                0x11D06CA0,0x14060B80,0x163A1A80,0x186C6DE0,
                0x1A9CD9C0,0x1CCB3220,0x1EF74C00,0x2120FB80,
                0x234815C0,0x256C6F80,0x278DDE80,0x29AC3780,
                0x2BC750C0,0x2DDF0040,0x2FF31BC0,0x32037A40,
                0x340FF240,0x36185B00,0x381C8BC0,0x3A1C5C80,
                0x3C17A500,0x3E0E3DC0,0x40000000,0x41ECC480,
                0x43D46500,0x45B6BB80,0x4793A200,0x496AF400,
                0x4B3C8C00,0x4D084600,0x4ECDFF00,0x508D9200,
                0x5246DD00,0x53F9BE00,0x55A61280,0x574BB900,
                0x58EA9100,0x5A827980,0x5C135380,0x5D9CFF80,
                0x5F1F5F00,0x609A5280,0x620DBE80,0x63798500,
                0x64DD8900,0x6639B080,0x678DDE80,0x68D9F980,
                0x6A1DE700,0x6B598F00,0x6C8CD700,0x6DB7A880,
                0x6ED9EC00,0x6FF38A00,0x71046D00,0x720C8080,
                0x730BAF00,0x7401E500,0x74EF0F00,0x75D31A80,
                0x76ADF600,0x777F9000,0x7847D900,0x7906C080,
                0x79BC3880,0x7A683200,0x7B0A9F80,0x7BA37500,
                0x7C32A680,0x7CB82880,0x7D33F100,0x7DA5F580,
                0x7E0E2E00,0x7E6C9280,0x7EC11A80,0x7F0BC080,
                0x7F4C7E80,0x7F834F00,0x7FB02E00,0x7FD31780,
                0x7FEC0A00,0x7FFB0280,0x7FFFFFFF

```

Here is your new lookup table with values of 0-180 (if this doesn't work, you may need a `.word` tag in front of each line):
```asm
sin_data: .word      0x00000000,0x023BE164,0x04779630,0x06B2F1D8
          .word      0x08EDC7B0,0x0B27EB50,0x0D613050,0x0F996A30
          .word      0x11D06CA0,0x14060B80,0x163A1A80,0x186C6DE0
          .word      0x1A9CD9C0,0x1CCB3220,0x1EF74C00,0x2120FB80
          .word      0x234815C0,0x256C6F80,0x278DDE80,0x29AC3780
          .word      0x2BC750C0,0x2DDF0040,0x2FF31BC0,0x32037A40
          .word      0x340FF240,0x36185B00,0x381C8BC0,0x3A1C5C80
          .word      0x3C17A500,0x3E0E3DC0,0x40000000,0x41ECC480
          .word      0x43D46500,0x45B6BB80,0x4793A200,0x496AF400
          .word      0x4B3C8C00,0x4D084600,0x4ECDFF00,0x508D9200
          .word      0x5246DD00,0x53F9BE00,0x55A61280,0x574BB900
          .word      0x58EA9100,0x5A827980,0x5C135380,0x5D9CFF80
          .word      0x5F1F5F00,0x609A5280,0x620DBE80,0x63798500
          .word      0x64DD8900,0x6639B080,0x678DDE80,0x68D9F980
          .word      0x6A1DE700,0x6B598F00,0x6C8CD700,0x6DB7A880
          .word      0x6ED9EC00,0x6FF38A00,0x71046D00,0x720C8080
          .word      0x730BAF00,0x7401E500,0x74EF0F00,0x75D31A80
          .word      0x76ADF600,0x777F9000,0x7847D900,0x7906C080
          .word      0x79BC3880,0x7A683200,0x7B0A9F80,0x7BA37500
          .word      0x7C32A680,0x7CB82880,0x7D33F100,0x7DA5F580
          .word      0x7E0E2E00,0x7E6C9280,0x7EC11A80,0x7F0BC080
          .word      0x7F4C7E80,0x7F834F00,0x7FB02E00,0x7FD31780
          .word      0x7FEC0A00,0x7FFB0280,0x7FFFFFFF,0x7FFB0280    @ 90 degrees is this line's 0xFFFFFFFF
          .word      0x7FEC0A00,0x7FD31780,0x7FB02E00,0x7F834F00
          .word      0x7F4C7E80,0x7F0BC080,0x7EC11A80,0x7E6C9280
          .word      0x7E0E2E00,0x7DA5F580,0x7D33F100,0x7CB82880
          .word      0x7C32A680,0x7BA37500,0x7B0A9F80,0x7A683200
          .word      0x79BC3880,0x7906C080,0x7847D900,0x777F9000
          .word      0x76ADF600,0x75D31A80,0x74EF0F00,0x7401E500
          .word      0x730BAF00,0x720C8080,0x71046D00,0x6FF38A00
          .word      0x6ED9EC00,0x6DB7A880,0x6C8CD700,0x6B598F00
          .word      0x6A1DE700,0x68D9F980,0x678DDE80,0x6639B080
          .word      0x64DD8900,0x63798500,0x620DBE80,0x609A5280
          .word      0x5F1F5F00,0x5D9CFF80,0x5C135380,0x5A827980
          .word      0x58EA9100,0x574BB900,0x55A61280,0x53F9BE00
          .word      0x5246DD00,0x508D9200,0x4ECDFF00,0x4D084600
          .word      0x4B3C8C00,0x496AF400,0x4793A200,0x45B6BB80
          .word      0x43D46500,0x41ECC480,0x40000000,0x3E0E3DC0
          .word      0x3C17A500,0x3A1C5C80,0x381C8BC0,0x36185B00
          .word      0x340FF240,0x32037A40,0x2FF31BC0,0x2DDF0040
          .word      0x2BC750C0,0x29AC3780,0x278DDE80,0x256C6F80
          .word      0x234815C0,0x2120FB80,0x1EF74C00,0x1CCB3220
          .word      0x1A9CD9C0,0x186C6DE0,0x163A1A80,0x14060B80
          .word      0x11D06CA0,0x0F996A30,0x0D613050,0x0B27EB50
          .word      0x08EDC7B0,0x06B2F1D8,0x04779630,0x023BE164
          .word      0x00000000
```