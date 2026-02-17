# Overview
Welcome to ECE 2170 Lab 2. Here, you will learn how to deal with complex exponentials in MATLAB. If you need a refesher or rexplanation of how complex exponentials work, let TA Cooper know. Once you have the fundamentals down, you will use your skills to solve a common problem of "multipath fading."

# The MATLAB Syntax
When writing code that uses complex exponentials in MATLAB, you can declare them using any of the following syntaxes:
- 1+j
- 1+1j
- exp(j\*pi)

However, you will find it most useful to use the exp() version in this lab.

MATLAB also has many built-in functions for working with complex numbers. Here is a list of functions and what they do:

`conj`: Returns the complex conjugate of the number (flips the sign of the imaginary part)
`abs`: Returns the magnitude of the complex number
`angle`: Returns the angle/phase of the number
`real`: Returns only the real part of the number (e.x. "2" in the complex number "2+9j")
`imag`: Returns only the imaginary part of the number (e.x. "9j" in the complex number "2+9j")

If you supply the above functions with a vector (array) of complex numbers, it will perform the operation on each number in the array.

Also, remember to try and use vectors instead of loops when working in MATLAB. To do so, you want to first generate a time series with `linspace`, then apply your function to the time vector. This will generate the result calculated for every time instance without needing to loop.

# Adding Sinusoids of the Same Frequency
Quick reminder on working with complex sinusoids. Any sinusoid can be represented as the real part of a complex sinuoid of the same frequency, with phase and amplitude dependent on the complex amplitude of the complex exponential. If you add multiple sinusoids of the same frequency, the resulting wave has the same frequency, but a different phase and amplitude as the originals. This new sinusoid is very hard to calculate using real sinusoids (e.x. cos(300pi)), but is very easy to calculate when using complex sinusoids, since you simply add the complex amplitudes of all the inputs.

If the sinusoids have different frequencies, you cannot directly reduce the result into a single real or complex term. The new signal will exist as a raw sum of the original signals with a total frequency as the fundamental frequency of the inputs.

# Functins in MATLAB
Functions in MATLAB work like they do in any other language. They can also return multiple values. Here is an example of a function declaration in MATLAB:
```
function [xx, tt] = goodCOS(ff,dur)
	tt = 0 : 1/(100*ff) : dur;
	xx = cos(2 * pi * ff * tt);
```
The function takes 2 parameters: `ff` for frequency and `dur` for duration. It then calculates a time series, `tt`, which is 100 samples per period for `dur` seconds. Finally, it calculates the cosine of each of those values and places it in a vector called `xx`. Note that, unlike other languages, you do not return values directly at the end of a function. In the function header, you declare the variables you want to return, in order, and those variables are automatically returned once the function ends (here, `xx` and `tt`).

# Conclusion
Here, you learned the basics of working with complex exponentials in MATLAB. Please let TA Cooper know if you have any questions or feedback on how to improve this lab for the future. All that's left is to finish the two tasks below and write your lab report. Soft deadline for this lab report is before the start of next weeks lab. Let me know if you need an extension.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](lab-guide) to see the expectations the TAs have of your lab reports.

## Task 1
Write a MATLAB function that adds all the input sinusoids and returns both the result and the time vector.

Additional Requirements:
The function must take the following as inputs: vector of frequencies, vector of complex amplitudes, number of samples per second, duration of time to sample, and the start time.
You should avoid using loops as much as possible, but you will need one for this task.

Assumptions:
You may use the following as a start for your code. Note that lines that begin with a `%` are comments, just explianing the inputs and outputs.
```
function [xx,tt] = syn_sin(fk, Xk, fs, dur, tstart)
%SYN_SIN Function to synthesize a sum of cosine waves
% usage:
% [xx,tt] = syn_sin(fk, Xk, fs, dur, tstart)
% fk = vector of frequencies
% (these could be negative or positive)
% Xk = vector of complex amplitudes: Amp*eˆ(j*phase)
% fs = the number of samples per second for the time axis
% dur = total time duration of the signal
% tstart = starting time (default is zero, if you make this input optional)
% xx = vector of sinusoidal values
% tt = vector of times, for the time axis
%
% Note: fk and Xk must be the same length.
% Xk(1) corresponds to frequency fk(1),
% Xk(2) corresponds to frequency fk(2), etc.
```

Expected Outputs:
You should show 2 examples of your function working. You can use any inputs with at least 3 sinusoids for your examples.


## Task 2
Multipath Fading
"In a mobile radio system (e.g., cell phones or AM radio), there is one type of degradation that is a common problem. This is the case of multipath fading caused by reflections of the radio waves which interfere destructively at some locations. Consider the scenario diagrammed in Fig. 1 where a vehicle traveling on the roadway receives signals from two sources: directly from the transmitter and reflections from another object such as a large building. This multipath problem can be modeled easily with sinusoids. The total received signal at the vehicle is the sum of two signals which are themselves delayed versions of the transmitted signal, s(t)."

[TODO: PHOTO1](PHOTO1)
Figure 1: Scenario for multipath in mobile radio. A vehicle traveling on the roadway (to the right) receives signals from two sources: the transmitter and a reflector located at (dxr, dyr). 

You can reframe the problem as follows:
	Imagine a car listening to the radio driving through a city. The radio wave can take multiple paths to get to the car: directly, or by reflecting off of a building. Each one of these paths takes a different amount of time to reach the car, and when the multiple signals arrive, they are combined (added) into one resulting wave. The two waves are exactly the same, just with a different phase between them. Your job is to find the specific spots on the road where the radio cuts out due to the original and reflected waves canceling out.

Include the following in your lab report:
1. The delay in seconds that each signal has can be calculated by the distance the signal travels divided by the speed of light. Write a MATLAB code that calculates the time delay each signal experiences, based off the diagram above. Make sure the code can take inputs for where the car is (dx, 0), where the transmitter is (0, dy), and where the reflector is (dxr, dyr).

2. Note that, when the signal bounces off the building (reflector), it gets a 180 degree phase shift. Explain how this affects the complex amplitude of the signal.

3. Write a function that takes the parameters `dx, dy, dxr, dyr` from part 1, as well as a frequency. The function should use your work from parts 1 and 2 to add the two delayed sinusoids, accounting for the phase flip of the reflected signal. You may be able to use your function from Task 1. The function should return only the amplitude (not complex amplitude) of the resulting signal.

4. Assuming that the transmitter is at (0, 1500) and the reflector is at (100, 900), find the amplitude of a 150 MHz signal at each meter the car travels from 0 to 300 meters.

5. Plot your data from part 4, where the x axis is the position of the car (0 to 300) and the y axis is the amplitude of the signal (between 0 and 2).

6. Explain what the plot signifies and any points of interest. At what positions will the radio be completely canceled out? 
