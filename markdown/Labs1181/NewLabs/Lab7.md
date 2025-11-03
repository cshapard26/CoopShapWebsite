# Overview
Welcome to Lab 7. Last lab, you learned about branching, linking, and looping. Today, you will learn about the stack, a memory structure that lets you make a checkpoint for your registers.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](lab-guide).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.

# The Stack
In ARM, we have access to a special region in memory called the stack. This area is set aside for a small amount of data that we want to put down and pick back up. Think of it like a desk with a bunch of papers. If you are not currently using one of your papers, you move it to the side of your desk. Any new paper you aren't using (but still want quick access to) get "stacked" on top of that paper. The papers (data) are nearby for when we need them, but a stack of papers has to be relatively small.

Much like a stack of papers, there are rules to how we interact with the ARM stack. Data can only be placed and taken from the very top of the stack. If you want something from the middle of the stack, you have to take out everything above it first. When you want to put data on the stack, you "push" it to the top. When you want to take data off the stack, you "pop" it off the top.

A stack is something you will see in Data Structures class, so you're getting a sneak peek in this class.

# Why it's Useful
You have 12 registers available for use in ARM. No more. What happens if you are running a complex piece of code and need more than that? That's where the stack comes in. You can push a bunch of your registers onto the stack, preserving them in time. Then, you do some math with your newly freed registers, and eventually, you pop your old values back into your registers, which restored the state it was in before. Think of it like putting a checkpoint on your registers, and you can go back to that checkpoint whenever you need.

You also don't need to checkpoint all the registers at the same time. You can just say "save registers 1 and 2", and then restore those later. However, the important thing is that you keep track of what is on the stack and in what order. To do this, we use something called Stack Protocols.

# Stack Protocols
There are 4 stack protocols: Increment After (IA), Incremement Before (IB), Decrement After (DA), and Decrement Before (DB). They each line up with a way to structure your stack: Empty Ascending, Full Ascending, Empty Descending, Full Descending, respectively. Here is what that means. You reference the stack with something called a Stack Pointer (SP). The SP is just an address, and that address is always stored in a free register called "SP" (you can see this if you do `i r` in the debugger). The SP always points to the "top" element of the stack. You get to choose two things: does the stack increase upwards or downwards (increasing memory addresses or decreasing memory addresses), and if the address is of the highest *empty* spot on the stack or the highest *full* spot.

If you want to add a register to the stack with IA protocol, the stack is made with increasing addresses and the SP points to the top empty spot on the stack. Thus, to add a new element, you first put your register on the stack in the empty spot, then increase the SP to now point to the next empty spot. This is why it is called "Increment After." The stack pointer incremements after you add the value.

If you want to add a register to the stack with DB protocol, the stack is made with decreasing addresses and the SP points to the top (lowest address) filled spot on the stack. Thus, to add a new element, you first decrease the SP to point to the next empty spot, then you fill that with your register (so the SP is now pointing to that value). This is why it is called "Decrement Before," because the stack pointer decrements before you add the value.

Exercise for the reader: What happens in IB and DA protocols?

Choosing a stack convention is like choosing a starter pokémon. There's really only a few options, but that doesn't mean you won't drastically overthink which one to choose. Here is a quick table with some info (SP stands for Stack Pointer):

0

Now, it's important to note that **The Store Sets the Protocol**. However, **your load should always use the opposite protocol**. I just remember this by flipping each letter in the protocol to the other option during the load. So, if you want to use Increment Before, you will use STMIB and LDRDA. If you were using Decrement After, you will use STMDA and LDRIB, etc.

You can use ANY STACK PROTOCOL YOU WANT, but you need to make sure it stays consistent throughout your whole program.

# Using the Stack
If you want to put something on the stack (a region in memory), you need to use a store command, STR. However, because we can put multiple values on the stack in a single command, there is a bit of a change. Instead of STR, we do STM:

Instruction: `STM`
Usage: `STMxx SP!, {registers}`
Description: Places multiple (STores Multiple) register values on the stack. `xx` is replaced by the stack protocol (IB, IA, DB, or DA), and the registers can be comma separated or hyphenated (`{R1, R3, R4-R7}` places R1, R3, R4, R5, R6, and R7 on the stack).
Example:
1

IMPORTANT NOTE: When placing multiple registers on the stack, they are always placed in ASCENDING order, even if you are using a descending stack protocol. This means the registers can appear "upside down" when viewing memory. It also means that you should always push and pop blocks of the same size (if you push 4 registers to the stack, the next pop should be 4 registers too).

To pop registers off the stack, we do the opposite:

Instruction: `LDM`
Usage: `LDMxx SP!, {registers}`
Description: Pops multiple (LoaD Multiple) values off the stack into the listed register. `xx` is replaced by the REVERSED (opposite of STM) stack protocol (IB, IA, DB, or DA), and the registers can be comma separated or hyphenated (`{R1, R3-R5}` puts the top stack value in R1, the next one in R3, then R4 and R5). Note that the registers you load the values into do not have to be the same as the ones they originally came from.
Example:
2

Notice that you can use STM and LDM together to move values around in registers with little effort. For example, you can swap the values in two registers without needing a third, scratch register by doing this:
3

# Linking
The most important use for the stack is used when you do a branch and link (`BL`, remember from last lab?). The link register `LR` holds exactly one number: the place to return to after a branch and link. But what happens if you BL to another place before returning to where you were? You will overwrite the old LR value and won't be able to return. This is where the stack comes in handy. After getting link address from the LR, we put it on the stack. Then, we can branch and link to a new function and do the same thing. When it is time to return, we first pop off the top LR value from the stack, go to that place, then pop off the next LR value and so on. We can nest function calls as much as we like!

This is also useful when you want to branch to a subroutine without messing up your current registers. Let's say you have a subroutine that prints out text. To use the Linux System Call for printing to the terminal, you need specific values in R0, R1, R2, and R7. What if we have valuable information in those registers we don't want to lose before printing? Push them to the stack before the subroutine, then pop them back afterwards (includes nested funciton calls). I use IA stack protocol, but any will work:
4


# Conclusion
Here, you reviewed and learned about managing the stack in ARM. In future labs, you will learn how to interface the Red Pitaya with a breadboard.

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](cheat-sheet) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write a program that performs calculations without changing the values in your register.

Additional Requirements:
You must start off by filling all 12 registers with any value. 
You then must perform at least 3 operations (ADD, MOV, etc) that actually change values in at least 3 different registers.
You must end with the original 12 values in their original registers.

Assumptions:
The register values can change between the beginning and end of the program, so long as the program ends with the 12 values you started with.
You can use any stack protocol.
You can perform any operations.

Expected Outputs:
Running the program with `gdb` should show the registers (with `i r`) at the end of the program containing the 12 initial values.


## Task 2
Write a program that uses nested function/subroutine calls.

Additional Requirements:
You must nest at least three subroutines and return back to the original spot using branches, links, and the stack.

Assumptions:
Your program can do anything you would like, or nothing at all.
Any stack protocol can be used.

Expected Outputs:
Running the program with `./executable` should not result in any errors. You should also include a sketch of how the PC moves through your program over time.


## Task 3
Explain in depth what would happen if your STM and LDM protocols do not align (are not complementary).

Additional Requirements:
You must give a concrete example of what exactly would happen to the address values, registers etc. either written or with a program example. 
You must include descriptions of errors for two distinct stack protocol combinations.

Assumptions:
Any two stack protocol pairs can be used.
You can use as much text or images as needed to fully explain your thought process.

Expected Outputs:
A written document with optional screenshots showing/explaining the issues that occur when a mismatch between STM and LDM is present.