# A script to generate all possible hijacks, given a pattern
import complete_the_siteswap
import siteswap_states

def find_transitions(start_pattern, target_pattern, permitted_transition_throws=[2,4,6,8]):
    """ Finds transitions between a start pattern and an end pattern."""

    active_throws = str(start_pattern[0::2])+'*'+str(target_pattern[0::2])
    passive_throws = str(start_pattern[1::2])+str(target_pattern[1::2])
    if siteswap_states.state(target_pattern) == siteswap_states.state(start_pattern):
        return [start_pattern, target_pattern, 'Active '+active_throws.replace('*','')+'\n'+'Passive '+passive_throws]
    elif target_pattern[0] % 2 == 0: # trying to do a self which doesn't fit
        target_pattern = target_pattern[1:] + [target_pattern[0]]
        target_state = siteswap_states.state(target_pattern)
        state_before_transition_throw = siteswap_states.state(start_pattern)
        for throw in permitted_transition_throws:

            new_state = siteswap_states.make_a_throw(throw, state_before_transition_throw)
            if new_state == target_state:
                active_throws = str(start_pattern[0::2])+'*'+str(target_pattern[1::2])
                passive_throws = str(start_pattern[1::2])+str(target_pattern[0::2])
                return [start_pattern, target_pattern, 'Active '+active_throws.replace('*',str(throw))+'\n'+'Passive '+passive_throws]
    else: # trying to do a new pass which doesn't fit yet

        start_pattern = start_pattern[-2:] + start_pattern[:-2]
        target_pattern = target_pattern[-2:] + target_pattern[:-2]

        # First noted when trying to transition from not-why to parsnip vs funky bookends:
        # You may need to go back multiple times if there is a pass before the new pass
        while start_pattern[0] %2 == 1:
            start_pattern = start_pattern[-2:] + start_pattern[:-2]
            target_pattern = target_pattern[-2:] + target_pattern[:-2]
        target_pattern = target_pattern[1:] + [target_pattern[0]]
        target_state = siteswap_states.state(target_pattern)
        state_before_transition_throw = siteswap_states.state(start_pattern)

        for throw in permitted_transition_throws:

            new_state = siteswap_states.make_a_throw(throw, state_before_transition_throw)
            if new_state == target_state:
                active_throws = str(start_pattern[0::2])+'*'+str(target_pattern[1::2])
                passive_throws = str(start_pattern[1::2])+str(target_pattern[0::2])
                return [start_pattern, target_pattern,'Active '+active_throws.replace('*',str(throw))+'\n'+'Passive '+passive_throws]
                # I claim there can be at most one transition throw, so can stop looking once one is found.
        #print("No transition found from {} to {}".format(start_pattern,target_pattern))

def do_not_throw_pass(raw_siteswap,index, permitted_throws):

    patterns_found = []
    siteswap = raw_siteswap.copy()
    siteswap = siteswap[index:] + siteswap[:index] # rotate so pass at front
    number_of_objects = sum(siteswap)/len(siteswap)
    # print(siteswap)

    if siteswap[0] != 7:
        print("There's no pass there not to throw!")
        return None

    elif len([throw for throw in raw_siteswap if throw %2 == 1])<=2:
        #All selfs, not an interesting pattern
        return []
    else: # siteswap[0] == 7 and still have passes after removing it
        siteswap[0] = '?'
        siteswap[5%len(siteswap)] = 2

    for time, throw in enumerate(siteswap):
        if throw != '?' and time % 2 == 0 and throw % 2 == 0:
            siteswap[time] = '?'

    permitted_self_throws = [throw for throw in permitted_throws if throw%2 == 0] # This is to rule out adding in extra passes over the transition
    solutions = complete_the_siteswap.complete(siteswap,permitted_self_throws,number_of_objects)
    raw_siteswap = raw_siteswap[index:]+raw_siteswap[:index]
    if solutions == []:
        pass
    for pattern in complete_the_siteswap.filter_rotations(solutions):
        patterns_found.append(find_transitions(raw_siteswap,pattern,[2,4,6,8]))
    return patterns_found




def throw_extra_pass(raw_siteswap,index, permitted_throws):
    siteswap = raw_siteswap.copy()
    siteswap = siteswap[index:]+siteswap[:index] # rotate so extra pass is at front
    patterns_found = []
    # print(siteswap)

    number_of_objects = sum(siteswap)/len(siteswap)

    for time, throw in enumerate(siteswap):
        if time % 2 == 0 and throw % 2 == 0:
            siteswap[time] = '?'
    siteswap[0] = 7
    # TODO: does this give weird results?
    siteswap[5%len(siteswap)] = 7

    permitted_self_throws = [throw for throw in permitted_throws if throw%2 == 0] # This is to rule out adding in extra passes over the transition
    solutions = complete_the_siteswap.complete(siteswap,permitted_self_throws,number_of_objects)
    raw_siteswap = raw_siteswap[index:]+raw_siteswap[:index]
    if solutions == []:
        pass
    for pattern in complete_the_siteswap.filter_rotations(solutions):
        patterns_found.append(find_transitions(raw_siteswap,pattern,[2,4,6,8]))
    return patterns_found

def generate_hijacks(siteswap, permitted_throws):
    hijacks_found = []
    if len(siteswap)%2 == 1:
        siteswap *= 2
    #print(siteswap)
    for index, throw in enumerate(siteswap):
        #print('----------')
        if index % 2 == 0 and throw == 7:
            # print('Calling do_not_throw_pass({}, {}, {})'.format(siteswap,index,permitted_throws))
            hijacks_found +=  do_not_throw_pass(siteswap, index, permitted_throws)
        elif index % 2 == 1 and throw == 2:
            extra_pass_index = (index - 5) % len(siteswap)
            # print('Calling throw_extra_pass({}, {}, {})'.format(siteswap,extra_pass_index,permitted_throws))
            hijacks_found += throw_extra_pass(siteswap, extra_pass_index, permitted_throws)
    return hijacks_found
