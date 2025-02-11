---
title: "Lab 4: Thanks for the Memories"
author: Cooper Shapard
date: 2024-09-18
category: Jekyll
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab4/Lab4_ThanksForTheMemories.pdf)

# Overview
Welcome to Lab 4!

As always, this guide is a supplement for the official lab instructions, not a replacement. When in doubt, refer back to the official instructions. If you need any help or clarification, be sure to ask a TA. The old lab guides are avaliable in case you want to freshen up on the skills you have already learned.

# Explanations
## Step 1
Read through pages 87-91 in the Smith book (please actually do this). This is the beginning of Chapter 5 to the "Loading a Register" section for those without page numbers.

## Step 2
Observe Table 5-3 on page 93 and note how the B, SB, H, and SH letters affect the LDR instruction.

## Step 3
Read pages 95-96. "Wrap" the given code from Listing 5-2 (also in the [Code Given](#code-given) section) in the starting and ending code you have seen in previous labs. Most coding languages have something called "wrapper" code. Like a candy wrapper, it surrounds the code and tells you something about what is inside. There are many variations of wrapper code, but for the ARM Assembly Language in this class, we use the following:
```ARM
.global _start

_start: 

    @ Your code goes here!

    MOV R0, #0
    MOV R7, #1
    SVC 0

@ Any .data or other information goes down here!
```

## Step 4
Compile the code from Step 3 using the familiar `make DEBUG=1` command. Make sure to update your makefile with the new filename before using the `make` command. Get used to the process of Step 3 and 4, as you will be using it in every lab from here on out. **After completing this step, take a screenshot of your code from Step 3 and the terminal showing that it compiles with no errors.**

## Step 5
Run the debugger (gdb) with your new code.

## Step 6
Repeat the debugger process you have used in previous labs to check the value of R1 after the `LDR R2, [R1]` line. This is the memory address of `mynumber`. Stay in the debugger for the next step.

## Step 7
Use the command `x /4ubfx TheNumberYouFoundInR1` (replacing TheNumberYouFoundInR1 with the actual number, in hex) to check what is stored in the memory address held in R1. **After completing this step, take a screenshot showing the values stored at R1's memory address.** These should be in the reverse order of the values you had in the "mynumber" line because of Little Endianness. Stay in the debugger for the next step.

## Step 8
Step over the next line of code and make sure R2 contains the reverse of the value you saw using the `x` command (aka, the same order as `mynumber`). You can now leave the debugger.

## Step 9
Like in previous labs, change `mynumber` to your student ID in hexadecimal, `make DEBUG=1` the file, and disassemble your program using the command `objdump -s -d NameOfYourFile.o`. **After this step, take a screeenshot showing the disassembled code. In your lab report, note which memory addresses hold your student ID.**

## Step 10
You should have gone over different types of index addressing in class. This is your time to implement them on your own! For this part, you should have 4 groups of lines. I have added a template for this under "Step 10 Code" in the [Code Given](#code-given) section of this page, which you should use to replace the code in the same file as the last few steps. <u>If you are copy and pasting my given template, make sure to change the value of `mynumber` back to your student ID</u>. You should have 4 total comparisons, following this format:
1. Compare a Byte using `[R1, #1]` vs `[R1], #1`
2. Compare a Signed Byte using `[R1, #1]!` vs `[R1], #1` (note the ! symbol)
3. Compare a Halfword using `[R1, #2]` vs `[R1], #2`
4. Compare a Signed Halfword using `[R1, #2]!` vs `[R1], #2` (note the ! symbol)
**Take a screenshot of your code and include it in your lab report.**

## Step 11
Run the code in the previous step with the debugger, and show the values of R2 for each comparison (as in, you should have 2 screenshots/displays per comparison. One with the first R2, and one with the second. They may be the same value). **Take a screenshot of each comparison (there should be 4 comparisons for this part)**. If you can't fit both examples in one screenshot, then that is okay. **Make sure to discuess the differences in your lab report.**

## Step 12
Stores (STR) are like loads (LDR), except reversed. Instead of grabbing values from memory, they place values into memory at the designated address. Remember: LDR changes registers, STR changes memory. There is no action needed for this step. 

## Step 13
Now, make a new file with the code given in "Step 13 Code" in the [Code Given](#code-given). Update your makefile with the name, `make DEBUG=1`, and run the debugger. Once you step PAST the `STR R2, [R1]`, check the registers, find the value in `R1` (the memory address for `mynumber`), then run `x /4ubfx TheNumberYouFoundInR1`. What are the values at the memory address? **Discuss this in your lab report.**


## Step 14
Now, BETWEEN the `LDR R1` and `STR R2` lines in your code file, add the following lines:
```asm
LDR R2, [R1]
LDR R3, =0x01010101 
ADD R2, R2, R3 
```
This code adds the number 0x01010101 to your student ID, then stores it back in the original memory address. Go through the same process as Step 13 and **in your lab report, discuss what values are stored at the memory address.**

## Step 15
Go back to your file from Step 10/11. Under the line `LDR R1, =mynumber`, add `LDR R2, [R1]`. This will put your student ID into R2. Next, you are going to do exactly what you did in Step 10, but with STR commands. Simply replace all the `LDR`s with `STR`s (besides the ones in `LDR R1, =mynumber`) BELOW the line `LDR R2, [R1]`. Update the lengths (B, SB, etc) as follows:
1. Byte
2. Byte
3. Halfword
4. Halfword

## Step 16
Make sure you update the correct file in your makefile, then make it. Run the code in the previous step with the debugger, and show the values of at the memory address of R1 for each comparison (as in, you should have 2 screenshots/displays per comparison. One with the first memory address, and one with the second. They may be the same value). Remember that, to view the data at a memory address, you need to check the value of `R1`,  then run `x /4ubfx TheNumberYouFoundInR1`. **Take a screenshot of each comparison (there should be 4 comparisons for this part)**. If you can't fit both examples in one screenshot, then that is okay. **Make sure to discuess the differences in your lab report.**

## Step 17
**In your lab report, explain why there is no signed STR instruction.**

# Conclusion
In this lab, you applied your knowledge of loading and storing values in memory. This is a very important concept you will use in every lab from now on. You should also now have a concrete understanding of pre, post, and auto indexing and how it effects the addresses you load and store from. This lab was a bit harder than the last, so if you have any questions, be sure to ask a TA. We also have office hours if you have more questions. Be sure to turn in your lab report before next lab, and have a great weekend.


# Code Given
Listing 5-2:
```asm
@ load the address of mynumber into R1
    LDR R1, =mynumber
@ load the word stored at mynumber into R2
    LDR R2, [R1] 


@ Put this in the .data section of the wrapper, below everything else
.data
    mynumber: .WORD 0x1234ABCD
```
Step 10 Code:
```asm
.global _start

_start:
    LDR R1, =mynumber

    @Comparison Template:
    @ Line that loads a {byte/halfbyte/etc} into R2 from [R1, #1]
    @ Line that resets R1 to the address of mynumber if the address changes
    @ Line that loads a {byte/halfbyte/etc} into R2 from [R1], #1
    @ Line that resets R1 to the address of mynumber if the address changes

    MOV R0, #0
    MOV R7, #1
    SVC 1


.data
mynumber: .word 0x12345678
```
Step 13 Code:
```asm
.global _start

_start:
    LDR R1, =mynumber @Make sure to update mynumber in the .data section with your student ID
    STR R2, [R1] 

    MOV R0, #0
    MOV R7, #1
    SVC 0

.data
mynumber: .word 0xYourStudentID
```

