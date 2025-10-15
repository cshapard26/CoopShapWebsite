Logic
# Overview
Welcome to Lab 5. Last lab, you learned about literal pools and the CPSR flags. Today, you will use those flags for "conditional execution", which is similar to the "if statements" you see in other programming languages.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](lab-guide).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.

# Conditional Execution
Conditional Execution is a way to use ARM code so that some lines are executed *if and only if* a condition is true. This works very similarly to an "if" statment in higher-level languages like Python or C++. This is a very, very powerful tool. However, these conditional executions are structured a bit differently than "if" statements in other languages, which might take some getting used to.

Here is an example of a very basic condtional execution in ARM. I will explain what it does line-by-line:
1
 
1. The first two 2 `MOV` lines: You should know what these do by now. It puts the number 1 into R0 and the number 2 into R1.
2. `CMP R0, R1`: In the given code, this line compares the numbers in R0 in R1. It uses the CPSR flags to remember this comparison. A comparison is the first step for all conditional executions.
3. `MOVGT R2, #42`: This looks a bit familiar. Remove the `GT` and you get `MOV R2, #42`. You know what that does. But what about the `GT`? That stands for "Greater Than." So, if in the previous CMP statement, the first number was 'greater than' the second number, this line executes like normal. If the first number is NOT greater than the second number, then this line is completely ignored. In this example, 1 is compared to 2. 1 is NOT greater than 2, so this line is ignored. The MOV does not execute and R2 is still empty.
4. `MOVLE R2, #69`: Similar to the last line, but with an `LE`. This stands for "Less Than or Equal To," so this line only executes if the first number compared is less than or equal to the second number. NOTE: The same CMP can work for multiple conditional statements in a row. The CMP only goes away when the CPSR flags are overwritten by another command. In this example, we use the CMP from two lines ago and compare 1 to 2. 1 IS less than or equal to 2, so this line executes. Now, R2 contains the number 69.

These are the basics of conditional execution, and hopefully you can already see how powerful it can be. You can ignore a whole block of code unless a comparison is true, or you could choose exactly which number to put in a register based on the state of your program.

For your reference:
Instruction: CMP
Usage: CMP number1, number2
Description: Compares (CoMPares) two numbers and sets the CPSR flags accordingly.

# Notes on CMP
A couple things to note on the CMP command. First was mentioned above, which is that the same CMP takes effect until the CPSR flags are overwritten (often by another CMP, but not always). 

Second is that ANY command can have a condition code on it. I used MOV in the last example, but you could slap a `GT` on an ADD, LDR, or even an LSL. It is very versatile. 

Next, you might wonder how CMP knows which CPSR flags to set. Under the hood, CMP is actually just SUBS. It subtracts the second number from the first number and sets the condition codes based on the resulting number (but that number is not saved to a register, unlike a regular SUB command). This isn't something you should worry about, so don't think too deep into it when decided which condition code to use, but it's always good to know what it's actually doing in the system.

Finally, you might already notice how CMP differs from a regular "if" statement in code. In code, you would write `1 > 2` or `x != y`. However, in ARM, you declare the two numbers/registers first, THEN say what comparison should be used. It would be like writing `1 2, >` or `x y, !=`. The advantage of this is that the two numbers can be reused with many different comparators. 

# Condition Codes
In the last example, I showed you `GT` and `LE`, but those are only the beginning. Here is a list of the most useful condition codes and what they do. I will also include the CPSR flags that make these conditions "true", but don't worry about those and work based on the word logic, not the binary. I will use 1, 0, and x for the condition codes, where "x" means "doesn't matter whether it's 1 or zero."

1. `EQ`, "equal to," x1xx: The line executes if the first number and the second number are equal to each other, or the same value.
2. `NE`, "not equal to," x0xx: The line executes if the first number and the second number are NOT equal to each other, or NOT the same value.
3. `LT`, "signed less than", 1xx0 or 0xx1: The line executes if the first number is less than the second number, assuming you interpret the system as signed.
4. `LE`, "signed less than or equal to", 11x0 or 01x1: Same as `LT` but the line also executes if the two numbers are equal.
5. `GT`, "signed greater than", 10x1 or 00x0: The line executes if the first number is greater than the second number, assuming you interpret the system as signed.
6. `GE`, "signed greater than or equal to", 1xx1 or 0xx0: Same as `GT` but the line also executes if the two numbers are equal.
7. `LO`, "unsigned less than", xx0x: The line executes if the first number is less than the second number, assuming you interpret the system as unsigned.
8. `LS`, "unsigned less than or equal to", x10x: Same as `LO` but the line also executes if the two numbers are equal.
9. `HI`, "unsigned greater than", x01x: The line executes if the first number is greater than the second number, assuming you interpret the system as unsigned.
10. `HS`, "unsigned greater than or equal to", xx1x: Same as `HI` but the line also executes if the two numbers are equal.
11. `AL`, "always execute", xxxx: Alawys executes the line. The same as putting no condition code at all.

Generally, you will only use the first six. They should be pretty intuitive, but these will always be here for reference if you need it.

# Common Patterns
Here are some common patterns you will see in condition codes. I will use ADD for all the examples, but any command can be used.

ADDEQ, ADDNE. If you see something like this, it is working like an "if-else" statement from other programming languages. The first ADD is executed if the compared numbers are equal, and the second add is executed if the compared numbers are not equal. In every case, exactly one of these lines are executed. No more, no less.

ADDGT, ADDLE. This is just like the above. It says "if the first number is greater than the second, do the first add. Otherwise (if the number is less than or equal to the first), do the second add." Again, exactly one line is executed in every case. This can be used with any *complementary* pair of > and < signs (GE+LT or GT+LE)

ADDGT, ADDLT. This is similar to the aboves, but it leaves out the case where the two numbers on the same. Occasionally, you will want to ignore all code if the CMP numbers are the same. An example would be trying to match up two numbers. If the first number is greater than the second, subtract one. If it is less than the second, add one. And if they are the same, do nothing.

ADDGT, ADDEQ, ADDLT. A three way branch (like an "if, else if, else" statement). I bet you can figure this one out. It covers all cases, and exactly one will always execute.

You won't always use these patterns, but they are quite common and a good starting place for shaping your program's flow.

# Conclusion
Here, you reviewed and learned about logic and conditional execution in ARM using the CPSR flags. In future labs, you will extend this behavior to branches to allow for loop-like behavior or larger if-then-like statements. Good luck on your assignments, and have a great fall break!

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](cheat-sheet) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write a program that takes a one-letter input from the terminal and outputs the same letter with the opposite case (m -> M or T -> t, etc).

Additional Requirements:
Your program cannot use branching.
Your program must use conditional execution, as the case of the letter will not be hardcoded into your program.
Your program must format the output nicely.

Assumptions:
You can assume that the input will always be a single alphabetic character
You can look at an ASCII table to find the relation between upper and lowercaes numbers (they are stored as hex values in the pitaya).
You can use this Linux operator in your ARM code to take an input from the terminal:
```
    MOV R0, #1              @ Command type
    LDR R1, =yourtaghere    @ String to print
    MOV R2, #numberofchars  @ String length
    MOV R7, #4              @ System call type
    SVC 0                   @ Execute command 
'''
Where R1 holds the address where you want to store the input from the terminal and R2 holds the number of characters you want to accept.

As a reminder from Lab 1, you can use this Linux operator to output text to the terminal:
```
    MOV R0, #0              @ Command type
    LDR R1, =yourtaghere    @ Address to recieve to
    MOV R2, #numberofchars  @ Max input length
    MOV R7, #3              @ System call type
    SVC 0                   @ Execute command 
'''
Where R1 holds the starting address of your message and R2 holds the number of characters you want to output to the terminal.


Expected Outputs:
Four examples of you running your program with `./your_executable_name` (not gdb). They should be the first letter of your first name and last name, each with a different case, as well as the letters "A" and "z" with those specific cases. E.x. with one flip:
[Image here](TODO)

## Task 2
Write a program that takes a '+' or '-' from the terminal and outputs the sum or difference of two hardcoded numbers, respectively.

Additional Requirements:
If the user inputs something other than + or -, the output should be the letter `x`.
Both the sum and the difference of the two numbers must be positive and a single digit (0-9). I suggest using 5 and 2.
The output should be formatted nicely.
No branching, only conditional execution

Assumptions:
The two numbers can be placed in a register directly in the program code and do not need to be inputted from the terminal.
Before outputting the number, you will need to add 0x30 to it so that it formats correctly with ascii (0x31 is a text character '1' in ascii, etc). 
The user can input any single text character.
You can use both code snippets from Task 1 to input and output from the terminal.

Expected Outputs:
A screenshot showing examples with +, -, and something else, ran using `./your_executable_name` (not gdb). The two numbers you use should be included in the screenshot of your code. E.x. with one addition (uses 6 and 3 as the)
[Image here](TODO)

## Task 3
Explain what would happen if you put a condition code on a CMP statement (e.x. CMPEQ).

Additonal Requirements:
Include a tree-like diagram of the possible outcomes of a 3-level conditional CMP (you can use: `CMP R1, R2; CMPLT R2, R3; CMPGE R1, R3` or your own version like it), and include what we know after each stage.
Explain why this behavior would or would not be useful in an actual program.

Assumptions:
You can make a digital drawing or a physical one and take a picture.

Expected Outputs:
An illustration and explanation as listed in the requirements above.

