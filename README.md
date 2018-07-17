# Assignments
Find the best assignment for a group of teams based on their preferences.

Usage: assignment.py [-f FILENAME]

Options:
    -f FILENAME --filename=FILENAME  Use this CSV file as input

If no input file is given, the program will interactively ask for the input.
The CSV file needs to have the following format:
    Team name 1, ..., Team name n
    Assignment 1, ..., Assignment m
    Preference Team 1 Assignment 1, ..., Preference Team 1 Assignment m
    ...
    Preference Team n Assignment 1, ..., Preference Team n Assignment m

Lower preference numbers mean the team has a higher desire to work on this assignment (think of it
as 1st, 2nd, ..., nth choices).

Requires: docopt, numpy, scipy
