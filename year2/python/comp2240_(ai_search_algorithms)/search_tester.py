## search_tester.py
## by Brandon Bennett --- 27/10/2009

## This is the top level file for running various search
## algorithms.

print( "Loading search_tester.py" )

import sys
from tree          import *
from queue_search  import *
from robot_servant import *
from knights_tour  import *
from eight_puzzle  import *

print( "*All imports loaded*\n" )

# Use this if you want to make Python wait between search tests.
def wait():
      input('<Press enter to continue>')


def run_tests_on_knight_puzzle():
      print( "*Running Knight's Tour search tests*\n" )
      ## Extend this definition to carry out tests as specified in
      ## question 1.a.i.
      search(get_knights_tour_problem(4,4), 'depth_first',   100000, [] )
      search(get_knights_tour_problem(5,5), 'depth_first',   500000, [] )


def run_tests_on_robot_search_problem():
      ### This is for illustration.
      ### But you should use a similar proceedure to carry out the
      ### search tests specified in Part 2 of the coursework.
      MAX_NODES = 5000
      search( robot_search_problem_1, 'breadth_first', MAX_NODES, [])

      wait()
      search( robot_search_problem_1, 'breadth_first', MAX_NODES, ['loop_check'])
      wait()
      search( robot_search_problem_1, 'depth_first', MAX_NODES, [])
      wait()
      search( robot_search_problem_1, 'depth_first', MAX_NODES, ['loop_check'])
      wait()
      search( robot_search_problem_1, 'randomised_depth_first', MAX_NODES, [])
      wait()
      search( robot_search_problem_1, 'randomised_depth_first', MAX_NODES, ['loop_check'])


def run_tests_on_eight_puzzle():
    """
    Attempts to solve the eight puzzle problem for some search algorithms under
    some conditions.
    """
    # To run a specific algorithm under specific conditions, the lists below
    # are formatted in such a way that it is easy to comment out any element.

    MAX_NODES = [
                 5000,
                 10000,
                 15000,
                 40000,
                 80000,
                 160000,
                ]

    STRATEGIES = [
                  'breadth_first',
                  'depth_first',
                  'randomised_depth_first',
                  ('best_first', eight_misplaced_tiles_heuristic),
                  ('best_first', eight_manhatten_heuristic),
                  ('A_star', eight_misplaced_tiles_heuristic),
                  ('A_star', eight_manhatten_heuristic)
                 ]

    OPTIONS = [
                'loop_check',
                []
              ]

    for STRATEGY in STRATEGIES:
        for OPTION in OPTIONS:
            for MAX in MAX_NODES:
                search(eight_puzzle, STRATEGY, MAX, OPTION)
#                wait()


def main():
    """
    Runs some search algorithms on some problems.
    """
    run_tests_on_eight_puzzle()
#    run_tests_on_robot_search_problem()
#    run_tests_on_knight_puzzle()


if __name__ == "__main__":
    main()
