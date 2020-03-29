# A script to generate all possible hijacks, given a pattern
import complete_the_siteswap
import siteswap_states

def find_transitions(start_pattern, target_pattern, permitted_throws):
    """ Write target_pattern with the new or missing pass at index 0"""
    # print(start_pattern)
    # print(target_pattern)
    active_throws = str(start_pattern[0::2])+'*'+str(target_pattern[0::2])
    passive_throws = str(start_pattern[1::2])+str(target_pattern[1::2])
    if siteswap_states.state(target_pattern) == siteswap_states.state(start_pattern):
        return [start_pattern, target_pattern, 'Active '+active_throws.replace('*','')+'\n'+'Passive '+passive_throws]
    elif target_pattern[0] != 7: # trying to do a self which doesn't fit
        target_pattern = target_pattern[1:] + [target_pattern[0]]
        target_state = siteswap_states.state(target_pattern)
        state_before_transition_throw = siteswap_states.state(start_pattern)
        for throw in permitted_throws:

            new_state = siteswap_states.make_a_throw(throw, state_before_transition_throw)
            if new_state == target_state:
                print("Branch A activated")
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

        for throw in permitted_throws:
            
            new_state = siteswap_states.make_a_throw(throw, state_before_transition_throw)
            if new_state == target_state:
                print("Branch B activated")
                active_throws = str(start_pattern[0::2])+'*'+str(target_pattern[1::2])
                passive_throws = str(start_pattern[1::2])+str(target_pattern[0::2])
                return [start_pattern, target_pattern,'Active '+active_throws.replace('*',str(throw))+'\n'+'Passive '+passive_throws]
                # I claim there can be at most one transition throw, so can stop looking once one is found.
        print("No transition found from {} to {}".format(start_pattern,target_pattern))

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
        print("You'll have all selfs if you do that!")
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
        print('Nope')
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
        print('Nope')
    for pattern in complete_the_siteswap.filter_rotations(solutions):
        patterns_found.append(find_transitions(raw_siteswap,pattern,[2,4,6,8]))
    return patterns_found



# print(find_transitions([6,7,2,7,8,6,7,2,7,8],[7,7,7,2,6,7,7,7,8,2],[2,4,6,8]))
# print(find_transitions([7, 2, 8, 6, 7, 7, 2, 8, 6, 7],[7, 7, 2, 6, 7, 7, 7, 8, 2, 7],[2,4,6,8]))
# print(find_transitions([7, 8, 2, 7, 7, 7, 2, 6, 7, 7],[7, 8, 6, 7, 2, 7, 8, 6, 7, 2],[2,4,6,8]))
# print(find_transitions([7,2,8,6,7,7,2,8,6,7],[7, 7, 2, 6, 7, 7, 7, 8, 2, 7],[2,4,6,8]))
# print(find_transitions([7, 7, 2, 6, 7, 7, 7, 8, 2, 7],[2, 7, 8, 6, 7, 2, 7, 8, 6, 7],[2,4,6,8]))
# print(find_transitions([7, 7, 7, 8, 2, 7, 7, 7, 2, 6],[2, 7, 7, 8, 6, 2, 7, 7, 8, 6],[2,4,6,8]))
# print(find_transitions([7, 8, 2, 7, 7, 7, 2, 6, 7, 7],[2, 8, 6, 7, 7, 2, 8,6, 7, 7],[2,4,6,8]))
# print(find_transitions([2, 7, 7, 8, 6, 2, 7, 7, 8, 6],[7, 7, 7, 8, 2, 7, 7, 7, 2,6],[2,4,6,8]))

#find_transitions([2, 8, 6, 7, 7, 2, 8, 6, 7, 7],[7, 8, 2, 7, 7, 7, 2, 6, 7, 7],[0,2,4,6,8,10])






def generate_hijacks(siteswap, permitted_throws):
    hijacks_found = []
    # TODO: Why does the period have to be 5 locally when the hijack pass is a 7? Does it?!
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
            print('Calling throw_extra_pass({}, {}, {})'.format(siteswap,extra_pass_index,permitted_throws))
            hijacks_found += throw_extra_pass(siteswap, extra_pass_index, permitted_throws)
    return hijacks_found



for pattern in generate_hijacks([7,8,6,2,7,7,8,6,2,7], [2,4,6,7,8]): # why-not
    print(pattern)
print('----------')
#generate_hijacks([7,2,8,6,7], [2,6,7,8]) # not-why
# print('----------')
# generate_hijacks([8, 8, 8, 2, 7, 2, 6, 6, 6, 7], [2,6,7,8]) #popcorn vs whoops
# print('----------')
#generate_hijacks([8, 8, 2, 7, 2, 6, 6, 6, 7,8], [2,6,7,8])
#print('----------')
# generate_hijacks([7, 8, 2, 7, 7, 7, 2, 6, 7, 7], [2,6,7,8])
# print('----------')
# generate_hijacks([7, 8, 6, 2, 6, 7, 8, 6, 8, 2], [2,6,7,8]) # popcorn vs 5 club why not
# generate_hijacks([8, 6, 2, 6, 7, 8, 6, 8, 2,7], [2,6,7,8]) # 5 club why not vs popcorn note: there aren't any!
# print('----------')
# generate_hijacks([7,2,7,8,6], [2,6,7,8]) # maybe
#funky bookends vs parsnip
#
# for transition in generate_hijacks([6, 2, 6, 7, 5, 2, 6, 4, 7, 5], [2,6,7,8]):
#     print(transition[2]) #parsnip vs funky bookends
#
# print('-'*20)
# for transition in generate_hijacks([2, 6, 7, 5, 2, 6, 4, 7, 5, 6], [2,6,7,8]):
#     print(transition[2]) #parsnip vs funky bookends
# print("Martin's one count")
#print(generate_hijacks([7,7,7,7,2,7,7,7,7,2], [2,6,7,8]))
# print("Maybe")
# generate_hijacks([7,2,7,8,6,7,2,7,8,6],[2,6,7,8])
#generate_hijacks([7,2,8,6,7,7,2,8,6,7], [2,6,7,8]) # not why
#print('----------')

#generate_hijacks([8, 2, 8, 6, 7, 2, 6, 8, 6, 7], [2,6,7,8]) # popcorn vs 5 club not why.
#generate_hijacks([8, 6, 7, 8, 2, 8, 6, 7, 2, 6, ], [2,6,7,8]) # 5 club not why vs popcorn - note: there aren't any!
# generate_hijacks([7, 2, 6, 6, 6, 7, 8, 8, 8, 2], [2,6,7,8]) # popcorn vs whoops
# print('----------')

# generate_hijacks([7, 2, 6, 6, 7, 7, 8, 8, 2, 7], [2,6,7,8]) # why not vs not why
# generate_hijacks([7, 8, 8, 2, 7, 7, 2, 6, 6, 7], [2,6,7,8]) # not why vs why not
# generate_hijacks([8,8,8,2,7,2,6,6,6,7], [2,6,7,8])


# generate_hijacks([7,7,7,8,6,7,7,8,6,7], [2,6,7,8, 10]) # funky funky bookends vs bookends


#generate_hijacks([7,7,7,8,6], [2,6,7,8,10]) funky bookends, 3 options: passive into why not, not why or maybe
#Option 1: passive into why not
#generate_hijacks([10, 7, 7, 8, 8, 2, 7, 7, 8, 6], [2,6,7,8,10])
#generate_hijacks([7, 7, 8, 8, 2, 7, 7, 8, 6, 10], [2,6,7,8])
#Option 2: passive into not why
#generate_hijacks([8, 8, 10, 7, 7, 2, 8, 6, 7, 7], [2,6,7,8,10])
#generate_hijacks([8, 10, 7, 7, 2, 8, 6, 7, 7,8], [2,6,7,8])
#Option 3: passive into maybe
#generate_hijacks([10, 7, 10, 6, 7, 2, 7, 8, 6, 7], [2,6,7,8,10])
#generate_hijacks([7, 10, 6, 7, 2, 7, 8, 6, 7, 10], [2,6,7,8])
# Now there are 3 5-club patterns which go against TTTPH - why-not, not-why and whoops
# Option 1: 5 club why-not
#generate_hijacks([10, 7, 10, 6, 10, 2, 7, 8, 8, 2], [2,6,7,8,10])
#generate_hijacks([7, 10, 6, 10, 2, 7, 8, 8, 2, 10], [2,6,7,8]) No results - no zips to target, and only 1 pass not to throw!
# # Option 2: 5 club not-why
#generate_hijacks([10, 2, 10, 6, 7, 2, 8, 8, 10, 7], [2,6,7,8,10])
#generate_hijacks([2, 10, 6, 7, 2, 8, 8, 10, 7, 10], [2,6,7,8]) No results - no zips to target, and only 1 pass not to throw!
# # Option 3: 5 club whoops
#generate_hijacks([10, 8, 10, 2, 7, 2, 8, 6, 10, 7], [2,6,7,8,10])
#generate_hijacks([8, 10, 2, 7, 2, 8, 6, 10, 7, 10], [2,6,7,8])

# passive 6 club why-not/not-whyer can go into popcorn in 2 different ways.
# way 1:
#generate_hijacks([6, 7, 8, 8, 8, 2, 7, 8, 6, 10], [2,6,7,8,10])
#generate_hijacks([7, 8, 8, 8, 2, 7, 8, 6, 10, 6], [2,6,7,8])
# way 2:
#generate_hijacks([8, 8, 8, 10, 7, 2, 6, 8, 6, 7], [2,6,7,8,10])
#generate_hijacks([8, 8, 10, 7, 2, 6, 8, 6, 7, 8], [2,6,7,8])
# going from maybe vs PPSTT gives two options:
# Option 1:
#generate_hijacks([6, 10, 6, 7, 8, 2, 8, 6, 7, 10], [2,6,7,8])
#generate_hijacks([10, 6, 7, 8, 2, 8, 6, 7, 10, 6], [2,6,7,8,10])
# Option 2:
#generate_hijacks([8, 10, 7, 10, 6, 2, 6, 7, 8, 6], [2,6,7,8])
#generate_hijacks([10, 7, 10, 6, 2, 6, 7, 8, 6, 8], [2,6,7,8,10])


# Let's add in zaps!
#generate_hijacks([7, 2, 8, 8, 5, 7, 2, 8, 8, 5], [2,4,5,6,7,8,9]) # gives two options: [8, 2, 8, 8, 5, 2, 6, 8, 8, 5] or [7, 7, 4, 8, 5, 7, 7, 8, 2, 5]
#generate_hijacks([8, 2, 8, 8, 5, 2, 6, 8, 8, 5], [2,4,5,6,7,8,9]) # two optoins: back where we came or into [78852]
#generate_hijacks([2, 8, 8, 5, 2, 6, 8, 8, 5, 8], [2,5,6,7,8,9]) # no options, no pass not to throw, no zip to target
#generate_hijacks([7, 8, 8, 5, 2, 7, 8, 8, 5, 2], [2,4,5,6,7,8,9])
#generate_hijacks([7, 7, 4, 8, 5, 7, 7, 8, 2, 5], [2,4,5,6,7,8,9])
#generate_hijacks([7, 4, 8, 5, 7, 7, 8, 2, 5, 7], [2,4,5,6,7,8,9])
#generate_hijacks([7, 7, 4, 7, 5], [2,4,5,6,7,8,9])

# Let's add in zaps part 2
#generate_hijacks([7, 5, 6, 6, 6], [2,4,5,6,7,8,9]) # only one option [8, 5, 8, 6, 8, 2, 5, 6, 6, 6]
#generate_hijacks([8, 5, 8, 6, 8, 2, 5, 6, 6, 6], [2,4,5,6,7,8,9])
#generate_hijacks([5, 8, 6, 8, 2, 5, 6, 6, 6, 8], [2,4,5,6,7,8,9])

# Let's add in zaps part 3
# generate_hijacks([7, 5, 8, 5, 5], [2,4,5,6,7,8,9]) # no results
