1
``` MOV R0, #12
    B tagname

    MOV R0, #16

end:
    MOV R0, #0
    MOV R7, #1
    SVC 0

tagname:
    ADD R1, R0, #30
    B end
```

2```
    MOV R0 , #some_number_here

beginning:
    CMP R0, #0
    BGT positive
    BLT negative
    BEQ end

positive:
    SUB R0, R0, #1
    B beginning

negative:
    ADD R0, R0, #1
    B beginning

ending:
    MOV R0, #0
    MOV R7, #1
    SVC 0
```

3```
    MOV R1, #10
    BL doubleR1
    ADD R1, R1, #2
    BL doubleR1
    BL doubleR1
    
end:
    MOV R0, #0
    MOV R7, #1
    SVC 0


doubleR1:
    MUL R1, R1, #2
    BX LR
```

4```
loophead:
    MOV R0, #0
    B loophead

ending:
    MOV R0, #0
    MOV R7, #1
    SVC 0
```

5```
    MOV R3, #0      @ This is your index
    MOV R4, #40     @ This is the total number of loops to do, called x in the previous passage

loophead:           @ Start the loop with a tag of any name, here I chose "loophead"

    @ Whatever code you want to repeat 40 times goes here

    CMP R3, R4      @ If you don't want to use a register to mark the total loops, you can remove R4 and just use CMP R3, #40
    BGE exit_loop   @ Exit the loop if R3 is >= R4
    ADD R3, R3, #1  @ Note that you don't actually need to put a condition on these two lines, since if the previous condition
    B loophead      @ is true, then the next two lines are skipped. A branch with a conditon has an implied NOT of the condition
                    @ for any lines following it.

exit_loop:
    MOV R0, #0
    MOV R7, #1
    SVC 0
```

6```
    MOV R0, #some_number_here

    CMP R0, #5
    BLT number_lessthan_five
    BGT number_morethan_five
    BEQ number_is_five          @ note that this line can just be "B number_is_five" becuase of the implied NOT mentioned above.
                                @ however, it is easier to read and debug if you just include the condition either way.

number_lessthan_five:
    @ do something here
    B other_code

number_morethan_five:
    @ do something else here
    B other_code

number_is_five:
    @ do something else else here
    B other_code

other_code:
    @ code for the rest of the program
```

7```
    MOV R0, #5
    CMP R0, #1
    BLT number_less_than

number_less_than:
    @ do something

number_more_than:
    @ do something else
```

8```
    MOV R0, #5
    CMP R0, #1
    BLT number_less_than

number_more_than:
    @ do something else

number_less_than:
    @ do something
```

9```
    MOV R0, #0              @ Command type
    LDR R1, =yourtaghere    @ Address to recieve to
    MOV R2, #numberofchars  @ Max input length
    MOV R7, #3              @ System call type
    SVC 0                   @ Execute command 
```

10```
    MOV R0, #1              @ Command type
    LDR R1, =yourtaghere    @ String to print
    MOV R2, #numberofchars  @ String length
    MOV R7, #4              @ System call type
    SVC 0                   @ Execute command 
```


