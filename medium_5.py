def get_valid_configurations(target, L1, L2, L3, D):
   """
   Generates all valid (Inner, Middle, Outer) tuples for a given target.
   """
   valid_states = []
   # Try all possible lengths for the Inner segment
   for inner in range(min(target, L1) + 1):
       # Try all possible lengths for the Outer segment
       for outer in range(min(target - inner, L3) + 1):
           # The Middle segment makes up the rest of the target distance
           middle = target - inner - outer


           # Check if Middle is within limits AND the stability constraint is met
           if 0 <= middle <= L2 and abs(inner - outer) <= D:
               valid_states.append((inner, middle, outer))


   return valid_states




def calculate_transition_cost(prev_state, curr_state, W1, W2, W3):
   """
   Calculates the wear cost of moving from one configuration to another.
   """
   delta_inner = abs(prev_state[0] - curr_state[0])
   delta_middle = abs(prev_state[1] - curr_state[1])
   delta_outer = abs(prev_state[2] - curr_state[2])


   return (delta_inner * W1) + (delta_middle * W2) + (delta_outer * W3)




def minimum_wear_cost(limits, wear_factors, targets, D):
   """
   Determines the minimum total wear cost to hit all targets in sequence.
   """
   L1, L2, L3 = limits
   W1, W2, W3 = wear_factors


   # DP Table: Maps a valid state (tuple) to the minimum cost to reach it.
   # The arm always starts at configuration (0, 0, 0) with a cost of 0.
   prev_states = {(0, 0, 0): 0}


   for target in targets:
       # Find all valid arm configurations for the current target
       curr_valid_states = get_valid_configurations(target, L1, L2, L3, D)


       # If a target cannot be reached without breaking limits/stability, abort
       if not curr_valid_states:
           print(f"Error: Target {target} is unreachable under current constraints.")
           return -1


       new_states_costs = {}


       # For every valid configuration for the current target...
       for curr_state in curr_valid_states:
           min_cost_to_reach_curr = float('inf')


           # ...calculate the cost to reach it from EVERY valid configuration of the previous target
           for prev_state, accumulated_cost in prev_states.items():
               transition_cost = calculate_transition_cost(prev_state, curr_state, W1, W2, W3)
               total_cost = accumulated_cost + transition_cost


               # We only care about the absolute cheapest path to this current state
               if total_cost < min_cost_to_reach_curr:
                   min_cost_to_reach_curr = total_cost


           new_states_costs[curr_state] = min_cost_to_reach_curr


       # Current states become the "previous" states for the next target
       prev_states = new_states_costs


   # Once all targets are processed, the answer is the minimum cost among the final states
   return min(prev_states.values())


if __name__ == "__main__":
   Limits = eval(input("Enter limits: "))
   Wear_Factors = eval(input("Enter wear factors: "))
   Targets = eval(input("Enter targets: "))
   D = int(input("Enter D: "))


   min_cost = minimum_wear_cost(Limits, Wear_Factors, Targets, D)
   print(f"Minimum total wear cost to complete all targets: {min_cost}")

