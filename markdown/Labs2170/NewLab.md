# Overview
Welcome to your shiny new revised lab for ECE2170. Here, you will learn everything you need to know to make and test passive filters. These are real-world skills you will see in the industry and may show up in technical interviews for internships.

# Passive Filtering
Passive filtering is creating a filter using only "passive" components (resistors, capacitors, and inductors). These are almost exclusively used for low-pass, high-pass, band-pass, and band-stop filters. You should know what each of these do from lecture. What's great about passive filtering is that it *requires no extra power*. Passive components don't need powering, so pushing a signal through them is a very energy efficient way to filter out unwanted signals.

The negatives of passive filtering is that they are not very strong. The cutoff for a passive filter has a very long slope compared to what you would like to see in an ideal filter. Take these images of an ideal low-pass filter and what a passive low-pass filter achieves:

Image 1

Image 2

What is the slope of a passive filter's cutoff? -20 dB/decade. That's you magic number. This means that every decade (1 Hz, 10 Hz, 100 Hz, 1000 Hz ...) of the frequency after the filter starts to take effect, the output of the filter drops by 20 dB. 

How do we identify the point where the filter officially "cut's off?" In the ideal image above, it is very easy to say that the filter allows all frequencies to the left of the vertical line to pass and removes all frequencies to the right. What about the passive filter? At what frequency is it "allowing" the signal to go through vs stoppin it? -3 dB. That's your magic number. This is the cutoff frequency of any -pass filter, where the output hits -3dB. -3dB is where the output is half the amplitude of the input, so it is also called the "halfway point."

# Multi-stage Filtering
Above, we were just talking about single stage passive filters. But there are multi stage filters as well. If you chain together multiple passive filters in a row, you will get the sum of all the filters as the output. So if you put a low-pass filter in the same line as a high-pass filter, the output will look like a band-pass filter with the low cutoff frequency as the high-pass filter's output and the high cutoff frequency as the low-pass filter's frequency. This is how you make more complex filters.

What if you put two of the same low-pass filters in a row? You get double the effect. So instead of -20 dB/decade of cutoff, you get -40 dB/decade. This is a steeper slope and looks closer to the ideal filter output in the image above. You can chain as many passive filters together as needed to get the cutoff that you want. But often, a single stage is all you need. This is often called the "order" of the filter. A first-order filter is just one passive filter, a second order is two chained filters, a third order is three, and so on.

# How to Design Passive Filters
Here is where the actual work comes in. 

## Voltage Dividers
First, here is a review of Voltage Dividers, which you should have seen in Circuit Theory (but most people don't remember them or don't know how to apply them). A voltage divider works by configuring two resistors in the configuration below:

Image 3

If you apply a voltage in the top resistor and ground the second one, the voltage in between the two will be this equation:

Image 4

Quick test: if the top resistor is 10kOhms, what resistor would you need on the bottom resistor for the output to be 1/3 the input voltage? Try it now.

5kOhms. You should be able to estimate that number almost immediately without any calculations by hand. Ask Cooper for an anecdote if you want to know why and tips to do it faster.

## Resistors
More importantly in the problem above, we have another issue: 5kOhms resistors don't exist. They don't make them. That's not a value that is manufactured for resistors. They make 4.7k resistors and 5.1k resistors, but not 5k. Why? If a manufacturer made every value of resistor between 0 and 1M, then they would go out of business. There is too many types to make and not enough demand for a 6.1k resistor or a 9.35k resistor to sell them. What values are made? E series, most often E12 or E24. Look up E24 resistors to see the most standard values of resistors you will work with.

So, if they don't make 5k resistors, what resistor do you use in the voltage divider? Think about it for like 30 seconds before moving on.

A novice ECE will say "I would put multiple resistors in series and parallel to get an equivalent resistance of 5kOhms." This is likely what you were thinking. A professional ECE will say "5.1k is pretty close, let's go with that." 

The big thing here is that you don't often need exact numbers. Engineering is the process of working with restrictions and choosing which battles to fight. Real resistors don't come with exactly 5.1kOhms. They are sold as 5.1k +-5% (different E series also have different tolerances). So, I could use a resistor labeled as 5.1k, but it is actually 5.35k or 4.85k. You can't control the exact value you will get, because small physical differences in each resistor causes slightly different resistances. Engineering is working with those and dealing with them. The good news is that, because all of the components you use have these random values within the 5% tolerance, they all kinda cancel out. In the end, you get something pretty close to what you want.

Also, in a voltage divider, I gave you one of the values. What do you do if you have to pick both? You just kinda, choose an arbitrary starting value (often between 1k and 10k) and then try to find an appropriate E24 resistor to get the division you want. You may pick higher or lower values depending on your use case (low values are more power hungry but have less noise, and high values are very power efficient but have a lot of noise), but in general, 1k-10k is a good middle-value and will cover 95% of your cases.

## Capacitors
You may remember from Circuit Theory that "capacitors behave as an open circuit in DC circuits." This is true, but not the interesting part. The best thing about capacitors is that their impedance/resistance *is dependent on frequency.* At DC, capacitors have infinite resistance. At 10 Hz, capacitors have a very high resistance. At 100 MHZ, capacitors have very low reisistance. This is a very, very useful property.

The exact resistance/impedance that a capacitor has at a given frequency also depends on its value (capacitance). You can calculate it's resistance at a frequency using this formula:

Image 5

One other thing to note is that capacitors also follow the same E series as resistors. So 6.8nF capacitors exist in E24, but not 7nF, etc.

## Putting it Together
Now, given what you have learned about capacitors and voltage dividers, here is your first assignment. Design me a low-pass filter. The filter should divide the output frequency in half (the -3dB point) when the frequency is at 1kHz and approach 0 as the frequency rises. Test your design with a few numbers to make sure it works. Once you have a design, show it to Cooper for approval before moving onto the next step.

The next step is to do the same, but with a high-pass filter. The cutoff frequency should be 15kHz this time. Again, show Cooper for approval before moving on.

Now, make a band-pass and a band-stop filter. Do not find any values for these, just show the structure that it would be and once again, check wit Cooper to make sure it is right.

# Implementation/Assignment
You have your design. Now it is time for the fun part: physically making it and testing it's functionality. Cooper has some components for you, and you should build your design on a breadboard. If you do not know how to use a breadboard, ask Cooper. The design you should build is a Band Pass filter that has cutoffs at 150Hz and 700Hz. Once you design and build your filter, bring it to Cooper to test. 

# Conclusion
In this lab, you learned the actual real-world skill of designing a filter for use in a system, the standard resistor values, estimation process, and testing an implementation of a design. All of these skills are things you will actually use in the field and may be asked to go over in techincal interviews for positions. If you have any questions about this lab, ECE in general, or honestly just anything, feel free to reach out. Thanks for joining me this semester, and good luck.