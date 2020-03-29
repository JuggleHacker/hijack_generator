# If we have a partially complete siteswap, how can we fill in the gaps?
# Note, I will use "?" to denote a gap in the pattern
import siteswap_states

def valid_so_far(partial_siteswap):
    period = len(partial_siteswap)
    landing_sites = set()
    for time, throw in enumerate(partial_siteswap):
        if throw == "?":
            continue
        else:
            landing_site = (time + throw) % period
            if landing_site in landing_sites:
                return False
            else:
                landing_sites.add(landing_site)
    return True


def ways_to_complete(partial_siteswap, list_of_throws, number_of_objects, solutions):

    if not valid_so_far(partial_siteswap):
        return None


    elif '?' not in partial_siteswap:
        if number_of_objects == None:
            solutions.append(partial_siteswap)
        elif sum(partial_siteswap)/len(partial_siteswap) == number_of_objects:
            solutions.append(partial_siteswap)

    else:
        first_unknown_throw_index = partial_siteswap.index('?')
        for throw in list_of_throws:
            trial_siteswap = partial_siteswap.copy()
            trial_siteswap[first_unknown_throw_index] = throw
            ways_to_complete(trial_siteswap, list_of_throws, number_of_objects,solutions)
    return None

def complete(partial_siteswap, list_of_throws, number_of_objects=None):
    solutions = []
    ways_to_complete(partial_siteswap, list_of_throws, number_of_objects, solutions)
    return solutions

def filter_rotations(list_of_lists_of_numbers):
    filtered_list = []
    for list in list_of_lists_of_numbers:
        list_to_be_added = True
        n = len(list)
        for i in range(n):
            if list[i:]+list[:i] in filtered_list:
                list_to_be_added = False
        if list_to_be_added:
            filtered_list.append(list)
    return filtered_list

# for pattern in filter_rotations(complete([7]+['?']*4,[2,5,6,7,8],6)):
#     if 5 in pattern:
#         print(pattern)
#
# period_6s = complete([5]+['?']*5,[2,5,6,7,8])
# for pattern in period_6s:
#     print(pattern)
