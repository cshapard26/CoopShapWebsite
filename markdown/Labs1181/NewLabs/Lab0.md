# Overview
Welcome to Microcontrollers and Embedded Systems, Lab 1!

In this lab, you will learn the basics of terminal navigation, Linux commands, and creating files on computers that don't have screens. The terminal/command line can be a bit intimidating because of how vast it is with no easy way to figure out what things do. However, with a little guidance and practice, you will get it down in no time.

This first lab is going to be very text-heavy, as it is introducing you to most of the tools you will be using every single lab from here on out. Please read through it all, and I promise the future ones will be shorter and focused more on problem-solving.

All labs require a lab report. For a comprehensive look on what the TAs are looking for, formatting, and scoring, take a look at the [Lab Report Guide](TODO: Link here).

These lab guides are handmade, and as such may contain errors in logic, spelling, grammar, etc. If you find any issues, please leave a note in the Feedback tab on the right so we can fix it ASAP.

# Physical Setup
For the physical red pitaya, make sure you have done these things:
1. Place the microSD card into the slot
2. Plug the ethernet cable from the pitaya to your computer (we will be passing out adapters at the beginning of the lab)
3. Provide power to the board with the microUSB port. There are 2 ports, so make sure you are using the POWER one.

If you have completed these steps, you should see the light on the pitaya blinking green and occasionally red. This is normal.

# Virtual Setup
## Connection
Now that your pitaya is all connected, we can make sure it is working digitally. To make sure you are connected properly, visit  http://rp-xxxxxx.local (replace the x's with the six digits on your red pitaya. It will be on the sticker with the QR code). If you are connected properly, you should be brought to a website with a Red Pitaya logo in the background and a bunch of buttons. If the website times out, then something went wrong. See below for some troubleshooting tips.

## Troubleshooting
1. Double check the website name. It is case insensitive. You may also need to add a "/" at the end to connect (i.e. http://rp-xxxxxx.local/), but try it with and without the slash.
2. If you are using a VPN, you may need to disconnect from it to interact with the red pitaya.
3. Try flipping around the ethernet cord and/or the adapter. If you have a nearby friend who's device is working, try using their adapter and see if that is the issue.
4. If none of the above works, contact the nearest TA for assistance.

## Note
Ethernet cords have a little tab you need to press down before pulling them out. Many cords have been broken in this lab. The students who committed such atrocities were shot on sight. Stay safe, take care of your equipment.

## The Terminal
The next step is to actually connect to the pitaya to be able to send commands. Here, the pitaya functions as a "headless" device, meaning it doesn't have a screen or keyboard, etc. In these systems, you will communicate with the device using the terminal. The terminal is a completely text-based system that lets you send and run commands on a device. There are no buttons, no graphics, no instructions. Just a blinking cursor and your sad, tired eyes in the reflection of the black screen. Master the terminal, and you will be unstoppable.

The first step is to open your computer's terminal. All computers come with a terminal app. On Mac, this is aptly named "Terminal." On Windows, this is called "Powershell" (if multiple flavors pop up when your search, pick your favorite). If you are on Linux, I pray that you already know what your terminal is called. If you don't, it might be time to sell your soul to Microsoft.

You should see a blank box with a text cursor and some sort of "prompt" (looks like `C:\Users\YourName >` or `YourName's Macbook 69 Pro $` or something similar). This is where you will enter your text commands. When you enter a command, the computer will respond in some way right under the space where you entered the command, and a new prompt will appear under that, allowing you to type another command. If you want to see this in action, go ahead and type `pwd` into the command prompt and click enter. It should respond with a file path and bring up a new prompt.

There are probably millions of terminal commands out there, and an infinite combination of those commands. To succeed in this lab, you will need to know an infinite number of commands. Wait, no, my sticky note was sideways. You need to know 8. You *should* memorize these commands, but for your convenience, I have also created a [Commands Cheat Sheet](TODO: Link here) to help you out. I will be adding new commands to this document as you learn them, so be sure to check back if you ever forget what command to use.

I also plan on dissecting each important command to help you understand what each command is doing. I don't believe that "repeat after me" learning is worthwhile or a productive use of your time. Here is your first command:

### SSH
Command: `ssh`
Usage: `ssh username@server`
Description: Connects your terminal to another computer's terminal

ssh stands for "secure shell" ("shell" is basically synonymous to "terminal") and is how you access and send commands to computers other than your own. For your pitaya, your username is `root` (which is the default and most powerful user on all devices) and the server is `rp-xxxxxx.local`, where xxxxxx is your pitaya's unique ID number (which can be found on the sticker on your pitaya; some will be under a QR code). Dissecting the command further, you can note that the server is on the `.local` channel because it is physically (locally) connected to your computer.

Try using the `ssh` command with the correct username and server. If all goes correctly, it will prompt you for a password. The password is `root` (secure, I know). <u>You won't see the letters you are typing while entering the password. This is normal and a "security feature." Just type `root` and click enter.</u>

You should now be connected to your pitaya through the terminal. You can check this by seeing if your command line now says `root:~ $` or something similar, instead of your laptop name.

# Linux Commands
Unlike your computer, the Red Pitaya runs on Linux (if your computer also runs Linux... nerd). This means you can run Linux commands without any extra work. Below, you will learn some of these Linux commands (part of the 8 I mentioned above, also available in the [Cheat Sheet](TODO: Link here).)

If you already are comfortable using the command line, you can brush over this. However, if you do so, you will miss the chance to read my lame attempts at humor.

## The Most Important Command
Next, type this command into your terminal `rdmcmdidk` and click enter.

You should get some red text, or at least an angry terminal that says the command you entered is wrong, doesn't exist, etc. This is good. `rdmcmdidk` is a made up command that does not exist. It literally stands for "random command, idk", which I just made up with my extremely creative mind. The lesson here is that you are going to make errors in the terminal. Things are going to go wrong. Things are going to be frustrating. You're going to end up in a folder in who-knows-where trying to run some command that has been outdated since before the first Apple computer came out, wondering how the heck to exit vim. Deep breath. Your terminal may be covered in red error messages, but those don't define you. Wish them away.

Command: `clear`
Usage: `clear`
Description: Clears the old text from your terminal. Does not mess up any configuration.

Make mistakes. It is how you learn. But feel free to keep things clean and tidy while you do.

## The File System
Everything on a computer can be broken down into 2 types of objects: folders and files. Folders, which are mostly referred to as "directories" in the terminal, can only contain other files. Files can only contain data of some kind. When you are on your pitaya, or any terminal session for that matter, you will always be "in" a directory. Think of it as the file system on your computer. There is always one folder that you are looking at, and you can only see the folders "below" that one in the hierarchy. Unlike your computer's file system, you cannot click around to navigate. The terminal needs commands.

The quickest way to tell which directory you are in is to check the command prompt. It will always start with your current location. If you look at your terminal, you should see something like `root@~`. Here, "~" is your directory. The squiggle is a pseudonym for your "home" directory. Imagine this as the very base of your file system, where you open up to every time you open your file explorer (this technically isn't true, but treat it like the base for all intense and porpoises).

We now want to see which files are in our current directory. This will be your next command.

Command: `ls`
Usage `ls`, or `ls -a` to list hidden files too
Description: List ("LiSt") all files and folders in the current directory

Try using the basic `ls` command now. You should see 2 files listed, "empty.txt" and "example.md". These are 2 files I added to your pitaya before you arrived, just so you aren't working with an empty directory. To see what is in a file, use the following command.

Command: `cat`
Usage: `cat file_name`
Description: Prints ("conCATenates") the contents of a file to the terminal.

Try it out now, replacing `file_name` with `example.md`. You should see a little welcome message! You can also try using the `cat` command on the empty.txt file, but nothing will print. That's because the I named the file after the state of your DMs: empty. There is nothing to print if there is nothing in the file.

The next step is to start making our own content. Let's begin with how to make a directory.

Command: `mkdir`
Usage: `mkdir new_directory_name`
Description: Creates a new, empty directory ("MaKe DIRectory") with whatever name you put for `new_directory_name`.

Make your own directory now, call it whatever you like. Note that the terminal does not give an output when you run this command. That means it was successful, and some commands you run won't give an output. As long as you don't get an error message, you can assume things are working. Before moving on, make sure your new folder was successfully created by listing the files in your current directory. You already know this command.

With your new folder/directory created, the next step is to enter it. If you want to do things in the terminal, you usually want to be inside the directory you are interacting with. That brings us to our next command.

Command: `cd`
Usage: `cd directory_name`
Description: Changes your current directory ("Change Directory") to the specified directory name. Paths are relative to your current location (e.x. you can't go from ~/Lab1/screenshots/ into ~/Lab2 by just typing `cd Lab2`. You need to go up the chain and find it).

Try "cd-ing" (a term you might hear in this lab) into your newly made directory, whatever you called it. Check your command prompt to make sure that you are now in `root@~/your_directory_name/` instead of `root@~/`. Now that you are in here, you can run all your normal commands like `ls` to list the files (which will be blank because the directory is empty). You can create more directories and cd into them too, if you wish.

You may encounter a problem here. Once you go "down" into a directory, you cannot go back "up" to the "parent" directory. For example, if you are in `~/random_name/second_name/`, then you cannot go back up by running `cd random_name`. Generally, you can only cd into directories below the one you are currently in. To go up a directory, the special keyword is `..` (two periods). In the terminal, `.` refers to your current directory, and `..` refers to the directory above that (it stops there, no `...` for you. Those are reserved for adding suspense...). So, to go up a directory, you would run `cd ..`. Try it now and check the command prompt to make sure you are in the right place.

You now know all the basic commands for navigating the terminal. Take a second to play around with creating directories, cd-ing into them, going out of them, making more nested directories, etc. As much as you think you can learn from just reading, this is going to be a lot easier if you play with it and make it your own. You are going to have to get very used to this system of navigation, and the more you play with it, the better--and faster--you will get. Eventually, you will be able to jump around your file system like it wasn't even there.

A quick tip: you can use relative file paths to reduce the number of `cd` commands you have to run. For example, if you want to move from `~/Labs/` to `~/Labs/Lab1/programs/`, you don't need to do `cd Lab1` then `cd programs`. You can just do `cd Lab1/programs` to jump right there. You can also do this with `..`s. In `~/Labs/Lab1/programs` and want to get back to `~/Labs/`? Just run `cd ../..` to go up two layers.

You can also use the Tab key to autofill any directory or file name when typing a command. Instead of typing `cd aLongDirectoryName`, just type `cd aLo` and hit tab. The terminal will do all the work for you. (Note that the file/folder has to already exist for this to work).

One more thing. Try using `cat` on a directory. See what it does. The terminal is on your side, there to give you helpful messages to guide you on what went wrong.

Now, I am sure you are eager to start making and editing your own files.

## Editing Files
There are many ways to make and edit files in the terminal. You can't exactly run Microsoft Word in the command line, and without the ability to use a mouse, you might wonder how you would even work with files. Terminal Text Editors are in-terminal apps that let you edit text. There are many options: The "vi" "vim" "nvim" sisters, the original "ed", and the dreaded [emacs](https://xkcd.com/378/). However, in this lab, we will use Nano for it's relative simplicity and ease of use.

Go into a directory of your choice, which is where you will create and edit a new file.

Command: `nano`
Usage `nano file_name`
Description: Runs the Terminal App "Nano," which allows you to edit files. If `file_name` exists in the current directory, you start editing it. If `file_name` does not exist in the current directory, nano will create a new file of that name and begin editing it.

Try creating a new file with a name of your choice now. Remember to add some sort of extension to it (e.x. ".txt", ".md", ".html", whatever you want).

You should now be on a new screen. Notice that there is no longer a command prompt, the organization is different, and there is some text at the bottom of your screen. This is a terminal app, and while you are inside it, you play by its rules. No `ls`ing while you are in here. This is a text editor, and you can only edit text here. Start typing, you will see the characters being written out. You can return, tab, make new lines, etc. just like a normal Word document. If you want to go edit text you already wrote, you need to use the arrow keys on your keyboard to move the cursor around. One thing you might notice is that your "backspace" key deletes the character BEFORE your cursor. This can seem counter intuitive. Too bad. Get used to it.

Now that you have added some text to the file, use the only shortcut you will *need* to know in nano (other shortcuts will be helpful if you learn how to use them, but this lab document is already too long. I will add some of them to the [Cheat Sheet](TODO: Add link)). That command is `CTRL + X`. Note that on Mac's, it is still CTRL, not CMD like you might be used to. Control X is used to exit Nano and return back to the terminal. Executing the shortcut will bring up the dialog at the bottom of your screen `Save modified buffer (ANSWERING "No" WILL DESTROY CHANGES) ?`. This is Squilliam Fancypants way of saying "Wanna save your changes?" If you want to save your changes, type `Y`, otherwise, type `N`. This is explained below the prompt. Clicking `Y` does not mean you are done yet. One more prompt will come up, saying `File Name to write : file_name`. Here, you can edit the name of your file (actually just creates a new file with your most recent changes and doesn't save the original), or leave it as-is. 99% of the time, you will just click Enter at this prompt, keeping the same file name and returning to the terminal.

You will get used to the exit protocol pretty quick. CTRL + X, Y, Enter. CTRL + X, Y, Enter. CTRL + X, Y, Enter. Same thing every time.

You have returned to the terminal in the same directory in which you ran the `nano` command to start with. Home sweet home!

Take a second to mess around with your new file system. Get good at navigating. Make a directory, create a file in it, add some text, print out the file, check which files are in your directory, go up a directory, go down 2 directories in one command, create a file using nano in a *different* directory (hint: rules that apply to one command often apply to another), cat a file in a different directory. And finally, return to the home directory. (That last one has a special shortcut: `cd ~`). Just play. Play with the new system. That is the only way you will get good at it, and trust me, you will need to get good at it. I guarantee you that knowing how to use the terminal will be useful for classes and careers other than this.

# Conclusion
Congratulations! You now know all the basic terminal commands for navigation and file editing. You may have felt a little overwhelmed during this first session. That's okay. It may take a minute to settle into these concepts, but know that there are plenty of resources available to you if you are confused. See either Dr. Camp's office hours or preferably the TA office hours for help with labs, homework, or general questions about the course. All that's left to do now is to write your lab report and submit it via Canvas sometime before your next lab session.

# Assignment
The assignment portion of the lab contains all instructions and requirements for your lab report. Any challenges or questions in the sections above were hypothetical and just for your practice. On your lab report, you only need to respond to the assignments in this section. Remember that you can check out the [Lab Report Guide](TODO: Link here) to see the expectations the TAs have of your lab reports. Without further ado, here is your task:

## Task 1
Starting in the home directory, create a new directory called "first_name" (replacing it with your actual first name) and create a directory inside of that one called "last_name" (same applies). Inside of that second directory, create a file named "smuid.txt" and fill it with your SMUID. No need to delete any files or folders you made while playing around. As long as you have these 3 things, full credit.

Clear your terminal, then show your chain of commands as you go down the directories one-by-one, listing the files in each one, and then printing the SMUID file to the terminal. You should then return to the home directory, going up one folder at a time. Take a screenshot of your terminal and include it in your lab report. You should only need the 1 screenshot that has your terminal's history of the commands listed in this paragraph.

Explain the difference between `cat` and `nano` if you just want to read what is in a file.

Explain what happens when you try to `cat` a directory and why you get the result that you do.

Explain what the `pwd` command does and how to use it. Note that this is something you will need to look up on your own. You are encouraged to learn more Linux commands beyond the 8 you *need* to know for this course. It will make you a better programmer and change the way you interact with computers. The TAs can give you recommendations on where to start if you are interested.


