---
title: "Lab 7: Functions and the Stack"
author: Cooper Shapard
date: 2024-10-17
category: Jekyll
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab7/Lab7_FunctionsStack.pdf)

# Overview
Welcome to Lab 7. Here, you will learn how to use subroutines, a.k.a. functions, to avoid rewriting code multiple times. **This may be one of the most valuable/useful concepts you learn relating to ARM Assembly.** Functions can take multiple inputs and return multiple outputs and can be called multiple times from anywhere in your code. However, there are a couple different ways that you can send and receive data to and from a function. They are:

1) <u>Pass by Register</u>
- This works by leaving values in the register, then accessing those same values from both functions. It's like putting the values on a desk so that multiple people can work on them/change them without having to move them to a different location.

Pros: Easiest to understand and implement.<br>
Cons: Least amount of space for values and can have side-effects (side-effects mean some values may change that you did not want to change).

2) <u>Pass by Reference</u>
- This works by placing the desired values in memory, then just sending the address of that memory location to the function. It's like putting the values in a storage locker, then sending the key to another person. To get the results, you must go back to the storage locker and grab them yourself.

Pros: Most amount of space and no side-effects.<br>
Cons: Slowest method and allows for possible memory leaks (memory leaks are values that get "stuck" in memory and just take up space without doing anything).

3) <u>Pass by Stack</u>
- This works by pushing all the values onto the stack, then letting the function pop them off as needed. It's like putting the values in a box, then sending the box to someone. That person changes the values, then sends the box with the results back to you.

Pros: Large amount of space and no side-effects or memory leaks.<br>
Cons: Only the top value on the stack can be popped unless you add extra code.

**Pass by Stack is the preferred method by professionals** because it is fast, free of side-effects/memory leaks, and allows for something called *nested function calls*, which are a very important concept. Here is a written explanation, but check the official lab paper for some diagrams if you're a visual learner.

Nested function calls means that you can call another function within a function. Very useful for efficiency, but it's not as simple as calling the new function and moving on. The Link Register (LR) can only store one value at any given time. So let's say I go into a function with a Branch and Link (BL), setting the link register to my return address. If I then call another function within that function using another BL, then it will overwrite the old LR value, and we get stuck in the function since we don't have a return address. 

**The way to fix this is by *pushing* the value of the LR to the stack when we enter a new function and *popping* it when we leave the function.** This allows us to store multiple LR values, but only use the one that we need in nay given function. With that, you are ready for the lab!

I have simplified the steps for you below for organizational purposes. Remember, this is not a replacement for the lab guide, just a more readable way to phrase the information. If you need any help, be sure to ask a TA!

# Explanations
## Step 1
Read through pages 109-116 in the Smith book. It should be review from class, but please actually read it so you can get a different perspective on functions and the stack.

## Step 2
Use the instructions on page 116 to 121 to make the specified Uppercase Revisited program. Code provided in the [Code Given Section](#code-given). Make and run the code to check that it works. If not, ask a TA.

## Step 3
Choose your favorite stack convention (IA, IB, DA, DB), and replace all the PUSH and POP commands in your program with the correct STMxx and LDRyy commands (where xx and yy are your stack conventions). Choosing a stack convention is like choosing a starter pokémon. There's really only a few options, but that doesn't mean you won't drastically overthink which one to choose. Here is a quick table with some info (SP stands for Stack Pointer):

| Name | Abbreviation | Example | Why you should choose it |
|:----:|:------------:|:--------|:-------------------------|
|Increment Before/<br>Full Ascending|IB|0x200b0: Data1<br>0x200b4: Data2<br>0x200b8: Data3<br>0x200bc: Data4 <-- SP|Counts upwards and always<br> points to the last used data.<br> Best if you like to logically keep<br> track of where everything is.|
|Increment After/<br>Empty Ascending|IA|0x200b0: Data1<br>0x200b4: Data2<br>0x200b8: Data3<br>0x200bc: Empty <-- SP|Counts upwards, but conceptually<br> starts at 0 instead of 1.<br> Best if you have lots of <br> programming experience.|
|Decrement Before/<br>Full Descending|DB|0x200b0: Data4 <-- SP<br>0x200b4: Data3<br>0x200b8: Data1<br>0x200bc: Data1|Counts downwards and always<br> points to the last used data.<br> Best for people who like<br> to visualize the stack<br> like a stack of papers.|
|Decrement After/<br>Empty Descending|DA|0x200b0: Empty <-- SP<br>0x200b4: Data3<br>0x200b8: Data1<br>0x200bc: Data1|Counts downwards and always<br> points to the next avaliable spot.<br> Best for people who don't like<br> any of the other options and<br>just wants to choose one and<br>move on.|

Now, it's important to note that **The Store Sets the Protocol**. However, **your load should always use the opposite protocol**. I just remember this by flipping each letter in the protocol to the other option during the load. So, if you want to use Increment Before, you will use STMIB and LDRDA. If you were using Decrement After, you will use STMDA and LDRIB, etc.

For this step, go replace every `PUSH` command with STMxx (where xx is your protocol), and every `POP` command with LDRyy (where yy is the opposite of your protocol).

## Step 4
Make sure your code works the exact same way as it did in Step 2. If not, try to find and fix the issues on your own before asking a TA. **Take a screenshot showing that your program works with your chosen stack convention. Make sure to include this code in your lab report as well.**

## Step 5
Read through pages 121-124 in the Smith book.


## Step 6
Look at your modified code Step 3. This code uses *pass by register* to input and output the data to and from the function. Currently, R0 and R1 contain the addresses of the input and output string, and after the function executes, R0 is replaced by the length of the string. Your goal is to change this code so that it used *pass by stack* instead, which uses STMxx and LDRyy to send data to the toupper function. Then, use STMxx and LDRyy to get the length of the string into R0 after toupper executes. Note that you will need to manually offset the stack pointer to grab R0 and R1 from the stack, since R4 and R5 will go on top of them. Your offset may be positive or negative depending on your stack convention. It may help to draw out your stack so it is easier to visualize.

To convert your program from a Pass by Register to a Pass by Stack procedure, you need to store the values of `R0` and `R1` on the stack BEFORE you branch to the toupper function. Then, in the toupper function, after you add R4 and R5 to the stack (which you should already be doing from the original code), you need to load the values of R0 and R1 FROM the stack. However, since those values are not on top, you will need to offset the stack pointer by a certain number (positive if you are using a descending protocol and negative if you are using an ascending protocol). You must figure out what this offset is and how to change the stack pointer to get the values you want, while also making sure it ends up where it was before the offset. Before ending the function, you need to push the new value of R0 onto the stack (you can do this after the LDRyy statement that is already at the bottom of the function).

Then, when you return to the main function, you need to load the values of R0 FROM the stack. This should be done before the `MOV R2, R0` command so that the correct value is placed in R2. 

It's easy to get lost in all this pushing and popping, so just let a TA know if you get stuck, and we can come help flush it out!

### Tips
1. Remember to include the ! after the SP in your STMxx and LDRyy commands. So it should look like `STMxx SP!, {your registers}` and `LDRyy SP!, {your registers}`.
2. Everything on the stack is stored in sets of 4 bytes. If your stack has 2 values on top of the values you want, then how may bytes will you need to reach over to get the values you want? Remember to account for if you're using a Full or Empty stack protocol!
3. Confused on what is on your stack at any given time? Try to draw it out! The TA's can help you find scratch paper if you don't have any.

## Step 7 
If you have not already, modify your STMxx and LDRyy statements to include the Link Register (LR) so that your program returns to the same place after performing the subroutine/function. You might already have this from the code you modified, but if you don't, just add the LR to the stack when you store the values and pop it when you load them (but only in the STMxx/LDRyy statements in the toupper function). Make sure to update your offset to include the LR. **Take a screenshot showing your progam works with your new Pass by Stack method, as well as your finished code**


# Code Given
main.s (Listing 6-3):
```asm
@
@ Assembler program to convert a string to
@ all uppercase by calling a function.
@
@ R0-R2 - parameters to linux function services
@ R1 - address of output string
@ R0 - address of input string
@ R5 - current character being processed
@ R7 - linux function number
@

.global _start          @ Provide program starting address
_start: 
    LDR R0, =instr      @ start of input string
    LDR R1, =outstr     @ address of output string
    BL toupper
                        @ Set up the parameters to print our hex number
                        @ and then call Linux to do it.
    MOV R2, R0          @ return code is the length of the string
    MOV R0, #1          @ 1 = StdOut
    LDR R1, =outstr     @ string to print
    MOV R7, #4          @ linux write system call
    SVC 0               @ Call linux to output the string
                        @ Set up the parameters to exit the program
                        @ and then call Linux to do it.
    MOV R0, #0          @ Use 0 return code
    MOV R7, #1          @ Command code 1 terminates
    SVC 0               @ Call linux to terminate the program

.data
instr: .asciz "This is our Test String that we will
convert.\n"
outstr: .fill 255, 1, 0
```
upper.s (Listing 6-4):
```assembly
@
@ Assembler program to convert a string to
@ all uppercase.
@
@ R1 - address of output string
@ R0 - address of input string
@ R4 - original output string for length calc.
@ R5 - current character being processed
@
.global toupper             @ Allow other files to call this routine
toupper: 
    PUSH {R4-R5}            @ Save the registers we use.
    MOV R4, R1
                            @ The loop is until byte pointed to by R1 is non-zero
loop: 
    LDRB R5, [R0], #1       @ load character and increment pointer
                            @ If R5 > 'z' then goto cont
    CMP R5, #'z'            @ is letter > 'z'?
    BGT cont
                            @ Else if R5 < 'a' then goto end if
    CMP R5, #'a'
    BLT cont                @ goto to end if
                            @ if we got here then the letter is lower case, so convert it.
    SUB R5, #('a'-'A')
cont:                       @ end if
    STRB R5, [R1], #1       @ store character to output str
    CMP R5, #0              @ stop on hitting a null character
    BNE loop                @ loop if character isn't null
    SUB R0, R1, R4          @ get the length by subtracting the pointers
    POP {R4-R5}             @ Restore the register we use.
    BX LR                   @ Return to caller
```
makefile (Listing 6-5). **Note that this is different than you've seen before since you are combining two files during compilation** (Make sure that the `as` and `ld` lines copy over as a tab and not 4 spaces):
```makef
UPPEROBJS = main.o upper.o

ifdef DEBUG
DEBUGFLGS = -g
else
DEBUGFLGS =
endif
LSTFLGS =

all: upper

%.o : %.s
    as $(DEBUGFLGS) $(LSTFLGS) $< -o $@
upper: $(UPPEROBJS)
    ld -o upper $(UPPEROBJS)
```