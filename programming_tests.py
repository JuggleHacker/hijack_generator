import unittest
import programming


class FindTransitionsTests(unittest.TestCase):

    def test_no_transition_throws_needed_not_throwing_a_pass(self):
        start_pattern = [7,8,6,2,7,7,8,6,2,7]
        target_pattern = [7,8,6,2,6,7,8,6,8,2]
        permitted_transition_throws = []
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [7, 8, 6, 2, 7, 7, 8, 6, 2, 7], [7, 8, 6, 2, 6, 7, 8, 6, 8, 2],
        'Active [7, 6, 7, 8, 2][7, 6, 6, 8, 8]\nPassive [8, 2, 7, 6, 7][8, 2, 7, 6, 2]'
        ]
        self.assertEqual(output, answer)

    def test_no_transition_throws_needed_throwing_an_extra_pass(self):
        start_pattern = [7,8,6,2,6,7,8,6,8,2]
        target_pattern = [7,8,6,2,7,7,8,6,2,7]
        permitted_transition_throws = []
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [7, 8, 6, 2, 6, 7, 8, 6, 8, 2], [7, 8, 6, 2, 7, 7, 8, 6, 2, 7],
        'Active [7, 6, 6, 8, 8][7, 6, 7, 8, 2]\nPassive [8, 2, 7, 6, 2][8, 2, 7, 6, 7]'
        ]
        self.assertEqual(output, answer)

    def test_transition_throw_needed_but_not_available(self):
        start_pattern = [2,7,7,8,6,2,7,7,8,6] # 6 club why-not
        target_pattern = [7,7,7,8,2,7,7,7,2,6] # parsnip vs funky bookends
        permitted_transition_throws = [2,6,8] # need a 4 to transition
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = None
        self.assertEqual(output, answer)

    def test_transition_throw_needed(self):
        start_pattern = [2,7,7,8,6,2,7,7,8,6] # 6 club why-not
        target_pattern = [7,7,7,8,2,7,7,7,2,6] # parsnip vs funky bookends
        permitted_transition_throws = [4]
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [8, 6, 2, 7, 7, 8, 6, 2, 7, 7], [6, 7, 7, 7, 8, 2, 7, 7, 7, 2],
        'Active [8, 2, 7, 6, 7]4[7, 7, 2, 7, 2]\nPassive [6, 7, 8, 2, 7][6, 7, 8, 7, 7]'
        ]
        self.assertEqual(output, answer)




class FindingHijackTests(unittest.TestCase):

    def test_find_transitions_from_martins_one_count(self):
        hijacks_found = programming.generate_hijacks([7,7,7,7,2],[2,6,7,8]) # from martin's one count
        known_hijacks = 2 # funky bookends vs parsnip, two different ways.
        self.assertEqual(len(hijacks_found),known_hijacks)


    def test_find_transitions_from_maybe(self):
        hijacks_found = programming.generate_hijacks([7,2,7,8,6],[2,6,7,8]) # from maybe
        known_hijacks = 3 # popcorn vs 5 club why not, funky bookends vs parsnip and popcorn vs 5 club not why.
        self.assertEqual(len(hijacks_found),known_hijacks)

    def test_find_transitions_from_why_not(self):
        hijacks_found = programming.generate_hijacks([7,8,6,2,7],[2,6,7,8]) # from why not
        known_hijacks = 3 # funky bookends vs parsnip, popcorn vs 5 club why not and popcorn vs 5 club not why.
        self.assertEqual(len(hijacks_found),known_hijacks)

    def test_part_of_lisas_loop(self):
        hijacks_found = programming.generate_hijacks([7, 8, 6, 7, 2, 7, 7, 8, 6, 2],[2,6,7,8])
        known_hijacks = 2
        self.assertEqual(len(hijacks_found),known_hijacks)


if __name__ == "__main__":
    unittest.main()
