0
| Name | Abbreviation | Example | Why you should choose it |
|:----:|:------------:|:--------|:-------------------------|
|Increment Before/<br>Full Ascending|IB|0x200b0: Data1<br>0x200b4: Data2<br>0x200b8: Data3<br>0x200bc: Data4 <-- SP|Counts upwards and always<br> points to the last used data.<br> Best if you like to logically keep<br> track of where everything is.|
|Increment After/<br>Empty Ascending|IA|0x200b0: Data1<br>0x200b4: Data2<br>0x200b8: Data3<br>0x200bc: Empty <-- SP|Counts upwards, but conceptually<br> starts at 0 instead of 1.<br> Best if you have lots of <br> programming experience.|
|Decrement Before/<br>Full Descending|DB|0x200b0: Data4 <-- SP<br>0x200b4: Data3<br>0x200b8: Data1<br>0x200bc: Data1|Counts downwards and always<br> points to the last used data.<br> Best for people who like<br> to visualize the stack<br> like a stack of papers.|
|Decrement After/<br>Empty Descending|DA|0x200b0: Empty <-- SP<br>0x200b4: Data3<br>0x200b8: Data1<br>0x200bc: Data1|Counts downwards and always<br> points to the next avaliable spot.<br> Best for people who don't like<br> any of the other options and<br>just wants to choose one and<br>move on.|

1
```
    MOV R0, #12
    MOV R1, #42
    MOV R2, #69

    STMIB SP!, {R0-R2}  @ At this point, the stack looks like this (assume it starts at 0x200a0):
                        @ 0x200a4: 12
                        @ 0x200a8: 42
                        @ 0x200ac: 69
                        @ 0x200b0: empty
                        @ and the SP value is 0x200ac

    @ ALTERNATIVELY (if the previous line wasn't used)
    STMDA SP!, {R0-R2} @ At this point, the stack looks like this (assume it starts at 0x200a0):
                        @ 0x20094: empty
                        @ 0x20098: 12
                        @ 0x2009b: 42
                        @ 0x200a0: 69
                        @ and the SP value is 0x20094
```

2
```
    MOV R0, #12
    MOV R1, #42
    MOV R2, #69
    STMIB SP!, {R0-R2}  @ At this point, the stack looks like this (assume it starts at 0x200a0):
                        @ 0x200a4: 12
                        @ 0x200a8: 42
                        @ 0x200ac: 69
                        @ 0x200b0: empty
                        @ and the SP value is 0x200ac

    MOV R0, #0
    MOV R1, #0
    MOV R2, #0          @ Now all registers are 0

    LDMDA SP!, {R2-R4}  @ At this point, the stack is completely empty (we popped all three values)
                        @ R2 now holds #12
                        @ R3 now holds #42
                        @ R4 now holds #69
                        @ The SP value is back to 0x200a0
```



3
```
    MOV R0, #10
    MOV R1, #20
    STMDB SP!, {R0, R1}
    LDMIA SP!, {R1, R0} @ Here, the values in R0 and R1 were replaced in opposite order
                        @ R0 now holds #20
                        @ R1 now holds #10

    @ You can do this on a much larger scale, shifting all 12 registers around at the same time
```

4
```
.global _start
_start:
    MOV R0, #69
    MOV R1, #42
    MOV R2, #1337       @ These three are very important numbers
                        @ We don't want them overwritten

    STMIA SP!, {R0-R2}  @ To make a checkpoint, we add these three to the stack
    BL print            @ Now we go to the "print" tag

                        @ Upon returning, R0, R1, and R2 have all been overwritten
                        @ But those original values are still on the stack
    LDMDB SP!, {R0-R2}  @ So we restore from the checkpoint

    B exit              @ End the program


print:
    MOV R0, #0
    MOV R1, =text_to_print  @ Putting standard print data in the registers
    
    STMIA SP!, {R0, R1, LR} @ Saving that data so it isn't overwritten, 
                            @ as well as the LR that goes back to _start
    BL calculate_length     @ Go to the calculate_length tag

    LDMDB SP!, {R2}         @ We have returned from calculate_length
                            @ This line gets the length from the stack (which
                            @ we put on the stack from R8 in the last function)  
    LDMDB SP!, {R0, R1, LR} @ Restores R0, R1, and the LR to _start

    MOV R7, #4              
    SVC 0                   @ more standard print data and execute

    BX LR                   @ Jump back to the branch in _start 


calculate_length:
    @ performs an operation that calculates the length of the string
    @ Assume the answer is in R8 here
    STMIA SP!, {R8}         @ Puts the answer on the stack to pass it along
    BX LR                   @ Return to the LR (in "print")


exit:
    MOV R0, #0
    MOV R7, #1
    SVC 0

.data
text_to_print: .ascii "Hello World!\n"

```