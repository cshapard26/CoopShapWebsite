# Overview
Welcome to Lab 8: The Final Lab! Last lab you learned how to use the stack in ARM. Here, you will learn how to interface with the General Purpose Input/Output (GPIO) Pins on your red pitaya with macros. You will receive a breadboard, resistors, LEDs, and jumpers (wires). You will then program your red pitaya to turn on the lights following a certain pattern.

# Macros
Here is an example of a macro in ARM code, followed by an explanation of what it does:
0

In this code, the first chunk is a macro, which is defined between `.macro` and `.endm` ("END Macro"). The first line contains the name of the macro (`addNumbers`, but this can be anything you want), followed by a list of parameters (these are like function parameters in other programming languages. You can name them whatever you want). The next line, `MOV R0, \num1`, moves whatever the input for `num1` is into R0. Same for R1. Then, the macro adds R0 and R1 and places the result in R2. Thus, when you run this macro, it will take the two inputs, add them, and place the result in R2.

For the first line of code, `addNumbers 10, 12`, you can see how to run the macro in code. You state the macro name, then define the inputs. Here, `num1` gets the value `10`, and `num2` gets the value `12`. Thus, after running this line, you get the result `22` in R2. What will happen when you run the next line? Exercise for the reader.

In ARM, macros are a lot like subroutines/functions. You define code for your processor to run, then can access that code repeatedly at any point. They both help to reduce repetition in your code, but there are a few key differences. 

The first is that a macro is *physically duplicated for each call*. Unlike a subroutine, where you branch your program counter to re-run the same code over and over, if you call a macro multiple times, you are actually adding more lines of code to your program. When you compile (`make`) your program, the processor goes to every instance of your macro and fills that spot with the full code. Thus, macros do not have the issue of pipeline flushing, but do need extra memory to run. You may think you are only running one line of code when you call a macro, but you are just inserting more code later on (running the `addNumbers` macro above actually takes 3 lines to run, even when you only call it in 1 line).

Another difference is that macros can take direct, hard-coded inputs. As seen in the above code, you can provide multiple numbers to a macro, which will get physically replaced in your code on compile time. This is different from subroutines, which use dynamic arguments given from the code. 

A common reason to use macros is to define a bunch of functions with similar behaviors that all vary with slightly different parameters. A great example of this is managing GPIO pins.

# GPIO
GPIO stands for General Purpose Input and Output. They usually are pins on a device that have no base functionality but can be programmed by the user to perform any action (either reading input from the pin or writing some output to the pin). All microcontrollers have some number of GPIO pins, and that is where you will implement all the functionality that actually effects the real world. You can use the GPIO pins to check when a button is pressed, get heat data from a thermometer, display information on a screen, turn on an led, etc. 

Your pitaya has 32 GPIO pins, but we will only use 3 in this lab. Follow the instructions below to set up your pitaya's GPIO pins in ARM. You will be creating a program that flashes LEDs (an ECE's dream project).

# Set Up
## Step 1
[Image here](/static/images/featured/ECE1181/gpio-diagram.png)

Wire your breadboard according to the picture above. Note the following:
1. The red pitaya has the golden bits facing upwards. This will make the logo on your case "upside-down."
2. The LEDs are diodes, which means you need to make sure you put them in the right way. One of the pins on each LED is longer than the other. *The shorter one should be plugged into the ground line (next to the blue line on your breadboard).
3. You should have 4 wires connecting to the red pitaya. Check to make sure everything is connected.

If you have questions or need further explanations, ask a TA.

## Step 2
Take out the wire connected to GPIO968 and connect it to the `+5v` pin on your red pitaya. This is the bottom right pin on the opposite collection of pins. This should turn on the LED. If it does not, try flipping around the LED. If it still does not, find a TA to check for defective parts. Repeat this process for GPIO969 and GPIO970. All your LEDs should be working before you continue.

## Step 3
Run the following command in the terminal to fix a change in the newer versions of the red pitaya: `overlay.sh classic`

To allow your pitaya to interact with the pins, set up the Linux GPIO API by running the following command: `cat /opt/redpitaya/fpga/classic/fpga.bit > /dev/xdevcfg`. (Note to Joseph and Hayden: if this doesn't run, ls and cd through the /opt/redpitaya/fpga library until you find an fpga.bit file. Any of them should work).

## Step 4
Run the following commands to activate the lights from your red pitaya. You will need to do this every time you connect to your pitaya:
1

If running these commands do not light up your LEDs, ask a TA for assistance.

## Step 5
The following files are listed in the [code given section](#code-given) of this lab guide. Create files with the specified names (the names must match exactly) and fill each one with their respective code: `gpiomacros.s`, `main.s`, `fileio.s`, and `unistd.s`.

## Step 6
Set your makefile to compile `main` as the top file, `make` it, and run `./main` (you may need to enter the password, "root", to run this command). You should see a change in the lights on your board. It may happen very quickly.

## Notes
If all these steps worked, you should have code that makes the LEDs flash in succession with 1 second between each flash. All of this behavior is defined in `main.s` and you are encouraged to read through that file to understand how the program works. It makes heavy use of macros that are defined in the other files you created.

# Conclusion
Here, you learned the basics of macros and working with gpio pins on the pitaya. All that is left in this lab is the final project, and you will have from now until the final lab day to complete it.

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](cheat-sheet) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write code that displays the value of R6 in binary on breadboard LEDs.

Additional Requirements:
Your code must count down from 7 to 0 to show all numbers working.
A reasonable (between 0.5 and 1.5 second) delay should occur between each number.

Assumptions:
The value in R6 will always be between 0 and 7 (three binary bits).
You can hardcode the starting number as 7, but your code must count down to show all numbers from 7 to 0.

Expected Outputs:
A video showing you running your code with the above functionality. Video can be zipped and attached to the lab submission.


## Task 2
Write code that generates a square wave of a specified frequency and outputs it on a GPIO pin.

Additional Requirements:
Your program must loop infinitely with this behavior, only stopping when typing `control+C` to cancel the terminal action.

Assumptions:
The frequency of the signal will only be between 1Hz and 500MHz.
The duty cycle is a fixed 50%.
Any pin can be used for the output.
You are generating a square wave, so a 1 (logic high) for x amount of time, then 0 (logic low) for x amount of time, repeating forever.
The frequency can be hardcoded into your program (either as frequency or period, no calculation is required).

Hint:
You can modify the nanoSleep macro to take an input argument, which is the amount of time in nanoseconds that the system waits before the next command is run.

Expected Outputs:
Test the program using a breadboard speaker and a 180 Hz frequency. You should hear a tone. Record a video and zip it for the project submission.


## Task 3
Write a macro that takes 3 input arguments `a`, `b`, and `c`, and performs the calculation `(a*b)^c`.

Additional Requirements:
The result must be placed in a register to be shown in the debugger.
You can use the `MUL` ARM command to multiply, but must implement the power operator yourself.

Assumptions:
The result will be within the 32 bit limit for registers.
Any numbers `a`, `b`, and `c` can be used such that `(a*b)^c` follows the first assumption.
The numbers can be hardcoded into your program, but not into the macro.

Expected Outputs:
A screenshot of the debugger showing the registers with `i r`, which contains the numbers `a`, `b`, `c`, and the result `(a*b)^c` in any registers. Specify which number is which in your lab report. You should have at least 3 examples of your program running this macro (should do it all at once with multiple macro calls.)


# Code Given
## gpiomacros.s
2

## main.s
3

## fileio.s
4

## unistd.s
5
