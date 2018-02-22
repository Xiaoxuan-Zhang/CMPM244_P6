from game import Simulator

def analyze(design):
    results = None
	# Called every time the design is edited
	# Returns results that can be inspected
    sim = Simulator(design)
    init = sim.get_initial_state()
    moves = sim.get_moves()
    next_state = sim.get_next_state(init, moves[0])

    position, abilities = next_state # or None if character dies
    i, j = position


    #… # Discover all reachable states.
    #… # Package results for inspection later.
    return results
'''

def inspect(results, pos, draw_line):

    # Called when the cursor is moved over tile
    # using results of last analyze()
    #…
    # Draws informative lines using draw_line
    # (documented later)
'''




