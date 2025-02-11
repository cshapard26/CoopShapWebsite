---
title: "Lab 1: Getting Started"
author: Cooper Shapard
date: 2024-08-27
category: Jekyll
layout: post
---

[Download Lab Instructions](/ECE1181/pages/Lab1/Lab1_GettingStarted.pdf)<br>
[Download Red Pitaya Setup Instructions](/ECE1181/pages/Lab1/Headless_RedPitaya_Configuration.pdf)

# Overview
Welcome to Lab 1! Here, you will learn how to set up your red pitaya, connect to it using your laptop, and start writing some code. Luckily for you, this year all the red-pitayas will be given to you pre-assembled, which cuts down on the time-commitment of this lab. Remember that this online guide is for your convenience, but is not comprehensive and should not be used as a replacement for the official lab guide, which you can download above. If you find any errors in this guide—whether logic, spelling, or grammar—please let TA Cooper know so he can get it fixed up ASAP.

# Red Pitaya Setup
## Physical Setup
For the physical red pitaya, make sure you have done these things:
1. Place the microSD card into the slot
2. Plug the ethernet cable from the pitaya to your computer (we will be passing out adapters at the beginning of the lab)
3. Provide power to the board with the microUSB port. There are 2 ports, so make sure you are using the POWER one.

If you have completed these steps, you should see the light on the pitaya blinking green and occationally red. This is normal.

## Virtual Setup
### Connection
Now that your pitaya is all connected, we can make sure it is working digitally. To make sure you are connected properly, visit  http://rp-xxxxxx.local (replace the x's with the six digits on your red pitaya. It will be on the sticker with the QR code). If you are connected properly, you should be brought to a website that is pictured in the "Headless Red Pitaya" document. If the website times out, then something went wrong. See below for some troubleshooting tips.

### Troubleshooting
1. Double check the website name. It is case insensitive. You may also need to add a "/" at the end to connect (i.e. http://rp-xxxxxx.local/), but try it with and without the slash.
2. If you are using a VPN, you may need to disconnect from it to interact with the red pitaya.
3. Try flipping around the ethernet cord and/or the adapter. If you have a nearby friend who's device is working, try using their adapter and see if that is the issue.
4. If none of the above works, contact the nearest TA for assistance.

### Editing
Now, to edit and create files on your red pitaya, there are 2 options: VSCode and Vim. Some of the pitayas are on a different version and are not compatible with VSCode. If VSCode works, we suggest you use that, as it is a much easier interface and leads to less errors. We are currently finding a way to downgrade the pitayas so they are all compatible with VSCode, and we will keep you updated on that process. In the meantime, here is a brief summary of how to use each one.

#### VSCode
1. Download [VSCode](https://code.visualstudio.com/download) if you don't already have it. Set it up with the default prompts.
2. In the bottom left of the VSCode screen, you should see a little blue "><" button. Click that.
3. A popup should appear. Click "Connect Current Window to Host..."
4. For the next window, type `ssh root@rp-xxxxxx.local` where "xxxxxx" is your pitaya number.
5. For the system type, click "Linux".
6. If all goes well, after around 5-30 seconds, you should see a popup that asks for the password. It is `root`.
7. For compatible pitayas, you should see "SSH: RP-xxxxxx" or something similar in the bottom left corner in blue.
8. If you did not get this screen, try the whole process again, and try adding a "/" to the end of the `ssh` line (i.e. `ssh root@rp-xxxxxx.local/`). If none of the above works, your pitaya is likely uncompatible, and you will need to use Vim.

#### Vim
1. Open "Terminal" if you are on Mac and "Powershell" if you are on Windows.
2. When it opens, type `ssh root@rp-xxxxxx.local` where "xxxxxx" is your pitaya number, and click enter.
3. It should prompt you for a password. It is `root`. **You won't see the letters you are typing in the command line. This is normal. Just type "root" and click enter.**
4. You should now be connected to your red pitaya (you can check this by seeing what the beginning of the line in the terminal says. It should say "root $" or something similar instead of your laptop name).
5. To create a file, type `touch main.s`. This creates a file called "main.s" in the current folder (a.k.a directory).
6. Type `vi main.s` to start editing. This is the Vim window. It is VERY confusing, even to experienced users. Here is a general overview of what you need to know:
   1. To start editing, click `i`.
   2. To paste text, right click on your mouse/trackpad (it's not CMD+V in Vim)
   3. You can also type regularly.
   4. You cannot use your mouse to select an area or move your cursor. You need to use arrow keys to move around.
   5. When you are done typing, pres `Esc` a few times, then type `:wq` (do NOT press `i` before it. You should see the letters at the bottom left of your screen). The colon starts a command, the "w" stands for Write (as in "save") and the "q" stands for Quit. If you do not want to save, just type `:wq`. Accept any prompt that comes up, and you should be back to the regular command line.
   6. If you get stuck in Vim or have questions, ask a TA.

This should be everything you need to know to setup the Red Pitaya. If you encounter difficulty at any step, let the nearest TA know and we can help you through the process. **For the first lab, we will be prioritizing getting people's pitayas working. Please be patient if you have a coding question, as hardware errors are our primary concern.**

# Explanations
For this lab, you will need the Smith book, which is required for this class. You need a copy of the book, either digital or physical. You should buy an official copy from an official website to have the official book for the official class. Not a pirated one :)

Now, read through chapter 1. You can skim until page 17, where you will be getting instructions for this lab.

## Step 1
*Code from the book can be found in the [Code Given](#code-given) section of this guide.*

Type the code from the book into a new file called "HelloWorld.s". Next, add the two lines from the book into a file called "build". It should NOT have a filetype (i.e. .txt, .s, etc.). You can check to make sure all the files were created properly by typing `ls` into the terminal. This will list all the files in the current folder on your Red Pitaya. If you don't see "HelloWorld.s" and "build", ask a TA for assistance.

In your terminal (in VSCode, you can open the terminal using `Ctrl/Cmd + Backtick`) type this command: `chmod +x build`. This command basically just tells the computer to transform the file "build" into an executeable. We can finally start executeing some code. 

To compile your code, run `./build` in your terminal. This with create a new file called "HelloWorld" (namely different than "HelloWorld.s"). This is the code your computer can run. To run it, type `./HelloWorld` into your terminal. This should output the phrase "Hello World!" in the next line of your terminal. If it does not, ask a TA for asissistance.

## Step 2
### Part A
Here, you need to edit the code to make it more personal. To do this, change the string at the bottom of "HelloWorld.s" (Not "HelloWorld" or "HelloWorld.o") to "Hello [Your Name Here]!". Remember that the red pitaya needs to know how many characters to write on the screen, so you will need to update the line `mov R2, #13   @ length of our string ` to the new length of the string. Remember to include spaces, special characters, and the "\n" as a single character when counting.

To check that your program works, you will need to run it again. It is important to note that you must recompile your code EVERY TIME YOU MAKE A CHANGE. You can recompile using the command `./build`. Run your program again using `./HelloWorld`, which should output "Hello [Your Name]!"into the terminal. **Take a screenshot of the output, as well as your code, and make sure to include it in your lab report.**

### Part B
This next step is pretty simple. Go into HelloWorld.s and change the LAST `mov R0, #0` to `mov R0, #AnyOtherNumber`. Where `AnyOtherNumber` is a number other than 0. Recompile your code and rerun it. What happened? Take a screenshot of the output and write out what you saw happen in your own words. If nothing happened, take note of that as well.

# Conclusion
Congrats! You just completed your first lab for ECE1181. All that's left to do now is to write your lab report and submit it sometime before your next lab session. Check the official lab instructions for more information about what to include in your lab report. When in doubt, always include screenshots. You may have felt a little overwhelmed during this first session. That's okay. It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. We hope you have a great rest of your day and look forward to the next lab!


# Code Given
WARNING: I strongly recommend typing this into your Red Pitaya directly – The reason is that there are hidden symbols that may cause a high degree of frustration from copy/paste that would be spared by just typing it in. Also, you get a better feel for the code in doing so. You will likely not understand all that is happening in this code for now. That is okay. As the semester goes on, you will gain an understanding of everything you see below.

HelloWorld.s:
```asm
@ Assembler program to print "Hello World!"
@ to stdout.
@ R0-R2 - parameters to linux function services
@ R7 - linux function number

.global _start  @ Provide program starting @ address to linker
                @ Set up the parameters to print hello world
                @ and then call Linux to do it.
_start: 
    mov R0, #1          @ 1 = StdOut
    ldr R1, =helloworld @ string to print
    mov R2, #13         @ length of our string
    mov R7, #4          @ linux write system call
    svc 0               @ Call linux to print
                        @ Set up the parameters to exit the program
                        @ and then call Linux to do it.
.data
    mov R0, #0  @ Use 0 return code
    mov R7, #1  @ Service command code 1
                @ terminates this program
    svc 0       @ Call linux to terminate

helloworld: .ascii "Hello World!\n"
```
build:
```build
as -o HelloWorld.o HelloWorld.s
ld -o HelloWorld HelloWorld.o
```
