CPSR and Literal Pools
# Overview
Welcome to Lab 4. Last lab, you learned about loading and storing data inthe memory of your microcontroller. Today, you will learn about the CPSR and literal pools and how these are handled in your ARM processor. This will be a shorter lab, so enjoy the break!

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](lab-guide).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.

# CPSR
The CPSR, or Current Program Status Register, is a register in you ARM microcontroller that keeps track of certain processes while the program runs. This behavior allows for some very unique solutions to problems, but you first must understand how to use it. While the CPSR contains 32 bits of information, we will only look at the first four in this class, also known as the Condition Codes. These are NZCV, in that order. They stand for Negative, Zero, Carry, and oVerflow, respectively.

These flags can be set by any command in ARM, and the bits are set based on the result. Assume we add the numbers 10 and -10. The result will be Zero, and no carry/overflow occured, so the NZCV bits will be set to 0100. If we add 4 and -8, the result is -4, so the NZCV bits are 1000. Let's pretend we are in a 4-bit, unsigned system. If we add 0b1111 (15) with 0b1000 (8), we get 0b0111 (7). This is because the leftmost bit gets carried and there is no space for it in the 4-bit system. Thus, the NZCV bits of this example would be 0010.

Wondering the difference between Carry and Overflow? If you are adding 2 numbers with the same sign and the result doesn't make sense (add two negatives and get a positive, etc), then it is a carry. If you are adding 2 numbers with different signs and teh result doesn't make sense (large positive number + small negative number = negative number, etc), then it is an overflow.

Multiple bits can be set at the same time, too. In the same 4-bit system, what if we add 0b1111 (15) and 0b0001 (1). The result is 0b0000 (0) with a carry. So both the C bit and the Z bit are set. The CPSR flags would be 0110.

## How to set CPSR flags
Some ARM commands automatically set CPSR flags when run. Others need to be set manually. To manually force the CPSR flags to be set, you add an "S" to the end of the command name. For example, if you want to set the condition codes when performing an ADD, you would write the command as ADDS. MOV and ADD are examples of commands you need to force set, and LDR is an example of a command that sets them automatically.

## How to view CPSR flags
In the debugger, the CPSR register can be seen at the bottom of your register list when you run `i r` (it is a register, after all). NOTE: The 4 bits are the LEFTMOST four bits of the 32 bit register. If you see 0xb00000010, then the CPSR flags are 0xb, which is 0x1100 in binary, so N and Z are on. If you see the cpsr register as `0x10`, remember that those are the RIGHTMOST bits (leading zeros are removed), so the four CPSR bits are 0000.

# Literal Pools
Remember Lab 2 where you were asked to put a 32 bit number into a register, and you had to shift+add+shift+add a million times? That's annoying to write and also inefficient. If only there were a better way to declare a 32 bit number and place it in a register.

Boom. Literal Pools.

A literal pool is a place in memory directly between your program code and the .data section with user defined memory locations. The pool is reserved (and only exists) for any declared numbers that are too big for an immediate value. What the microcontroller does is, when compiling, replaces the large number in your code with the address for the literal pool and then puts the value at that address into a register. Essentially, it performs a load (LDR). 

So, how does this magic work? Instead of saying `MOV R0, #0xFFFFFFFF`, which will throw an error on compile, you write `LDR R0, =0xFFFFFFFF`. Notice that there is an `=` instead of a `#`, and that the command is LDR instead of MOV. If you write it like this, then you only need one line to place a 32-bit number in a register.

# Literal Limitations
Literal pools are very helpful, but they do have limitations. When locating where a literal (the number you are loading) is, the code only knows the distance between the command and the memory location where the literal is held. So the ARM processor says "oh, the literal is 60 bytes down, I'll go there, get the number, then come back." It doesn't know the objective address.

It does that because the address of the literal pool command is an immediate value, while memory addresses are too long to be used as an immediate value. An offset can fit. But only up to a certain amount.

In the ARM processor in your microcontroller, that limitation is 4096 bytes. That means that if there is more than 4096 bytes between a command and it's literal (stored right before the .data section), then the compiler will throw an error when you run `make`.

One way to add a bunch of bytes is with the `.fill` directive. The syntax for that is `.fill blocksize, numberofblocks, value`. This fills a section of memory with `numberofblocks` number of `blocksize` sized sections which all contain the number `value`. Note that blocksize must be <=8, and your value must fit in the blocksize.


# Conclusion
Here, you reviewed and learned about the CPSR flags and how literal pools work in ARM. In future labs, you will see how both of these can be applied to do some really cool things. For now, enjoy the short lab and good luck on the assignments!

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](cheat-sheet) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write code that produces the compiler error "invalid literal constant: pool needs to be closer."

Additional Requirements:
None

Assumptions:
Your program does not need to perform any action.
Your program will not be able to compile because of the error.

Expected Outputs:
A screenshot of the error message after you try to `make` the file.

## Task 2
Write code that produces all CPSR flags at least once when adding a number to your student ID.

Additional Requirements:
Your student ID must be loaded in a register using a literal pool.

Assumptions:
The number you add to your student ID is up to you, and you can change it as needed to get the correct flags.
Multiple bits can be set at any given time and can count for multiple examples. E.x. getting the CPSR values 0110 will count as both your Z and C bits.
All CPSR bits needs to be '1' at some point, and you can use as many programs/screenshots needed to show this occurring.
You can view the CPSR bits using the debugger.
You can do all the examples in a single program or update the file with new numbers for each example.

Expected Outputs:
One or more screenshots showing each CPSR bit set at least once, as well as the number you added to your ID to get that result.

## Task 3
Find the memory address of a literal in your code.

Additional Requirements:
You cannot use a tag to mark the start of the literal pool.

Assumptions:
Your code includes at least one line that loads a number into a register using the literal pool.
The result will have the memory address held in a register.
You can find the address of any literal if you have more than 1 in your code.

Expected Outputs:
You should use the debugger to list the address of the literal contained in a register with `i r` and display the content of that memory address with an `x` command to show that it really does contain the literal.
