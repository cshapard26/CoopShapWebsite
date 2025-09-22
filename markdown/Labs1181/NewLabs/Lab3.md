Memory
# Overview
Welcome to Lab 3. Last lab, you learned about moving, adding, and shifting values in registers, as well as how to use the debugger to examine your program. Today, you will be looking at memory in the red pitaya and how to work with it.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](TODO: Link here).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP. This tab can also be used to anonymously submit suggestions, improvements, or complaints about the website. All of these will be reviewed and taken into consideration.

# What is Memory
As you should have seen before in lecture, memory is a dedicated spot in the microcontroller that stores information in larger quantities than can be stored in the registers. The memory on your pitaya is used to store both the programs that you are executing and the data that that program executes. There are different sections of memory reserved for different types of data, but you will see that more in lecture. The memory on your red pitaya is RAM, which is a type of volatile memory. This type of memory is erased when you unplug the pitaya. Your pitaya also has storage (what the microSD card is for), which is a type of nonvolatile memory that is slower, but can hold larger amounts of information.

Generally speaking, the more data a type of memory can hold, the slower it is. The registers on your pitaya can only hold around 100 bytes of data at a time, but are extremely fast and can be acted upon in a single cycle. Memory/RAM on your pitaya can hold around 512 KB of data, and is still fast, but not super fast, needing 3 cycles to act on (get address, access address, act). Finally, storage on your pitaya holds around 32 GB of data, but is very slow and is not supposed to be acted on.

Note that the program that you write is placed in storage so that is persists even after unplugging your pitaya. However, when you run the program, the whole thing is loaded into memory, which is where it is actually acted on. You do not run code from storage, even if it is stored there.

All memory has an address (just like a street address) that tells you where a specific byte is located. These addresses are often written in hex (e.x. 0x200C0 or 0xAB4C). To load or store data in memory, you first need to specify the address that the data should be stored at or loaded from.

# Data Sizes
A quick note on data sizes. When talking about data, a "word" means a 32-bit or 4-byte block of data. A "halfword" means a 16-bit or 2-byte block of data. A "byte" means an 8-bit or 1-byte block of data. This will be useful later.

# Getting a Memory Address
Now that you know what a memory address is, we should look at how to get one. You shouldn't have to type the actual numbers (0x200AC, etc) when accessing memory, as that would be a pain. Luckily, ARM has a way around this that you have already seen: tags.

When you create a tag in your program (e.x. "_start:" or "helloworld:"), that tag is actually a pseudonym for the address where the data it marks is stored in memory. For example, in Lab 1, you printed out a message that said "Hello YOURNAME!", and this was marked with the tag "helloworld:". If you wanted to access the data at that tag/address, you need a special command:

Instruction: `LDR`
Usage: `LDR destination, =tag`
Description: Loads ("LoaD into Register") the address named by the tag into the destination register.
Example:
```arm
.global _start
_start:
      
      @ Look at the .data section at the bottom for addresses and data
      
      LDR R0, =hellothere     @ This loads the address of the tag "hellothere:" into register 0
                        @ R0 now contains the value 0x20000. It does not contain the value "G"
                        @ However, the value "G" is stored *at* the address 0x20000

      LDR R1, =perry          @ This loads the address of the tag "perry:" into register 0
                        @ R0 now contains the value 0x200BC. It does not contain the value "t"

      MOV R0, #0
      MOV R7, #1
      SVC 0

.data
hellothere:       .ascii "General Kenobi"       @ Pretend this starts at the address 0x20000
perry:            .ascii "the platypus"         @ Pretend this starts at the address 0x200BC
anothertag: .word 0x12345678        @ Pretend this starts at the address 0x20108
onemore:    .byte 0x12345678
      
```

Note that this is actually a secondary use of the LDR command, which you will see in the next section of this lab. What it is doing here is actually creating a "literal pool," the topic of our next lab. For now, just know that you can get a memory address of a tag using `LDR reg, =tag`.


# LDR
You've seen how to get the address of a section in memory. But this is useless on it's own. You don't want to know where "perry:" is. You want to know the "the platypus." Similarly to how we got the memory address, we can use the LDR command to get the value AT the memory address. This is the primary usage of the LDR instruction.


Instruction: `LDR`
Usage: `LDRx destination, [address]`
Description: Loads ("LoaD into Register") a value from the specified memory address into the destination register. Here, the "x" specifies the size of the data to be loaded, where replacing "x" with "B" loads a byte, "H" loads a halfword, and removing the "x" loads a full word. "LDRx" is not a valid command, and you need to replace the x to make a working instruction.

Example:
```arm
.global _start
_start:
      
      @ Look at the .data section at the bottom for addresses and data
      
      LDR R0, =hellothere     @ This loads the address of the tag "hellothere:" (0x20000) into register 0
      LDRB R1, [R0]           @ This goes to the address held in R0 (0x20000) and places one byte of that data
                        @ into register 1. R1 now contains "0x47", which is the ASCII value for "G"

      ADD R0, R0, #0x1  @ Adds 1 to the memory address
      LDRB R2, [R0]           @ Loads one byte from the address in R0 (0x20001) into R2
                        @ This is "0x65", the ASCII value of "e" (the second letter of "General")

      LDR R0, =perry          @ Overwrites R0 with the address of "perry" (0x200BC)
      LDRB R0, [R0]           @ Replaces the contents of R0 with one byte stored at the address in R0,
                        @ which is "0x74" or the ASCII value for "t". R0 now contains "0x74", and the address
                        @ that R0 had in it before was overwritten. This is a quick way to get the value at an address
                        @ without using up too many of your registers

      LDR R5, =anothertag
      LDR R3, [R5]            @ R3 now contains one WORD of data from the address held in 5 (0x20108)
                        @ R3 now contains the value 0x12345678

      LDR R6, =perry
      LDRH R4, [R6]           @ R4 now contains one WORD of data from the address held in R6 (0x200BC)
                        @ R4 now contains the value "0x6874", or the ASCII values for "ht"
                        @ Why is it backwards? Keep reading.

      MOV R0, #0
      MOV R7, #1
      SVC 0

.data
hellothere:       .ascii "General Kenobi"       @ Pretend this starts at the address 0x20000
perry:            .ascii "the platypus"         @ Pretend this starts at the address 0x200BC
anothertag: .word 0x12345678        @ Pretend this starts at the address 0x20108
      
```

A few things to note:
1. You cannot skip steps and do something like `LDR R2, [=anothertag]`. Why? The ARM philosophy says we can only do one thing at a time.
2. As in the second example, you can add or subtract from the address in a register to get new addresses. This is useful for getting one character at a time from a string of text
3. You may have noticed that when loading a halfword of ascii text, the letters were reversed ("ht" instead of "th" like it was written). That is because ARM is a little endian system.

# Endianness
You should have heard about this in lecture, but here is a recap: Big Endian means that the most significant bit (MSB) comes first when loading or storing data. Little Endian means that the least significant bit (LSB) comes first when loading or storing data.

Generally, you write numbers with the MSB first. 0x100 is a large number, and 0x001 is a small number. However, in little endian systems, the LSB comes first (when in memory). This can seem counterintuitive, so why do it? ARM is built for efficiency.

Think about it this way. You have a stack of 100 paper plates. You want to move the plates from one cabinet to another. What do you do? like a sane person, you will pick up the entire stack of plates and move it to the new cabinet. The order of the plates is the same, even when moved to a new location. This is like a Big Endian system. But data is not a paper plate. It is not super light and easy to move.

Now assume you have a stack of 100 lead plates. You know, the ones that give you lead poisoning when you eat acidic food on them? Pretend that each plate weighs 20 pounds. If you wanted to move all the plates from one cabinet to another, you wouldn't pick up the entire stack and move it. You would take one plate from the top of the pile, move it to the new cabinet, and then repeat for all the plates. Now, the order in the plates in the new cabinet will be reversed from that of the original cabinet. This is like a Little Endian system.

One important thing to note is that you will only be moving data between registers and memory. If you have data in a register, it flips when it goes into memory, then it flips again when you take it out of memory. In that way, when you are working with data, you generally don't have to worry about endianness, as it sorts itself out as you use it. Where it becomes important is with data sizes.

Little endian takes effect on a single chunk of data at a time. These chunks range between bytes and words. If you store data as a byte, it performs no flip, since a byte is the smallest unit of data in memory (you can't reverse the order of one object). If you store it as a halfword, it flips the two bytes, and if you store it as a word, it flips all four bytes. This means that, when you are loading and storing data in memory, you need to be consistent with the data size. If you store a piece of data as a word, then try to load it as a halfword, it will jumble up the data. ASCII characters are only meant to be loaded or stored a single byte at a time. That is why the "th" was reversed when it was loaded as a halfword in the previous example.

# Signed vs Unsigned
One additional argument that the `LDR` instruction takes is whether a number is signed or unsigned (integer or whole number). This is not very important and you likely won't have to apply it in this class. It is mostly used to set Condition Codes, which you will learn about in our next lab session. LDR commands are unsigned by default, and you can make them signed by adding the letter `S` after it. E.x. `LDRS` for a signed word, `LDRSB` for a signed byte, and `LDRSH` for a signed halfword. Again, you won't need to use this, but it's good to know in case you see it in code given to you.

# STR
You read about loading data from memory and the effects of endianness, so now it's time to learn about storing data into memory.

Instruction: `STR`
Usage: `STRx number, [destination]`
Description: Stores ("StoRe into Register") a the given number/data into the address "destination". Here, the "x" specifies the size of the data to be stored, where replacing "x" with "B" stores a byte, "H" stores a halfword, and removing the "x" stores a full word. "STRx" is not a valid command, and you need to replace the x to make a working instruction.
Example:
```arm
      LDR R2, =emptyarea
      MOV R5, #0x6C
      STRB R5, [R2]           @ Stores a byte from the value in R5 (0x6C) into the memory address in R2
                        @ No changes occured to any of the registers, but now the data at "emptyarea"
                        @ is 0x6C000000 instead of 0x00000000
      
      ADD R4, R2, #2
      MOV R5, #0xA7F3         
      STRH R5, [R4]           @ Stores a halfword from the value in R5 (0xA7F3) into the memory address in R4
                        @ which is 2 addresses after "emptyarea". No registers changed, and the data in
                        @ "emptyarea" is now 0x6C00F3A7 (remember little endian)
      
      LDR R0, [R2]            @ Loads a word from the address in R2 (still "emptyarea") into register 0
                        @ R0 now contains 0xA7F3006C

.data
emptyarea:  .word 0x00000000

```

Important Note: `STR` is one of the few commands that don't follow the pattern of starting with the destination. Remember that the destination is the memory address. It is the exact opposite of an `LDR`.

The example code given also shows what happens when you mix up your data sizes (stored a byte and a halfword, loaded a word, now the data is mixed up).

# Indexing
Indexing is a bit of an annoying topic, but it is important. In ARM, you often are working with data larger than a byte or a word. Take the strings above, for example. "the platypus" is 12 characters long, so 12 bytes or 3 words. However, the tag "perry:" only reveals the address of the first byte. How do we access the next bytes? In the previous examples, I manually added a byte or two to the address using an ADD command. However, this is inefficient and doesn't always give us the behavior that we want. Since viewing a range of addresses is so common, ARM gives us options to do so automatically upon loading or storing. This is called Indexing.

There are 3 types of indexing in ARM: preindexing, postindexing, and autoindexing. When loading or storing, the address you are working with will *always* be in a register. However, in some indexing types, the address you are loading or storing to is offset from the actual address in the register. This offset address is called the "effective address" and it may be the same or different than the address stored in the register.

## Preindexing
Preindexing means that when loading or storing to an address, you specify an offset, and the data is stored to the new effective address. The address in the register is not updated. It looks like this:
```arm
      LDR R0, =somebody
      LDRB R1, [R0, #3] @ This is preindexing notation. It gets one byte from the address "somebody" PLUS
                        @ the value 3. This is three bytes after the original one, so it gets the value "e".
                        @ The value in R0 is not changed.

      LDRB R1, [R0, #8] @ Preindexing to get the character 8 bytes after the first one, which is a "d". R0 is
                        @ not changed

      LDRB R1, [R0, #0] @ Gets the character from the original address plus 0 bytes, which is still the first
                        @ character, "o". Note that this is equivalent to "LDRB R1, [R0]". R0 is not updated
      
.data
somebody: .ascii "once told me"
```

Preindexing is useful for getting a byte at a specific, unnamed location without changing the state of any of your registers.

## Postindexing
Postindexing means that when loading or storing to an address, you do not specify an offset, and the data is stored at the original address (which is the same as the effective address. However, you do specify a number, which is how much to change the original address stored in your register after the command is executed. This is better explained with an example:
```arm
      LDR R0, =somebody
      LDRB R1, [R0], #2 @ This is postindexing notation. It gets one byte from the address "somebody" without
                        @ any offset. This is the first letter "o". Next, the value 2 is added to R0 and stored
                        @ back into R0. If "somebody" has the address 0x20000, the R0 originally held 0x20000 but now
                        @ holds 0x20002.

      LDRB R1, [R0], #2 @ This is the same command. However, since R0 was updated in the previous command, we are now
                        @ getting the value at 0x20002, which is the "c". After we get that value, 2 is added to R0
                        @ and stored back in R0. Thus, R0 now holds 0x20004

      LDRH R2, [R0], #-3      @ This gets two characters (reversed because of little endian) from the address in R0,
                        @ which is still 0x20004. R2 now holds ascii for "t ". R0 is now updated to 0x20001

      LDR R0, =somebody @ Note that you can reset the address in R0 back to 0x20000 (a.k.a "somebody") at any point
                        @ with this command.

      
.data
somebody: .ascii "once told me"
```

As you may have noticed, you can also use negative numbers as indexes. This works for all types of indexing. Post indexing is useful for code that is repeated or getting a large set of data that is evenly spaced (like one byte characters in a string).

## Autoindexing
Autoindexing is just preindexing and postindexing combined. If you want to get data at an offset, then change the value of the stored address, you can do both at the same time. This is like saying `LDRB R6, [R7, #4], #2`. HOWEVER, due to limitations in ARM, the offset and the address update MUST be the same value. That means the previous example cannot exist, but `LDRB R6, [R7, #4], #4` is allowed. Because the two numbers are the same, ARM simplifies the command to be `LDRB R6, [R7, #4]!` with the `!` at the end. This is the syntax for autoindexing, as seen in the example below:
```arm
      LDR R3, =RoadWordAhead
      LDRB R8, [R3, #6]!      @ This is autoindexing notation. It gets one byte from the address "RoadWorkAhead" in R3 PLUS
                        @ the value 6. Assuming that "RoadWorkAhead" is at 0x14C00, the effective address is
                        @ 0x14C06, which puts the ascii "I" into R8. Next, R3 is updated to be the old effective
                        @ address, 0x14C06. R8 now holds "I" and R3 now holds 0x14C06

      LDRB R9, [R3, #4]!      @ Another autoindex, but with a 4. Since R3 is still 0x14C06, this will get the character at
                        @ 0x14C06 PLUS 4, which is 0x14C0A, and put that character into R9. R9 holds "r", and R3 is     
                        @ updated to the old effective address, 0x14C0A


.data
RoadWorkAhead: .ascii "Yeah, I sure hope it does."
```

As you can see, autoindexing combines both pre and post indexing into one command. It is most useful for jumping around memory without knowing where you are going in advance.

## Final Notes on Indexing
Though most of the examples above showed large numbers as offsets and address additions, you will almost always be using either "1" to move to the next byte or "4" to move to the next word. When working with text, you will mostly be using postindexing with an update of 1. Get a character, move to the next one, repeat. All in one command.

Also, though all the examples I gave used `LDR`, all of these topics apply exactly the same with `STR` commands.

Since indexing has historically been a tough topic for students, I have made this little animation to show you the different indexing types in action.

TODO: Add gif

# Memory and GDB
Remember your old friend GDB? As the debugger's best friend, you get to learn another command to interact with it. You used the command `i r` to view the contents of registers. Now you get the command to view the memory at a specified address:

`x /4ubfx ADDRESS`: This displays four bytes in memory starting at ADDRESS (which is replaced with the memory address you want to see). This command can be modified a bit to display different information, but I find this the cleanest way. If you are interested in other ways to display memory check out TODO:page_number in the Smith book.

Remember that gdb commands can only be run when in the debugger. Check last lab for reminders on that. Also, you may not know what memory address you need. The best way to find this address is to first do `i r` to check your registers, then find the memory address that you put in one of the registers (in the command `LDR R3, =idunno`, this would be R3). You can add or subtract from that value to view a different window of memory.


# Conclusion
This lab went over Loading, Storing, and indexing types. This lab was focused less on reading and more on giving you descriptions and examples of how to use the tools. I encourage you to play around with these a bit before tackling the assignment portion below. Create a new file, add some wrapper code, LDRs and STRs with Indexing and Datasizes, and then compile the file. Run the file with the debugger and step through it, checking memory occasionally to see how your commands are affecting the pitaya's memory. The assignments below are challenging and focused on using the commands and tools you used in fun new ways, so becoming comfortable with the toolset you have is the best way to approach these.

It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](TODO: Link here) to see the expectations the TAs have of your lab reports.

You should perform all these tasks in a new, blank directory on your red pitaya. Feel free to reference previous labs or the [Cheat Sheet](#TODO: add link) to refresh on old topics. All tasks should only include ARM instructions you have learned up to this point. Working ahead is fine, but you need to keep the tasks in the scope of the lessons. For questions on this (if something applies, etc), ask a TA.

## PICK TWO
There are three tasks listed for you below. You can pick any two tasks to attempt for this lab. The unchosen one is available for you to practice or review, but is not required. Submitting all three tasks will not grant you extra credit.

However, the TAs will still make comments and give feedback on all three tasks, if submitted. If you want to submit a third task for feedback, but do NOT want it to be considered for grading, you must mark it clearly in your lab report with the phrase "DO NOT SCORE." If no task is marked with this phrase, the TAs will roll a random number generator to decide which two tasks to score for your lab grade.

Additionally, if you come up with a task that you think is of comparable challenge to the ones listed, you may pitch it to one of the TAs. If accepted, your task (bound by the requirements agreed upon by you and the TA) will count towards one of the PICK TWO tasks. The other tasks may be submitted for feedback following the same protocol listed in the paragraphs above.

## Task 1
Write a program that takes a number stored in memory and adds your student ID to it, then puts it back in the same place.

Additional Requirements:
- The number you add to your student ID must be a word in length (4 bytes).
- You must show the results by inspecting memory in the debugger.

Assumptions:
- Your student ID will be in hex. That means if your student ID is 12345678, the value should be 0x12345678.
- Your SMUID is 8 hex digits (32 bits), which is within the 32-bit limit for registers.
- Both your student ID and the 4 byte number will be hardcoded/manually stored in the `.data` section of your code before the program runs. Remember that you can specify that some data in memory is a word with the directive `.word` (instead of `.ascii`, for example).
- The sum of the two numbers should be stored in the same memory location as your chosen 4-byte number.

Expected Outputs:
- Displaying memory in GDB should show the value of your student ID plus another number (with word-length addition, not byte-by-byte). Note that the value will be displayed in reverse due to little endianness. The same screenshot should also show your student ID and your 4-byte number in your registers somewhere. E.x.
TODO: Photo here

## Task 2
Write a program that demonstrates how data is altered if data sizes are inconsistent. Explain what is happening in your lab report.

Additional Requirements:
- You must show examples by inspecting memory in the debugger.
- Your program must include at least one mistake in the data and an explanation of what went wrong and how to fix it.
- Your report must mention how endianness affects the results.

Assumptions:
- You can place any type of data (numbers, ascii/text, etc.) in the `.data` section of your code to use in your program.
- You can use as many or few examples and explanations as needed to fully convey your point.

Expected Outputs:
- A demonstration and explanation of the requirements above.

## Task 3
Write a program that fills the first 8 registers (R0-R7) with 16 bytes of data stored in memory, 2-bytes per register, in order.

Additional Requirements:
- You must show the result by inspecting registers in the debugger.
- The 16 bytes of data you use must be `0x00112233445566778899AABBCCDDEEFF`. After your program executes, R0 will contain `0x0011`, R1 will contain `0x2233`, and so on.
- You must use at least one type of indexing.

Assumptions:
- You can place the given 16-bytes in the `.data` section of your code to use in your program.
- You can use whatever directive you would like to define the data in the `.data` section (.word, .ascii, .byte, etc)

Expected Outputs:
- Displaying the registers in GDB should show the value of 0x0011 in R0, 0x2233 in R1, and so on up to 0xEEFF in R7. E.x.
TODO: Photo here
