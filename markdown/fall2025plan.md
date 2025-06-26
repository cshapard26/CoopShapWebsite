
[[Microcontrollers Lab 0]]: Leaning the Tools
	Learn Linux commands, navigating the terminal, and editing files
[[Microcontrollers Lab 1]]: Intro to ARM
	See ARM code for the first time, go line by line in explanation, and make some light modifications. Add building and makefiles. Learn the ARM philosophy.
[[Microcontrollers Lab 2]]: GDB, Moving, and Adding
	Learn how to move and add numbers in ARM. Go over Shifting and LDR vs MOV for large numbers. Learn how to interface the debugger. Write a basic calculator program. Learn about the Wrapper Code.
[[Microcontrollers Lab 3]]: CPSR, Intro to Memory
	Learn the CPSR flags and see LDR and STR in action. Write code that sets all CPSR flags.
[[Microcontrollers Lab 4]]: Memory and Literal Pools
	Learn the intricacies of memory, data size, and indexing. See how literal pools are handled by ARM (it is just more memory). Write code that shows the difference between indexing types, but more open-ended compared to the current version.
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
