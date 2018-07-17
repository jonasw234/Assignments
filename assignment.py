#!/usr/bin/env python3
"""
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
"""
from docopt import docopt
import numpy as np
from scipy.optimize import linear_sum_assignment


def read_input_from_command_line():
    """ Read input from command line."""
    # Read array values as input from user as preferences for each assignment
    print('Please enter teams as CSV: ', end='')
    teams_input = input()
    teams = [t.strip() for t in teams_input.split(',')]
    print('Please enter assignments as CSV: ', end='')
    assignments_input = input()
    assignments = [a.strip() for a in assignments_input.split(',')]
    cost = np.zeros((len(teams), len(assignments)), np.int32)
    for team_no, team in enumerate(teams):
        for assignment_no, assignment in enumerate(assignments):
            print('Please enter team {team}\'s priority for {assignment}: '.format(team=team,
                assignment=assignment), end='')
            priority = input()
            priority = int(priority)
            cost[team_no][assignment_no] = priority
    return teams, assignments, cost


def read_input_from_file(filename):
    """Read input from CSV file `filename`."""
    teams = np.genfromtxt(filename, max_rows=1, delimiter=',', dtype=str, autostrip=True)
    assignments = np.genfromtxt(filename, skip_header=1, max_rows=1, delimiter=',', dtype=str,
        autostrip=True)
    cost = np.genfromtxt(filename, skip_header=2, delimiter=',')
    return teams, assignments, cost


def main():
    """Read input, calculate assignments."""
    # Determine source of input
    args = docopt(__doc__)
    if args['--filename'] is None:
        teams, assignments, cost = read_input_from_command_line()
    else:
        teams, assignments, cost = read_input_from_file(args['--filename'])

    # Calculate best assignment using Hungarian algorithm and output results
    row_ind, col_ind = linear_sum_assignment(cost)
    for team_no, assignment_no in enumerate(col_ind):
        print('Team {team} gets assignment {assignment}.'.format(team=teams[team_no],
            assignment=assignments[assignment_no]))


if __name__ == '__main__':
    main()
