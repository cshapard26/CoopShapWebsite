---
title: "Lab 5: Literal Pools and Logic"
author: Cooper Shapard
date: 2024-09-25
category: Jekyll
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab5/Lab5_LiteralPoolsLogic.pdf)

# Overview
Welcome to Lab 5! In this lab, you will expereince first-hand how literal pools are handled by the Red Pitaya and how to implement conditional execution in your code. You should have heard about literal pools in lecture, but if not, let a TA know and we can explain them.

As always, this guide is a supplement for the official lab instructions, not a replacement. When in doubt, refer back to the official instructions. If you need any help or clarification, be sure to ask a TA. The old lab guides are avaliable in case you want to freshen up on the skills you have already learned.

# Explanations
## Step 1
Read through pages 92-95 (Please actually do this).

## Step 2
Reuse your code from Lab 1 with a modern makefile (if you don't have the code from Lab 1, I have also included it in the [Code Given](#code-given) section), and use the `x /4ubfx addressInR1` command to check the contents of the memory at the specified address. Note that this will print the hex value of the ascii characters. If you would rather see the actual ascii characters in memory, you can use `x /4ubfs addressInR1`. **Take a screenshot of the memory location**, and discuss the range of memory of the string in your lab report. Make sure to note the *address* of the memory as well as the length of the block in memory (it will be more than you printed).

## Step 3
Add any number of Arbitrary Commands AFTER the last `SVC 0` statement, but BEFORE the `.data` section. Some examples of Arbitrary commands are moving a `#0x0` into a register, Adding 0 and 0 and putting the sum in a register, and similar tasks. **Take note of the total number of bytes you are adding.** When figuring out how many bytes you added to the program through your Arbitrary Commands, remember that each ARM command is 4 bytes long.

NOTE:
You may remember that the last `SVC 0` statement exits the program. So, it's fair to ask, why are we adding commands after that line? Basically, the makefile will compile the code as it is written. It is not aware that the program ends at the last `SVC 0` statement. However, if you try and run through the program in the debugger, it won't execute the arbitrary commands you added. The reason we are putting them after the `SVC 0` statement is to create a *seperation* between the code and the `.data` section. The only way to do this without getting a compiler error is to add actual commands, even if they won't be executed.

## Step 4
Use the `make DEBUG=1` command again and check the new memory address at R1 like you did in step 2. **Take a screenshot of the new location. In your lab report, explain if the number of Arbitrary Commands you added lines up with the new location in memory.**

## Step 5
Now, add a very large about of bytes in the same place as the Arbitrary Commands from earlier. You will need at least `4096 Bytes` to successfully get the error message described in the lab report ("Error: invalid literal constant: pool needs to be closer"). **Take a screenshot of the error message**, which will occur when you try and *make* the program. Describe in your lab report how you made this occur. 

There are a couple options you can do for this. I suggest either using a `.fill` command or a `.ascii` command with a very large string, like a copypasta. The fill command is probably cleaner, and you can read about how to use it on page 90 in the Smith textbook under Table 5-1.

## Step 6
Create a new file called `inputASCII.s`, and fill it with the code in the Code Given section of the instructions. Be sure to update the `makefile` with the new file name.

## Step 7
After using the `make` command, run the program. NOTE: you are NOT running the debugger for this step. You can run the program by entering `./inputASCII` into the terminal, like you did in Lab 1. The program then expects you to enter a character, so if it is not doing anything, just type a single letter in the terminal and click Enter. This should print out the same character that you just entered. **Take a screenshot showing the same character being printed out.** If this does not happen, let a TA know and we can help debug. 

NOTE: 
You may notice that the second SVC command is printing out 2 characters. This is so that it includes the `\n` character, which formats the output nicely on the screen.

## Step 8
You don't need to do anything for this step, but it tells you to be aware that when you are in the debugger, stepping over the first `SVC 0` command will prompt you for a character like in step 7. It may seem like an error, but just enter in the character and click enter, and it will move on to the next line in the debugger like you are used to.

## Step 9
"Wow!" you say, "I've been speeding through this lab. I bet I will get out 2 hours early!" 

And then you got to step 9.

This guide isn't meant to just give you the answers, so you will need to complete this step on your own. You will be actually writing code for the first time. As with all new experiences, you may encounter some difficulties. You can use as many or as few lines you need to complete the step. There are many ways to approach the problem, and any solution that works will get full credit. Know that the TA's are here to help you with logic and debugging your code!

Before you begin, I would suggest pulling up an ASCII table online to use as a reference.

Without further ado, here is your task:

Modify the code from Step 6 to convert any inputted lowercase letter to Uppercase AND any inputted Uppercase letter to lowercase. Instead of printing out the same character like in Step 7, it should print out the same letter of the *opposite case*, (so, it should print out `A` when you enter `a` or `n` when you enter `N`). For simplicity's sake, you do NOT need to check if the character entered is an alphabetical letter. You will NOT know if the letter is Uppercase or lowercase before it is entered, so you will need to check for that in your code.

You will input your new code between the STDIN and STDOUT section of `inputASCII.s`. This means your code should go here:

```asm
     mov R7, #3     @ read 
     svc 0          @ Call linux to receive input 

@ YOUR CODE GOES HERE.

     mov R0, #1     @ 1 = StdOut 
     ldr R1, =msg   @ string to print 

```

To code this part, you are NOT allowed to use branching. However, you will need to utilize Conditional Execution. You can read about these on page 71 in Table 4-1. I would also recommend reading about the `CMP` instruction on page 71. Here is an example of how you would use these commands (the code is unrelated to your assignment, but should give you an understanding of how to use Conditional Execution):

```asm
CMP     R1, #0x12   @ This line compares R1 to the number 0x12. It will set condition codes based on the result. This works exactly the same as a SUBS command, but without storing the result.
MOVGT   R2, R1      @ This moves the value of R1 into R2 ONLY if R1 is signed Greater Than 0x12 (as defined from the condition codes in the previous line).

CMP     R4, R2      @ This line compares R4 to R2 and sets the condition codes
ADDNE   R3, R2, 0x1 @ This line adds R2 and 0x1 and stores the result in R3 ONLY if R2 and R4 are Not Equal (as defined from the condition codes in the previous line).
SUBEQ   R3, R2, 0x1 @ This line subtracts 0x1 from R2 and stores the result in R3 ONLY if R2 and R4 are Equal (as defined from the condition codes in the CMP line). Note that the CMP condition codes continue to apply until the CPSR flags are overwritten (either by a command ending in an S or another CMP).
```

Notice that the range of ASCII values for ‘A’ to ‘Z’ is 0x41 to 0x5A and the range for ‘a’ to ‘z’ is 0x61 to 0x7A. Think about a mathematical operation that you could use to convert a lowercase letter to the same Uppercase letter. Since you know that the input will be a letter, I would suggest picking either 'a' (0x61) or 'Z' (0x5A) and know that any number above this range is lowercase and anything below this range is Uppercase. Note that one of these will be Greater Than/Less Than or Equal To, and the other will be Greater Than or Equal To/Less Than.

At this point, you should be able to tackle the problem on your own. Test around and see what works, and feel free to ask a TA for assistance.

*To run/test your code:*
Follow the same procedure you used in step 7. However, if your code is not working, you may want to use the debugger to check registers/values.

Make sure to test "edge cases." If you test the letter 'Z', do you still get 'z'? what about 'a' to 'A'? If the other tests work, but one of these don't, then you may check your conditional execution statements to see if they are "Greater than" or "Greater than or equal to".

## Step 10
**Take a screenshot of your code**. In your lab report, explain what it does line-by-line (only for the parts you added).

## Step 11
Test your program by running it without the debugger. You should input 4 tests:
1. Your first initial of your first name in lowercase (which should print out your initial in UPPERCASE on the next line).
2. Your first initial of your first name in UPPERCASE (which should print out your initial in lowercase on the next line).
3. Your first initial of your last name in lowercase (which should print out your initial in UPPERCASE on the next line).
4. Your first initial of your last name in UPPERCASE (which should print out your initial in lowercase on the next line).
**Take a screenshot with all 4 tests. You should be able to fit it all on one screen.**

# Conclusion
Hopefully, you now have a better understanding of how Literal Pools work within the ARM Processor. Though you likely won't come across the `pool needs to be closer` error during this semester, it is important to keep in mind why this happens for when you work with microcontrollers in the future. You also implemented Conditional Execution for the first time in this lab. You will need to use this for most labs moving forward, and it's truly the first step towards industry level Assembly coding. This is also the first lab where you are truly implementing a solution all on your own. This will be a recurring theme, so get used to writing your own ARM code! If you have any more questions, specific or general, make sure to ask a TA. Have a great weekend!

# Code Given
Lab 1 code (please replace all the messages in the "{}" characters, there are 2):
```asm
.global _start

_start: MOV R0, #1
    LDR R1, =helloworld
    MOV R2, #{The number of characters in your .data helloworld line. '\n' counts as a single character}
    MOV R7, #4
    SVC 0

    MOV R0, #0
    MOV R7, #1
    SVC 0

.data
helloworld: .ascii "Hello {your name here}!\n"
```
inputASCII.s:
```asm
@ 
@ Assembler program to input ASCII characters via stdin 
@ The program will transform a lower-cased character to upper case 
@ or an upper case character to lower case 
@ R0-R2 - parameters to linux function services 
@ R7 - linux function number 

.global _start      @ Provide program starting at address to linker 
                    @ Set up the parameters to retrieve the character and then call Linux to do it. 
_start:   
    MOV R0, #0      @ 0 = StdIn 
    LDR R1, =msg    @address to receive input 
    MOV R2, #1      @only receive one character 
    MOV R7, #3      @read 
    SVC 0           @ Call linux to receive input 
                    @ Set up stdout to echo that character back and then call Linux to do it. 
    MOV R0, #1      @ 1 = StdOut 
    LDR R1, =msg    @ string to print 
    MOV R2, #2      @ length of string (include ‘\n’ to print nicely) 
    MOV R7, #4      @ linux write system call 
    SVC 0           @ Call linux to print 
    
    MOV R0, #0      @ Use 0 return code 
    MOV R7, #1      @ Service command code 1 terminates this program 
    SVC 0           @ Call linux to terminate 

.data 
msg:   .ascii "0\n"
```