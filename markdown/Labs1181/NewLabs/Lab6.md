Branching and Linking
# Overview
Welcome to Lab 6. Last lab, you learned about conditional execution. Today, you will pair that conditional execution with a new type of statement: branching. Branching allows you to jump between lines of code and break the PC+4 behaviour you are used to seeing.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](lab-guide).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.

# Branching
Branching is a method in ARM that allows you to move the program counter to any arbitrary memory location. As you have seen in lecture, the program counter, or PC, is what tells ARM which line to run at any given time. On its own, it follows something called "PC+4" behaviour, which is where the the PC moves 4 bytes down after every line executed. Because instructions are 4 bytes long, this just means the PC executes one line after another, in order, and continues to do this through the whole program.

When you perform a branch, you move the PC to another location. You can use this to execute different blocks of code at different times without needing to put them all right next to each other in your program. Think of this like making function in higher-level programming languages. You can set a block of code that you execute many times without having to type it over and over. However, branching is much, much more versatile than just functions and makes up everything from loops to recursion to subroutines.

Here is a minimal code example using a branch, followed by an explanation of each line:
1

1. `MOV R0, #12`: Places the number 12 in register 0.
2. `B tagname`: This is your branch. You provide the branch instruction, `B`, with a single input: the name of any tag. The program counter then moves to that tag and starts executing code there. Here, the PC moves to the ADD command at `tagname` and skips all lines in between.
4. `tagname`: This is just a tag that marks the location of a line
5. `ADD R1, R0, #30`: This line adds the value in R0 and the number 30 and places the result in R1. Here, R0 contains 12, not 16, because the branch skipped that line. Thus, this line adds 12 and 30, and the result is the number 42 in R1.
6. `B end`: Another branch. This time, it jumps to the `MOV R0, #0` line in the middle, which is marked by the tag `end`.
7. `MOV, MOV, SVC 0`: You know this set of 3 lines as the Linux command that terminates your program.

This basic example just showed how to use branching to jump between spots in code. Notice that the line `MOV R0, #16` was *never executed* due to the way the branches were set up. Branches on their own aren't super useful besides just organizing code. Their strength, however, comes from their interactions with other ARM systems.

# Conditional Branching
One of the most powerful tools in all of ARM is a conditional branch. As you might expect, this happens when you put a condition code on a `B` command, such as `BGT` or `BEQ`. Here is an example of one reason to do that:
2

Without going line-by-line, lets follow the program.

First, we put some number into R0. Let's say we take that number as input from the terminal, so we don't know what it is by the time we run this code. Then, we go to the next line, marked by `beginning`. We compare a the input number to 0. If it is greater than zero, we jump to the `positive` tag. In the `positive` area, we subtract 1 from R0 and jump back to the `beginning` block, repeating the process. If R0 is less than zero, we jump to the `negative` tag. In there we add 1 to R0 and branch back to `beginning`. If the number is equal to zero, then we branch to `ending`, which terminates the program.

So, let's say that R0 starts at the number 7. Take a second to figure out what will happen as the program progresses. Answer: 7 is greater than zero, so we subtract 1 and start over. R0 continues this pattern, becoming 6,5,4,3,2,1, all the way down to 0. Once it hits zero, we branch and end the program.

Now try starting at the number -42. What will happen? Answer: We count upwards from -42 up to 0, i.e. -42,-41,-40,...-2,-1,0. Once we hit zero, we jump to the end of the program.

Hopefully you can now see how useful conditional branching can be, opening up tons of new doors for program functionality including looping and conditional code blocks.

# Linking
One very common way to use branching involves jumping to a block of code, then going right back to where you branched from and continuing on from there. Because this is so common, the inventors of ARM have a built-in way to do so. It is called Linking. How it works is that instead of using `B`, you use `BL` (for Branch and Link). When you do this, the current address plus 4 is placed in a special register called the Link Register (a.k.a LR, you can see it in the debugger when you do `i r`). 

Then, whenever you want to return to the line after your branch, you just run `BX LR`, which takes you back and clears the Link Register for new use.

For example:
3

Take a moment to think through what this program does (note that "MUL" is the ARM command to multiply two numbers). What is the final number in R1 before the program ends? Answer: 88. The program starts with the number 10 in R1, then jumps to the `doubleR1` section, which multiplies the number in R1 by 2 and then jumps back to the branch it just used to get there. R1 is 20 at this point. We then add 2 to get 22 in R1, and then double R1 twice in a row using the same branch as before. At that point, the program ends with 88 in R1.

Linking is very useful for creating the same functionality as a "function" in higher level languages like Python or C.

# A Warning
Take a second to think about what the following code block will do:
4

Answer: Starting at the top, we enter the `loophead` block. We put the number 0 into R0, then we branch to the top of the `loophead` block. There, we put the number 0 into R0 and branch to the top of the `loophead` block. There, we put the number 0 into R0...

You get the point. Using branches, it is possible to get stuck in an *infinite loop*. Always make sure to check for this as a possibility. If it is occuring in your code, whay you will see is that you run `./executable_name` to start your program, then the terminal gives no output and does not give a new shell prompt. This is similar to how it looks when it is waiting for user input. However, no matter what you type in the terminal, nothing will happen. Higher-level languages are smart enough to crash when you go into an infinite loop. ARM is not. It will literally run forever if you let it. How do you stop it? In the terminal, press `Ctrl+C` (for Mac users, this is still control, not command C). This does not mean "copy" in the terminal, it means "cancel" and will immediately terminate any running program. Use it as needed.

# Common Patterns
## Creating a loop
To create a loop that runs a block of code for `x` number of times, first, decide on a register to be your index, which will keep track of what loop you are on and start at 0. Then place the code you want to repeat in a tag. At the end of the group in the tag, you want to compare your index to `x`. If it is greater than or equal to `x`, you will leave the loop and go to the next block of code. If your index is less than `x`, you will add 1 and branch back to the start of the tag marking your loop. Example:
5

## Blocked Ifs
If you want an "if-elseif-else statement" with a lot of lines in each part, then you might want to use a system like the following, which executes one of three blocks of code depending on a condition, then makes sure all paths end up back on a main path (`other_code` here):
6

## Functions
See the Linking section for an example of how to make a function. These don't take any inputs (yet! that's next lab), but can execute the same block multiple times without deviating from your main path of code. They are typically done with `BL` and `BX LR` commands.

## Fall Through Conditions
One very important thing to note is that, if a conditional branch doesn't execute (because the condition is false), then ARM continues with PC+4 behavior and executes the next line in the program. This can either be very helpful or very problematic.

Here is an example of an INCORRECT way to use fall-through conditions:
7

See the issue? When the BLT is run, it will branch to `number_less_than` if the condition is true. But if it is not true, the Branch is skipped, and we run the next line. The next line is in the `number_less_than` section too!! This means that no matter if R0 is more or less than 1, we always go to `number_less_than`, which is obviously not what we intended.

Here is an example of a CORRECT and clever way to use fall-through conditions:
8

Subtle difference, right? The ordering of the `number_less_than` and `number_more_than` are different. Now what happens at the BLT? If the number is less than 1, we skip over `number_more_than` and go to the `number_less_than` section, just like we intend. If the number is NOT less than 1, then we ignore the branch and run the next line, which is in the `number_more_than` section. This is exactly where we want to be, and by using a fall-through condition instead of a separate `BGT number_greater_than` line, we have saved a line of code AND reduced the number of branches in our program, which noticeably speeds it up (it's the difference between 0.001 microseconds and 0.0011 microseconds, but still, that compounds over time).

Fall-through conditions are very useful if you use them right, but always make sure you are ending a code block with a branch unless you intend to fall-through. Else, you may do so by accident and mess up your program logic.


# Reference Linux Commands
## Take input from the terminal
9

Where R1 holds the address where you want to store the input from the terminal and R2 holds the number of characters you want to accept.

## Print text to the terminal
10

Where R1 holds the starting address of your message and R2 holds the number of characters you want to output to the terminal.


# Conclusion
Here, you reviewed and learned about braching and linking in ARM, as well as how to tie it with conditional execution. In future labs, you will learn how to nest branches using the stack.

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](cheat-sheet) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write a program that prints the numbers 0 to 9 to the terminal.

Additional Requirements:
Each number must be on its own line, formatted nicely.
You cannot just write the same print statement 10 times. You need to use a branch like a loop.

Assumptions:
Your program will take no input.
You understand the difference between the number 1 and an ascii "1" (one of them is 0x1, the other is 0x31). Use an ascii table if needed. Output to the terminal must be in ascii format or it won't be displayed correctly.


Expected Outputs:
Running your program with `./your_executable_name` (not gdb) should print the numbers 0-9 in order, each on its own line. Example:
[Image here](/static/images/featured/ECE1181/Lab6Task1.png)


## Task 2
Write a program that takes a text input from the terminal and outputs the same text, but all in uppercase.

Additional Requirements:
Numbers, symbols, and already uppercase characters should not be affected.
In your output, you must include at least one edge case with the characters "@" and "[".
The output must be formatted nicely.

Assumptions:
The user will input between 1 and 50 characters.
You can look at an ASCII table to find the relation between upper and lowercaes numbers (they are stored as hex values in the pitaya).

Expected Outputs:
Three screenshots showing you running your program with `./your_executable_name` (not gdb), entering a text input, and getting an all-uppercase output. You can include all three tests in the same screenshot if they fit. Example:
[Image here](/static/images/featured/ECE1181/Lab6Task2.png)

## Task 3
Write a program that continues to prompt the user "Would you like to quit?" until the user types "y", then says "Goodbye!".

Additional Requirements:
If the user types anything other than "y", the prompt will be displayed again on a new line.
The user's input must be shown on the same line as the prompt.
The outputs must be formatted nicely.

Assumptions:
If the user types a phrase longer than 1 character, but it begins with "y", this can be considered a way to end the program.
The user will input between 0 and 50 characters.
The program will terminate after "Goodbye!" is displayed.

Expected Outputs:
Three screenshots showing you running your program with `./your_executable_name` (not gdb), entering any number of non-"y" characters, then ending with a "y". The three screenshots should include different numbers of non-"y" inputs, with one being at least 5 prompts long. Example with three non-"y" responses and ended with a "y":
[Image here](/static/images/featured/ECE1181/Lab6Task3.png)


