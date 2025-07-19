
[[Microcontrollers Lab 0]]: Leaning the Tools

Learn Linux commands, navigating the terminal, and editing files

      Connecting to the Pitaya
      
      How this lab is going to structure things
      
      Basic Linux commands
      
      File Systems
      
      Editing files
      
      Commands: ssh, ls, cd, mkdir, cat, cp, rm, make (gdb/nano launch apps, so don't count towards the 8)
      
      Project: make a new directory on your red pitaya with your first name, make a directory inside of that with your last name, then make a file in that called smuid.txt with your smuid in it. Clear your terminal, then show your chain of commands to go down the directories one by one, listing the files in each one, and then catting the file with your text in it before going back up the chain of directories. Only one screenshot needed.
      

[[Microcontrollers Lab 1]]: Intro to ARM

See ARM code for the first time, go line by line in explanation, and make some light modifications. Add building and makefiles. Learn the ARM philosophy.

      The ARM philosophy: Few commands, each do one thing at a time. Make a program with the smallest possible units
      
      What ARM code looks like
      
      Explanation of what each line does
      
      Compiling with a makefile (no build file because why the heck were we doing that?)
      
      What compiling means, and why ARM is literally coding in binary
      
      Running the code
      
      A note on how ASCII works
      
      Project: Replace code in the given file to print "Hello, Firstname Lastname!" Show the process of compiling the file, running it, and viewing the output. Output should be formatted correctly.
      

[[Microcontrollers Lab 2]]: GDB, Moving, and Adding

Learn how to move and add numbers in ARM. Go over Shifting. Learn how to interface the debugger. Write a basic calculator program. Learn about the Wrapper Code.

      MOV and ADD instructions
      
      Binary
      
      Shifting and Rotating
      
      Wrapper Code
      
      GDB
      
      Project: PICK 2 (all these are hard coded, no terminal input, show result in gdb)
            1. Write a program that creates a large number/student id (MOV only has 1 byte. Need to move, shift, add, move, shift, add)
            2. Write a program that rotates a number by a variable amount (from another register)
            3. Write a program that adds 2 numbers and only saves the last 4 bits (done by LSL 28, then LSR 28. Chops the top part right off)
      
[[Microcontrollers Lab 3]]: Memory

Learn the intricacies of memory, data size, and indexing. Write code that shows the difference between indexing types, but more open-ended compared to the current version.

      LDR and STR instructions
      
      Data size (word, halfword, byte)
      
      Signed vs Unsigned
      
      Endianness
      
      Pre- Post- and Auto indexing
      
      Accessing memory with GDB
      
      Project: PICK 2 (all these are hard coded, no terminal input, show result in gdb)
            1. Show and explain what happens if your LDR and STR indexing types don't align
            2. Show and explain how data sizes affect the way endianness stores numbers (STRH 0x1234 vs STR 0x12, STR 0x34)
            3. Write a program that takes a number stored in memory and adds your student ID to it, then puts it back


[[Microcontrollers Lab 4]]: CPSR and Literal Pools

Learn the CPSR flags and how literal pools work. Write code that sets all CPSR flags. See how literal pools are handled by ARM (it is just more memory).
 
[[Microcontrollers Lab 5]]: Conditional Execution

Learn how conditional execution takes place and play around with it. Write a program that takes a letter as input from the terminal and outputs "x is before 'm'" or "x is after 'm'" depending on the letter. Write a program that uppercases or lowercases a letter inputted from the terminal.
 
[[Microcontrollers Lab 6]]: Branching

Learn how branching works in code and how to use it for both conditional execution and loops. Create a 4 function terminal calculator (limitations: answer must be positive and 1 decimal digit. Mult/Div should only be by factors of 2^n). Write a program that loops through the Lab 5 code for multiple characters.
 
[[Microcontrollers Lab 7]]: Subroutines and the Stack

Learn how linking works and how to use it in code. Write a program that uses branching and linking to make set characters uppercase. Learn stack protocols and write code that gets around an issue of all 12 registers being used and important before going into a subroutine. 
 
[[Microcontrollers Lab 8]]: GPIO and Macros

Learn what macros are and how to interface the GPIO pins on the red pitaya. Explain the difference between subroutines and macros (memory vs speed). Write a program that turns on the leds in binary order. However, this time they have to use a macro to check which LEDs to turn on. No brute force (but not as intensive as the final project version).
 
[[Microcontrollers Project]]

	Same as before

Other additions:
- How to write a lab report
- Break programming questions into: task, requirements, assumptions, and expected outputs.
- Linux, ARM, GDB, and Nano quick reference sheet
- After labs are done, release my solution to each program so they can see different ways to go about it
- A makefile that only needs 1 variable change
- Flow chart for a typical programming workflow with ARM
- If I finish everything else and still have an itch to expand: write ARM code for more breadboard peripherals. Abstractions for motors, servos, speakers, etc and more general things like PWM, reading input, analog input, I2C/SPI, etc.
