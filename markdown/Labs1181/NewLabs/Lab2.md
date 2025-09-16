# Overview
Time for Lab 2. In the previous labs, you learned how to navigate the terminal, work with ARM, and get things running on your pitaya. Now, we are going to start learning ARM commands and how to use them. From now on, labs will be less about reading and more about problem solving and learning through experience.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](TODO: Link here).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.


# Wrapper Code
Like most programming languages, ARM has some boilerplate code that you need to put in all files for it to work properly. We will be calling this "wrapper code" (since it wraps around your main logic), and this is what it looks like:

1

Recall from the previous lab that the "MOV, MOV, SVC" block is what ends your program. All code you write in this class will first start with this wrapper code.

# The MOV Instruction
As you should have seen in lecture, microcontrollers all come with registers (ARM has 12 you can use), which are places to hold numbers that are currently being used. These are named R0 through R11. One of the most important things you will need to do is place a specific number in a register or move a number between two registers. Here is the ARM instruction for that:

Instruction: `MOV`
Usage: `MOV destination, number`
Description: Places ("MOVes") a number into the destination register. If the number is another register, it copies that register's contents into the destination register.
Example:
2

Take a minute to figure out what value will be in each register after the following code is ran. Assume we are starting from scratch (all registers hold 0x0).
3

Here are the correct answers: R3=16, R6=0, R7=0x13 or 19 in decimal, R8=0. You may have been caught off guard by the last one. Note that this is a valid instruction in ARM, and it is just moving a register's content into itself, which makes no change. It may seem useless, and in this example it is, but later it will become a powerful tool.

IMPORTANT: If the "number" parameter is an actual number (e.x. #12) and not a register (e.x. R2), the the number MUST be one byte or less in length (0xFF in hex or 255 in decimal). The compiler will throw an error if you try a larger number.

# The ADD Instruction
As you might have guessed, the ADD instruction adds two numbers. It is one of the few raw commands on the microcontroller, and many other commands stem from it (multiplication is just repeated addition, etc). Here is how you use it:

Instruction: `ADD`
Usage: `ADD destination, number1, number2`
Description: Adds ("ADDs") number1 and number2 and places the result in the destination register. Note that number1 *must* be a register, and number2 can be either a register or a regular number.
Example:
4

In the last instruction, you can see how we can add "in-place" by making the destination register one of the operands. You will notice that most ARM instructions require a destination, and since registers are limited, we often want to save space by performing the instruction "in-place." This is an example of how you would do that.

Like before, take a minute to figure out what the final value of each register will be after this code is run from scratch:
5

Correct answers: r0=160, R1=80, R2=480. Notice how we can use the same register as many times as we want in a command, and that the old value will only be updated *after* the whole command is ran.

# A Quick Note on Binary
You should have seen binary in lecture and how it relates to both hex (hexadecimal) and decimal. For this next section, it will help to be able to convert between decimal and binary. You can use an online calculator for this, but make sure to understand how the conversion works first.

# Shifting and Rotating
Another concept you may have seen in lecture already, Shifting and Rotating are ways to modify binary values in a register. There are many types of shifting, but you only need to know these three for the lab:

Logical Shift Left (LSL): Moves all bits to the left one, and the leftmost bit "falls off" (disappears). The rightmost bit becomes a zero. Example: "101101" becomes "011010"
Logical Shift Right (LSR): Moves all bits to the right one, and the rightmost bit "falls off". The leftmost bit becomes a zero. Example: "11101" becomes "01110"
Rotate Right (ROR): Moves all the bits to the right one, and the rightmost bit becomes the leftmost bit. Example: "100001" becomes "110000"

Here is how you use them in your code:
Instruction: LSL, LSR, or ROR
Usage: `TYPE destination, number, amount`
Example:
6

Note that shifting/rotating is special in that you can combine it with other commands, making it an extension of the "number" operand. Example:
7

You can do this with any command, but note that it can only operate on the *last* number in the command. E.x. you can't do `ADD R3, LSL 3, #4, ROR 18`, but you can do `ADD R3, #4, ROR 18`, which would rotate only the #4 by 18 bits.

When you talked about shifting in class, you should've seen how the shifting type logically affects the output. Shifting to the left 1 bit multiplies a number by 2, and shifting to the right 1 bit divides the number by 2 (and rounds down). There is no easy mapping for rotates.

# GDB, the Debugger
Finally, we need to be able to see what is happening when you run your code. In the last lab, your code was designed to print things to the terminal (which is why we used a more complex program for the demonstration). Now, we want to see what is happening line-by-line inside the registers. We can't do this with basic terminal commands, so we need to run a new terminal app: GDB.

Command: `gdb`
Usage: `gdb executable`, where "executable" is the name of the file you want to execute (the one with no extension, not the .s)
Description: Runs the terminal app GDB ("Gnu DeBugger"), which allows you to step through and examine code while it is running

Remember, this command is run from the base terminal, not inside ARM or nano.

When you run gdb, it will look very similar to your regular terminal, except it will say `gdb>` on the left. That is your indicator that you are in the app. While in the app, regular terminal commands won't work, so you will need some new, app-specific commands. They are:

`b _start`: Creates a "Breakpoint" at the tag "_start", which is from your code. You can replace the _start tag with any other tag to start debugging your program from a different point.
`r`: "Runs" to your breakpoint. In this context, it means execute all the built-in code up to the _start tag and prepare to start executing code.
`s`: "Steps" over a single line of code. This executes the line and waits for the next command. IMPORTANT NOTE: the command you see listed after running `s` is the NEXT command, so it has not yet been executed. To execute that command, you need to step again.
`i r`: Reveals the contents of your registers ("Inspect Registers") in a nice format.
`exit`: Exits gdb and returns to the terminal

These GDB commands will be listed in the [Command Cheat Sheet](#TODO: add link) for your convenience. You will be using them often. A normal workflow looks like this:
1. Start running GDB
2. Set a breakpoint for _start
3. Run to the breakpoint
4. Step a bunch of times until you get to the line you want to check
5. Inspect the registers to see what numbers they contain at that moment
6. Step to the next part, inspect again, and so on
7. Once you get the info you need, exit the debugger

# One More Terminal Command
Now, I know you just got a lot of gdb commands thrown at you, but here's a terminal command that will save you quite some time.

Command: `cp`
Usage: `cp file, new_location`
Description: Copies ("CoPy") a file into a new location. If new_location is a directory, the file is copied exactly. If new_location is a file, the file contents are copied exactly but the name is changed to the new file name.
Example: `cp makefile ../Lab2`

Your makefile from last lab can be reused a lot, but you will want to keep your code from different labs in different directories. The example above is how you would copy the makefile (assuming you are inside a directory called ~/Lab1 and want to copy it to a directory called ~/Lab2). Using this will save you quite a lot of time and typing in the long run.

# Conclusion
This lab went over Moving, Adding, and working with the debugger. Unlike previous labs, this lab was focused less on reading and more on giving you descriptions and examples of how to use the tools. I encourage you to play around with these a bit before tackling the assignment portion below. Create a new file, add some wrapper code, MOVs and ADDs and Shifting, and then compile the file. Run the file with the debugger and step through it, checking the registers occasionally to see how your commands are affecting the registers. The assignments below are challenging and focused on using the commands and tools you used in fun new ways, so becoming comfortable with the toolset you have is the best way to approach these.

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](TODO: Link here) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](#TODO: add link) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.


## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write a program that makes a register hold your student ID (in hex).

Additional Requirements:
Your program can only use MOV, ADD, and shifting/rotating commands.
You must show the results by inspecting registers in the debugger.

Assumptions:
Your student ID will be in hex. That means if your student ID is 12345678, the register should hold 0x12345678. You do not need to use any converter for this, just enter all digits in hex instead of decimal.
Your SMUID is 8 hex digits (32 bits), which is within the 32-bit limit for registers.
Remember that an MOV command can only move one named byte (two hex digits) into a register at a time.

Expected Outputs:
Inspecting regisers in GDB should show your full student ID in any of the available registers. E.x.
TODO: Photo here

## Task 2
Write a program that rotates a number by a variable amount.

Additional Requirements:
Your program can only use MOV, ADD, and shifting/rotating commands.
You must show the results by inspecting registers in the debugger.
Debugging screenshots must include both the original number and the shift amount.

Assumptions:
You put the number and the shift amount in two differnet registers of your choice at the start of your program.
Any 32-bit number can be used (but you should stick with 1 byte numbers for ease), and the rotate amount should be less than 32.

Expected Outputs:
Inspecting regisers in GDB should show the number, shift amount, and result in any three separate registers. E.x.
TODO: Photo here

## Task 3
Write a program that adds two numbers, then saves only the last four bits. (e.x. 0x12 + 0xA4 = 0xB6 = 0b10110110. Last 4 bits = 0b0110 = 0x6, so the final register should only have 0x6 in it).

Additional Requirements:
Your program can only use MOV, ADD, and shifting/rotating commands.
You must show the results by inspecting registers in the debugger.
Debugging screenshots must include both original numbers and the result.
The two original numbers must be greater than 15.  

Assumptions:
You put both original numbers in two different registers of your choice at the start of your program.
Any 32-bit numbers greater than 15 can be used (but you should stick with 1 byte numbers for ease).
The resulting four bits do NOT need to be returned directly after the ADD. You can run as many instructions as you need to achieve this result, and the four bits need only need to be isolated sometime before the end of your program.

Expected Outputs:
Inspecting regisers in GDB should show both original numbers and the isolated 4-bit result in any three separate registers. E.x.
TODO: Photo here
