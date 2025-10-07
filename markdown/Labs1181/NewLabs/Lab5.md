Logic
# Overview
Welcome to Lab 5. Last lab, you learned about literal pools and the CPSR flags. Today, you will use those flags for "conditional execution", which is similar to the "if statements" you see in other programming languages.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](lab-guide).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.





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
Four examples of you running your program with `./your_executable_name` (not gdb). They should be the first letter of your first name and last name, each with a different case, as well as the letters "A" and "z" with those specific cases. E.x.
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
A screenshot showing examples with +, -, and something else, ran using `./your_executable_name` (not gdb). The two numbers you use should be included in the screenshot of your code. E.x.
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

