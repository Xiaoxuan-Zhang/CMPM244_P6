from game import Simulator
from collections import deque

import sys
import random

def analyze(design):
    results = dict()
	# Called every time the design is edited
	# Returns results that can be inspected
    # Discover all reachable states.
    queue = deque()
    visited = set()
    sim = Simulator(design)
    moves = sim.get_moves()
    # start exploration
    init = sim.get_initial_state()
    queue.append(init)

    last_pos = dict()
    last_pos[init] = None
    while len(queue) != 0:
        current_state = queue.popleft()

        for move in moves:
            next_state = sim.get_next_state(current_state, move)
            if next_state in visited:
                continue
            if next_state == current_state:
                continue

            if next_state is not None and next_state not in queue:
                queue.append(next_state)
                last_pos[next_state] = current_state
        visited.add(current_state)

    # position, abilities = next_state # or None if character dies
    # i, j = position

    #… # Package results for inspection later.
    for state in visited:
        position, abilities = state
        if position not in results:
            results[position] = {}
        results[position][abilities] = reconstruct_path(last_pos, state)

    return results

def reconstruct_path(last_pos, current):
    path = []
    while current in last_pos:
        path.append(current)
        current = last_pos[current]
    path.reverse()
    return path


def inspect(results, pos, draw_line):
    if pos in results:
        if sys.argv[2] == 'singlepath':
            # find the shortest path
            steps = 9999
            shortest_key = None
            for key, route in results[pos].items():
                if len(route) < steps:
                    steps = len(route)
                    shortest_key = key
            path = results[pos][shortest_key]
            for i in range(len(path) - 1):

                draw_line(path[i][0], path[i + 1][0], None, route[i][1])

        elif sys.argv[2] == 'multiplepath':
            for key, route in results[pos].items():
                for i in range(len(route) - 1):
                    draw_line(route[i][0], route[i + 1][0], route[i][1], route[i][1])
    else:
        print('Unreachable position.')

    # Called when the cursor is moved over tile
    # using results of last analyze()
    #…
    # Draws informative lines using draw_line
    # (documented later)





