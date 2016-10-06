# asm2ws
A python3 cross compiler from (a custom version of) ASM file to
Whitespace.

This script interprets a pseudo-ASM, or ASM-like language I made to represent
commands in the [WhiteSpace](http://compsoc.dur.ac.uk/whitespace/tutorial.html) language.
It then writes out the corresponding Whitespace code to a file.

The language is simply a set of keywords that represent each possible
Whitespace command as a character string instead of a sequence of spaces and
tabs followed by a newline. Numbers and labels are also represented in order to
facilitate reading and writing of code: numbers are written out in numerical
characters, with an optional sign. Labels are written as as series of ones and
zeroes, representing respectively tabs and spaces.

Why make this, and why put it up on github? I found myself wanting to write a
simple Whitespace program as part of a CTF challenge I was creating. After
reading the language's doc (at the website linked above) I felt I could quite
easily write the kind of program I wanted. The language is surprisingly easy to
grasp! Unfortunately, writing with spaces, tabs and newlines makes it difficult
to keep all the commands available to you in your head at once, which would
severely slow me down (not to metion render the process unpleasant). I figured
an assembly-like language fit 1-to-1 with Whitespace's commands. I figured I'd
upload the code and share it in case anyone else ever wants to write a quick
Whitespace program (for whatever reason) and like me couldn't find much reading
to be had on the language (i.e. I couldn't find any tutorials online apart from
the very basic one at the bottom of the page above).  Sidenote:
tutorialspoint's online IDE can parse Whitespace, rendering it much more
lisible, and the default file is a Hello World, giving a tutorial on printing
strings.
