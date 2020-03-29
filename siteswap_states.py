
# A script to explore siteswap states


# Question 1: given a siteswap, how do I get its state?

def is_valid_state(state):
    """ Returns True if a list of integers is a valid state, False otherwise """

    for landing_site in state:
        if landing_site != 0 and landing_site != 1:
            return False
    return True

def possible_throw_from(state, permitted_throws):
    """ Given a state and a list of permitted throws, returns a list of which
    throws are possible """

    if state[0] == 0:
        return [0] if 0 in permitted_throws else []
    else:
        possible_throws = []
        for throw in permitted_throws:
            if throw >= len(state):
                possible_throws.append(throw)
            elif state[throw] == 0:
                possible_throws.append(throw)
        return possible_throws


def state(siteswap):
    """ Takes a list of integers (throws) and returns the state """

    # Look backwards for what has been thrown, and where it is hitting.
    # How many throws do you need to look back? At most the highest throw
    highest_throw = max(siteswap)
    period = len(siteswap)

    i = 1
    landing_times = []
    while i <= highest_throw:
        j = (i % period)
        if siteswap[-j] != 0:
            if -i + siteswap[-j] >= 0: # object still has to land!
                landing_times.append(-i + siteswap[-j])
        i += 1

    latest_landing_object = max(landing_times)
    state = [0] * (latest_landing_object + 1)
    for landing_time in landing_times:
        state[landing_time] += 1
    return state

def make_a_throw(throw, state):
    """ Returns the new state after making the given throw """
    if state[0] == 0:
        if throw != 0:
            return False
        else:
            return state[1:]
    else: # we have an object to make a throw with!
        new_state = state.copy()
        if throw >= len(state):
            new_state += [0] * (throw - len(state) + 1)
            new_state[throw] = 1
        else:
            new_state[throw] += 1


    return new_state[1:]

def transition_to_ground_state(state):
    """ Prints a sequence of throws to get into ground state, from the given state """
    while 0 in state:
        next_zero = state.index(0)
        state = make_a_throw(next_zero, state)
        print(next_zero, state)

def transition_from_ground_state(state):
    """ Prints a sequence fo throws to get from the gound state into a given state """
    ground_state = [1] * state.count(1) # ground state with appropriate number of objects
    if state == ground_state:
        return None
    current_state = ground_state
    first_zero = state.index(0)
    i = first_zero
    while state[i] == 0:
        i += 1
    # i will now be the 1 after the first zero - we want to throw here!
    throw_to_make = len(ground_state) + i - first_zero
    current_state = make_a_throw(throw_to_make, current_state)
    print(throw_to_make, current_state)
    i += 1
    while i < len(state):

        if state[i] == 0:
            j = i
            while state[j] == 0:
                j += 1
            throw_to_make += (j - i)
            i = j
        current_state = make_a_throw(throw_to_make, current_state)
        print(throw_to_make, current_state)
        i += 1

def transition_between(start_state, end_state, permitted_throws):
    """ Returns a sequence of throws from the given permitted throws, which
    will transition from the given start_state, to the given end state.
    If no transition is possible with the given throws, the funciton will
    print "No transition possible" and return None """
    states_visited = {'':start_state}
    while True:
        updated_states_visited = states_visited.copy()
        for transition, state in states_visited.items():
            print(transition, state, states_visited)
            for possible_throw in possible_throw_from(state, permitted_throws):
                next_state = make_a_throw(possible_throw, state)
                print(next_state, possible_throw, state)
                if next_state not in updated_states_visited.values():
                    updated_states_visited[transition + str(possible_throw)] = next_state
                    if next_state == end_state:
                        return transition + str(possible_throw)
        if len(updated_states_visited) == len(states_visited):
            break
        else:
            states_visited = updated_states_visited
    print("No transition possible")
    return None



def transition_throws(base_pattern, target_pattern, permitted_throws):
    base_state = state(base_pattern)
    target_state = state(target_pattern)
    #print(base_state == target_state)
    if base_state == target_state:
        print("No transition throws needed, patterns are the same state.")
    print(base_state, target_state)
    for throw in permitted_throws:
        test_state = base_state.copy()
        test_state = make_a_throw(throw, test_state)
        print(throw, test_state)
        if test_state == target_state:
            print("Transition found: {}".format(throw))

print(state([8,6,2,7,7,8,6,2,7,7]))
print(state([6,7,7,7,8,2,7,7,7,2]))
