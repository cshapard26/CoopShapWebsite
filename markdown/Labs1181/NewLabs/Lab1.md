# Overview
Welcome back to the Microcontrollers lab. In this lab, we are going to look at ARM Assembly code, how it works, how to compile it, and make some light modifications. 

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](TODO: Link here).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP.

# The ARM Philosophy
The purpose of ARM is to write machine-level commands for microcontrollers with ARM architectures (a very large chunk of modern computers). This type of code is often called "low level," where the level is referring to how close you are to just coding in straight binary. ARM is one level above that. By coding in the ARM Assembly Language, you are doing the closest human-feasible thing to coding in raw binary 1's and 0's. 

The main philosophy of how ARM Assembly works is this: few commands, and each do exactly one thing at a time. You are trying to make a program with the smallest possible units.

If you have programming experience in any language, this might be unintuitive (if you don't have programming experience, don't worry. After this class, you will get to brag that your first language was Assembly). The goal of most languages is to pack as much computation, logic, or decision-making possible into a single statement. That's what if-statements, loops, and lists/arrays are for. ARM doesn't have any of those, they make you do it from scratch.

But why? Why learn ARM if it is just making everything more complicated, takes longer to code, and has less functionality than literally every other programming language? To that, I respond: good point. You will probably never be asked to write assembly code in real life (unless you go into specific fields like computer architecture). But that's not the point. The point is learning how computers operate at the most fundamental level. 1's and 0's don't get the luxury of if-statements or loops. Logic gates don't know what a string is. The point is to understand how these machines think, how to talk with them, and how to use them at maximum performance.

The computer that you are using probably has at least 8 GB of RAM. That is an objective buttload of memory available to you. You can write a Python program however you want, and the code itself is not going to make a dent in that. Real microcontrollers, the ones that run all devices from coffee machines to game controllers to speakers to pace-makers? Top dollar ones will give you less than 10 MB. The ones you will be working with will be in the 10's of KB or less. Kilobytes. You get 10,000 bytes to work with. That's it. The standard python package with no libraries is 232,000,000 bytes (232 MB). 

As you may be starting to see, ARM Assembly makes a lot more sense in the context of actual microcontrollers. You goal is to make a program as small as possible, as fast as possible, as optimized as possible. You cannot get that level of sheer performance with any other language (even Rust, don't even go there). With ARM, you are only paying memory for *exactly* what you need to compute. No more, no less. That is the ARM philosophy.

# ARM Code
ARM code (which is what I will be calling ARM Assembly of the ARM7TDMI variant) is based around 4 main commands: MOVE, ADD, LOAD, STORE, as well as variants of these. You will learn how to use each of these commands in future labs. What makes ARM better than other assembly languages is that it offers lots of other commands without any performance costs.

Here is an example of a basic script you might see in ARM:
```arm
.global _start

_start:
    MOV R0, #1              @ Command type
    LDR R1, =helloworld     @ String to print
    MOV R2, #13             @ String length
    MOV R7, #4              @ System call type
    SVC 0                   @ Execute command 

    MOV R0, #0
    MOV R7, #1
    SVC 0

.data
    helloworld: .ascii "Hello World!\n"
```

This code prints "Hello World!" to your terminal when run.

A couple things to note before we dive in to what each line means:
    1. The commands are all case insensitive. `MOV` is the same as `mov` is the same as `Mov` (`r1` == `R1`, `ldR` == `lDr`, etc). You can use whichever you prefer in your own code, but I will default to using all caps in the examples given.
    2. As with all programming languages, ARM supports comments. These are designated by the `@` symbol, and anything after it is ignored by the program. These are just used for you to document your thoughts, or for me to explain what things do (in future labs, where I won't be explaining every line). The spacing between comments and code is not required, but I will default to lining up the comments so they are easier to read.
    3. The tabs before the commands are optional. In general, ARM ignores all whitespace (i.e. you can put as many spaces between text as you want, indent wherever, etc).

You are not expected to know or fully understand what all this code does in this lab alone. You will be working with ARM a lot moving forwards, and the more you work with it, the better you will get and the more you will understand. In fact, the program given is quite complex for an introduction. The reason we are using it is because it gives you a visual indicator that things are working (by printing to the terminal). 

Here is the play-by-play for this program:
1. `.global _start`
    Tells the computer that your program begins at the address associated with `_start`. Remember how I said that you only get around 10,000 bytes on a standard microcontroller? Your program doesn't start on the first byte. It will probably get stored somewhere around byte 6,000. The computer needs to know where your program starts, and the "_start" keyword is used to tell it that. Anything in ARM that starts with a `.` is called a "directive" and is used for giving the system context. `.global` means that *this* "_start" should be used as the starting point for all programs (makes more sense when you realize you can have multiple ARM files working together).
2. `_start:`
    As mentioned above, "_start" is where you program begins.
3. `MOV R0, #1`
    This can be read as "Move, into R0, the value 1". You should have seen what registers are from lecture, but they are essentially your "variables" in ARM. You get 12 of them total. If you need more, you have to overwrite old ones. Each register holds 32 bits of data. Here, we are saying "replace whatever value is in register 0 with the number 1". After this command executes, R0 will hold the hex number 0x1. You will learn more about MOV commands in the next lab.
4. `LDR R1, =helloworld`
    This can be read as "Load, into register 1, the memory address of the `helloworld` tag." Similar to MOV instructions, LDR (load) instructions replace the value of a register with a new one. The difference is that they go through memory (you will see this more in future labs). The `=` sign means "find this tag". "Tag" is what I will be calling lines that start with something + a colon (:). `_start:` and `helloworld:` are two tags in this program. Tags are used to mark a memory address (you will learn about these in future labs). So, what this command is doing is finding the memory address associated with the tag `heloworld` and putting that address in R1 (register 1).
5. `MOV R2, #13`
    Another move command, works the same as line 3. This one moves the value 13 (0xD in hex) into register 2.
6. `MOV R7, #4`
    This one is left as an exercise for the reader.
7. `SVC 0`
    This is a command that executes some sort of system-wide protocol. In this lab, you will see this be used to execute Linux commands from inside ARM code. To use `SVC 0`, you need to add some configuration to it. This configuration is stored in registers 0 through 7. The content in these registers tells the SVC what to execute and how to execute it. We will go over this configuration more in a second. Just know that, once the program reaches an `SVC` command, it will execute whatever system call it is configured to do.
8-10.
    More `MOV`s which configure another system call, then executed at the `SVC 0`.
11. `.data`
    This is another directive, which is used to mark where program ends and user-defined memory begins. In this section, you cannot execute commands, but you can store large quantities of data. Generally, data in this section will follow the pattern `tag: directive content`. Where the tag marks the memory address, the directive tells the system what type of data is stored there, and the content is, well, the content. The `.data` section will continue until another section is declared using a directive or the system runs out of assigned memory.
12. `helloworld: .ascii "Hello World!\n"`
    Using the .data pattern listed above, this data packet is structured the same. `helloworld:` is the tag. You can use whatever name you want for a tag. The only restriction is that you can't use any text that is already reserved by ARM (i.e. directives, commands like MOV, etc). Tags *are* case-sensitive, so `helloworld:` is a different tag than `HelloWorld:`. `.ascii` is the directive which states that the following data is of type ASCII (meaning it is human-readable text). And finally, `"Hello World!\n"` is the data being held here. You may wonder what the "\n" is for. That is the ASCII character for a newline. When printed in the terminal, it will create a new line (essentially what happens when you click "enter" while typing in a text program). This is mostly just used for formatting, but can have some other benefits you will learn later. Note that, while "\n" is composed of two actual characters ("\\" and "n"), ASCII/ARM read it as a single character. When counting how many characters are in a string, you should only count "\n" as a single character.





Note to Joe: Haven't finished this part yet. It will just be an explanation of the new Makefile once I get that set up, as well as a note on how ASCII works. The assignment will be compiling and running a file with the code above, but printing their name instead. I will not be explicitly reminding them to replace the value in R2 to get the length right.



# Conclusion


# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](TODO: Link here) to see the expectations the TAs have of your lab reports. Without further ado, here is your task:

## Task 1


