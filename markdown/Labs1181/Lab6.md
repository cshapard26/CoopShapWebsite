---
title: "Lab 6: Controlling Program Flow"
author: Cooper Shapard
date: 2024-10-03
category: Jekyll
draft: true
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab6/Lab6_ControllingProgramFlow.pdf)

# Overview
Welcome to Lab 6! Here, you will find only 4 simple steps. Simple does not mean easy.

In this lab, you will begin to see how a program can execute different parts based on **something called a *branch.*** Before, your program would execute each line in your program, one by one, in order. That was called PC+4 behavior because each command is four bytes long, so the program counter (PC) would go up by four bytes to execute the next line. Now, instead of the letting the program counter work on its own, **we can change the PC to whatever location we want.** That allows us to do some really fun things like repeating a section of code multiple times without having to rewrite it over and over or executing large blocks of code without the need for conditional execution (subgt, addlt, etc). 

While this new behavior is very useful, it is also very dangerous. You may move the program counter to a location it's not allowed to execute, or if it stops lining up with the four byte lines of code, that could cause problems that are very hard to identify. That second part is easy to find if you know what you're looking for. **The main thing to note is that the program counter must always be a multiple of four.** Luckily, we use hex numbers, so you can check if a number is divisible by four by checking if the hex number ends in 0, 4, 8, or c. If so, then your program counter is lined up correctly!

If you need any help, be sure to ask a TA!

# Explanations
## Step 1
Read through all of chapter 4 in the Smith textbook (please actually do this). Then, copy the code from the [code given](#code-given) section into a new file with a name of your choosing. Create a makefile, and update it with the new filename. Use `make DEBUG=1` to make the program with gdb enabled. Test the program using `./your_program_name` (without the .s). The program should work just like Lab 5, but it can take up to 50 characters of input. It will simply output the same characters you put in. Make sure that your program does this correctly.

## Step 2
This step is pretty much the whole lab.

Similarly to last lab, you need to design an algorithm that changes a lowercase letter to an uppercase letter (but not vice versa this time). However, instead of only uppercasing one letter, you need to be able to check up to fifty letters. *You are not allowed to do this by writing the same code 50 times.* You must use branching, which you read about in chapter four, to execute the same command for the length of the string. Your program should:
    - Loop through each character stored at the `msg` label in the .data section of your code.
    - Use a register to keep track of which character you are on (which I call a "tracker"). So if you have already checked/updated the first 14 characters, you should have a register that has the number 14 in it (or some other way to track where you are in the string, like updating the base register).
    - For each character:
        - Check if it is capitalized. If not, capitalize it, then store it back in the same position. If so, ignore it.
        - If it is not a letter, ignore it.
        - Update the location of your tracker.

**Notes**
1. If we are ignoring both uppercase letters and numbers, then what is the only ascii range we need to check?
2. How can we check if we have reached the end of the string? What is the ascii value of a '\n' (also called a Line Feed)?
3. You can either print out each character after checking if it is uppercase, or you can print them all out at the end. The choice is yours.
4. For your tracker, you can either update the register that holds the address of `msg` or have a register that tracks how many characters away from the start of `msg` you are. One uses pre-indexed addressing and one uses post/auto-indexed addressing. Depending on your solution, which should you use?
5. The program counter naturally increases by 4 bytes to get the next instruction. If one loop ends without branching to another part of the code, it will always start executing the next line, whether or not that is another loop. Always make sure that all branching cases are accounted for to prevent executing code you don't intend to (so if you have a BGT, you will probably want a BLE as well).

**Coding Practices**
1. It is possible to combine *branching* with *conditional execution.* For example:

```assembly
   MOV R1, #0

loopstart:
   ADD R1, R1, #1    @ Adds 1 to R1
   CMP R1, #5        @ Compares the number in R1 to the number 5
   BLT loopstart     @ If R1 is less than 5, branch back to the loop start.
                     @ Otherwise, continue downwards (to the Other Code).

   @ Other Code
```

2. You can have multiple branch heads. For example:

```assembly
loophead:
   CMP R1, #5
   BGT doThis     @ Goes to the doThis block of code if R1 > 5
   BLT doThat     @ Goes to the doThat block of code if R1 < 5
   BEQ end        @ Goes to end block of code if R1 == 5

doThis:           @ Write "hi coop" for 2 extra lab points
   SUB R1, R1, #1 @ Subtracts 1 from R1
   B loophead     @ Returns to loophead block of code

doThat:
   ADD R1, R1, #1 @ Adds 1 to R1
   B end          @ Branches to the 'end' block of code

end:
   @ Print output, etc.

```

## Step 3
**In your lab report, describe line-by-line how your algorithm works for the code you wrote.**

## Step 4
Screenshot at least 3 different tests that showcase your program working. Include various upper and lower case mixtures of your first name, last name, and student ID. **Include the screenshots in your lab report.**

# Code Given
```asm
@ Assembler program to input ASCII characters via stdin 
@ The program will take a string of up to 50 characters and modify it 
@ such that all lower-cased letters will be made upper-case. 
@ R0-R2 - parameters to linux function services 
@ R7 - linux function number 

.global _start          @ Provide program starting at address to linker 
                        @ Set up the parameters to retrieve characters and then call Linux to do it. 
_start:   
   MOV R0, #0           @ 0 = StdIn 
   LDR R1, =msg         @ Address to receive input 
   MOV R2, #50          @ Receive at most 50 characters 
   MOV R7, #3           @ Read 
   SVC 0                @ Call linux to receive input 

   MOV r2, r0           @ Captures number of characters input 

@ Insert your code here 

                        @ Set up stdout to echo those characters back and then call Linux to do it. 
   MOV R0, #1           @ 1 = StdOut 
   LDR R1, =msg         @ String to print 
   @MOV R2, #2           @ Commented out because you will need to calculate the string length 
   MOV R7, #4           @ Linux write system call 
   SVC 0                @ Call linux to print 

   MOV R0, #0           @ Use 0 return code 
   MOV R7, #1           @ Service command code 1 terminates this program 
   SVC 0                @ Call linux to terminate 

.data 
   msg:   .fill 51, 1, '\n'  @ Allocates enough memory for 50 characters 
```