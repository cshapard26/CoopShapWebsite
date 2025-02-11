---
title: "Lab 3: Moving and Adding"
author: Cooper Shapard
date: 2024-09-08
category: Jekyll
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab3/Lab3_MovingAdding.pdf)

# Overview
Welcome to Lab 3! Now that you are familiar with the syntax of ARM and the debugger, we can start analyzing how the ARM processor manipulates data. There are two main takeaways from this lab. First, the ARM processor does not interpret values; only the programmer does. Whether you are doing signed addition, unsigned addition, or something else, the ARM processor behaves the exact same way, using Two's Complement. Thus, the result of an operation may be a signed or unsinged number, but the processor doesn't know which it is. It is up to the programmer to interpret the output using the CPSR condition codes (NZCV), which put to use in this lab. Second, this lab focuses on placing values in registers **without** accessing memory. Though the word "load" is used in the text, this is a misnomer, as "load" is exclusive to accessing memory in ARM. You will learn more about memory management in a future lab, but understand that for now we are only looking at immediate values.

As always, this guide is a supplement for the official lab instructions, not a replacement. When in doubt, refer back to the official instructions. If you need any help or clarification, be sure to ask a TA. The old lab guides are avaliable in case you want to freshen up on the skills you have already learned.

# Explanations
## Step 1 & 2
Read pages 27-41 in the Smith textbook. Please actually do this. Many of the topics will be familiar from lecture, but it is cruicial to get another perspective before continuing with the lab. 

## Step 3
Following the book, create a file using the code from Listing 2-1 (also found in the [Code Given](#code-given) section). Be sure to update your "makefile" file with the new name of your file. There should be 3 updates. This is the same makefile you used in the previous lab. Build the file with the command `make DEBUG=1`. Next, use the command `objdump -s -d NameOfYourFile.o` to object dump the file. Please please please replace the word "NameOfYourFile" with the actual name of your file (likely "movexamps"). This is the #1 issue people have. **Take a screenshot of the objdump output and include it in your lab report.**

## Step 4
Take your code from step 3 and change all of the `MOV` instructions to `MOVS`. Ignore the `MOVT` line. Adding the S makes the program update the CPSR (Current Program Status Register) flags, which you should remember from lecture. These are the NZCV bits. For this step, we only care about the C (carry) bit and can examine it with the debugger. 
1. Add breakpoints in front of the first 7 `MOVS` lines. This is similar to what you did last lab. I recommend you name the breakpoints `mv1:`, `mv2:`, etc. 
2. Enter the program using the debugger (gdb). Set breakpoints for each line and step over each breakpoint. After you step over a MOVS line, display the registers. There is a register named CSPR, which is where the CPSR flags are stored. **For each of these MOVS lines, include a screenshot of the registers/CPSR.** You should have 7 screenshots for this step.
3. Now, you want to check the C bit of your CPSR. This can get confusing, so read carefully and ask a TA if you have questions. You learned from lecture that there are 4 CPSR flags we want to pay attention to: NZCV. These 4 bits are the *leftmost* bits of the CPSR. However, in your program, the CPSR will be displayed in hexadecimal. You will need to extract the binary flags from the hexadecimal notation. Since 4 bits turn into 1 character in hex, we can do this easily by <u>converting just the very first character of the CPSR register from hex to binary</u>. So if the register contains "0x90000010", then we would just take the 9, convert it into binary—1001—and assign each bit to its flag NZCV in that order. So in this example, the N and V flags are on/1 and the Z and C flags are off/0. Another example: "0xB681EF21". We take the leftmost character "B", convert it to binary "1011", and assign the flags "N_CV". <u>You may occationally see a shortened CPSR like "0x10" that does not have all 8 characters. This means that all the flags are off/0.</u> **Under each of the 7 screenshots, explain why each MOVS command gave the resulting C value.**

## Step 5
Read pages 45-49 in the Smith book. These concepts should be familiar from lecture and HW1.

## Step 6
Create a new file called "mvnaddexamp.s" and fill it with the code from Listing 2-3 (also in the [Code Given](#code-given) section). Update your "makefile" with the new filename; there should be three updates. Build the file with the debugger enabled. Now, use the debugging procedure (gdb) to examine your file. Step, `s`, to the very last line (SVC 0), but don't go further. Then, print the registers with `i r`. What value is in register R0? **Include a screenshot of the registers from this step in your lab report.**

## Step 7
Create a new file called "addsadcexamp.s" and fill it with the code from Listing 2-4 (also in the [Code Given](#code-given) section). Update your "makefile" with the new filename; there should be three updates. Build the file with the debugger enabled.

## Step 8
We are now going to do something similar to step 4, but now we care about all 4 CPSR flags, NZCV. Using your code from step 7, change the line `MOV R3, 0xFFFFFFFF` to `LDR R3, =0xYourSMUID`, so if your ID was 12345678, you would have `LDR R3, =0x12345678`. You will also want to change R5 to be an `LDR` command. This number will be added to the number in R5. Your goal is to change the number in R5 to achieve *each/all* condition code value, NZCV. You will want a situation where N = 0, one where N = 1, one where C = 0, one where C = 1, etc. Since you can have multiple condition codes, you do not necessarily need 8 screenshots/8 R5 values. Ideally, you could do this is 2 numbers in R5, but use as many as you need to complete this step.

To do this, I would recommend placing a breakpoint at the `ADC` line. Each time you change R5, `make DEBUG=1` the program, open the debugger, run to your breakpoint, then print the registers to check the CPSR value. 

If this step is confusing, check the official lab section and ask a TA if you still need help.

**For each CPSR value you generate, take a screenshot of the registers and include it in your lab report. We should be able to see both the value of R5 and the CPSR in the screenshot.**



# Conclusion
In this lab, you examined how the ARM processor manipulates data through moving and adding. You gained experience with the CPSR and navigating the debugger. You should be starting to feel more comforable with the syntax of ARM and how to apply the lecture topics directly to your code. If you have any questions, be sure to ask a TA. We also have office hours if you have more questions. Be sure to turn in your lab report before next lab, and have a great weekend.

# Code Given
Listing 2-1:
```asm
@
@ Examples of the MOV instruction.
@
.global _start          @ Provide program starting address
                        @ Load R2 with 0x4F5D6E3A first using MOV and MOVT
_start: 
    LDR R2, =0x4F5D6E3A
                        @ Just move R2 into R1
    MOV R1, R2
                        @ Now let’s see all the shift versions of MOV
    MOV R1, R2, LSL #1  @ Logical shift left
    MOV R1, R2, LSR #1  @ Logical shift right
    MOV R1, R2, ASR #1  @ Arithmetic shift right
    MOV R1, R2, ROR #1  @ Rotate right
    MOV R1, R2, RRX     @ Rotate extended right
                        @ Repeat the above shifts using
                        @ the Assembler mnemonics.
    LSL R1, R2, #1      @ Logical shift left
    LSR R1, R2, #1      @ Logical shift right
    ASR R1, R2, #1      @ Arithmetic shift right
    ROR R1, R2, #1      @ Rotate right
    RRX R1, R2          @ Rotate extended right
                        @ Example that works with 8 bit immediate and shift
    MOV R1, #0xAB000000 @ Too big for #imm16
                        @ Example that can't be represented and
                        @ results in an error
                        @ Uncomment the instruction if you want to
                        @ see the error
    @MOV R1, #0xABCDEF11 @ Too big for #imm16
                        @ Example of MVN
    MVN R1, #45
                        @ Example of a MOV that the Assembler will
                        @ change to MVN
    MOV R1, #0xFFFFFFFE @ (-2)
                        @ Set up the parameters to exit the program
                        @ and then call Linux to do it.
    MOV R0, #0          @ Use 0 return code
    MOV R7, #1          @ Service command code 1
    SVC 0               @ Call Linux to terminate
```
Listing 2-3:
```asm
@
@ Example of the ADD/ADC instructions.
@
.global _start  @ Provide program starting address
                @ Multiply 2 by –1 by using MVN and then adding 1
_start: 
    MVN R0, #2
    ADD R0, #1
                @ Set up the parameters to exit the program
                @ and then call Linux to do it.
                @ R0 is the return code and will be what we
                @ calculated above.
    MOV R7, #1  @ Service command code 1
    SVC 0       @ Call Linux to terminate
```
Listing 2-4:
```asm
@
@ Example of 64-bit addition with
@ the ADD/ADC instructions.
@
.global _start          @ Provide program starting address
                        @ Load the registers with some data
                        @ First 64-bit number is 0x00000003FFFFFFFF
_start: 
    MOV R2, #0x00000003
    MOV R3, #0xFFFFFFFF @ as will change to MVN
                        @ Second 64-bit number is 0x0000000500000001
    MOV R4, #0x00000005
    MOV R5, #0x00000001
    ADDS R1, R3, R5     @ Lower order word
    ADC R0, R2, R4      @ Higher order word
                        @ Set up the parameters to exit the program
                        @ and then call Linux to do it.
                        @ R0 is the return code and will be what we
                        @ calculated above.
    MOV R7, #1          @ Service command code 1
    SVC 0               @ Call Linux to terminate
```