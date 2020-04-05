import unittest
import programming

class FindTransitionsPeriod3sTests(unittest.TestCase):

    def test_no_transition_throws_needed_not_throwing_a_pass(self):
        start_pattern = [9,7,5] # holy grail
        permitted_throws = [2,5,7,8,9]
        output = programming.generate_hijacks(
        start_pattern, permitted_throws
        )
        answer = [[
        [5,9,7,5,9,7], [8,9,7,2,9,7],
        'Active [5, 7, 9][8, 7, 9]\nPassive [9, 5, 7][9, 2, 7]'
        ]]
        self.assertEqual(output, answer)

    def test_no_transition_throws_needed_throwing_an_extra_pass(self):
        start_pattern = [8,5,5,2,5,5] # holy grail
        permitted_throws = [2,5,8]
        output = programming.throw_extra_pass(
        start_pattern, 0, permitted_throws
        )
        answer = [[
        [8,5,5,2,5,5],[5,5,5,5,5,5],
        'Active [8, 5, 5][5, 5, 5]\nPassive [5, 2, 5][5, 5, 5]'
        ]]
        self.assertEqual(output, answer)



class FindTransitionsPeriod5sTests(unittest.TestCase):

    def test_no_transition_throws_needed_not_throwing_a_pass(self):
        start_pattern = [7,8,6,2,7] # 6 club whynot
        target_pattern = [7,8,6,2,6,7,8,6,8,2] # popcorn vs 5 club whynot
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
        start_pattern = [2,7,7,8,6] # 6 club why-not
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

class FindTransitionsPeriod7sTests(unittest.TestCase):

    def test_flip_needed_to_transition(self):
        # 9788827 TO 9797226 VS 9797888
        # [8298877]4[9926772] active transition
        # [8778298][8778998] passive transition


        start_pattern = [2,7,9,7,8,8,8]
        target_pattern = [9,7,9,7,2,8,6,9,7,9,7,8,2,8]
        permitted_transition_throws = [2,4,6,8]
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [8,8,2,7,9,7,8]*2, [8,9,7,9,7,2,8,6,9,7,9,7,8,2],
        'Active [8, 2, 9, 8, 8, 7, 7]4[9, 9, 2, 6, 7, 7, 2]' + '\n' + \
        'Passive [8, 7, 7, 8, 2, 9, 8][8, 7, 7, 8, 9, 9, 8]'
        ]
        self.assertEqual(output, answer)

    def test_another_flip_needed_to_transition(self):
        # 9968827 TO 9922497 VS 9968897
        # [8296879]4[9924792] active transition
        start_pattern = [2,7,9,9,6,8,8]
        target_pattern = [9,7,9,9,2,8,4,9,7,9,9,6,2,8]
        permitted_transition_throws = [2,4,6,8]
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [8,8,2,7,9,9,6]*2, [8,9,7,9,9,2,8,4,9,7,9,9,6,2],
        'Active [8, 2, 9, 6, 8, 7, 9]4[9, 9, 2, 4, 7, 9, 2]' + '\n' + \
        'Passive [8, 7, 9, 8, 2, 9, 6][8, 7, 9, 8, 9, 9, 6]'
        ]
        self.assertEqual(output, answer)


    def test_self_needed_to_transition(self):
        # 9797226 VS 9797888 TO 9788827
        # [9926772]6[9887782] active transition
        # [7789988][7782988] passive transition

        start_pattern = [9,7,9,7,2,8,6,9,7,9,7,8,2,8]
        target_pattern = [2,7,9,7,8,8,8]
        permitted_transition_throws = [2,4,6,8]
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [9, 7, 9, 7, 2, 8, 6, 9, 7, 9, 7, 8, 2, 8],
        [7, 9, 7, 8, 8, 8, 2, 7, 9, 7, 8, 8, 8, 2],
        'Active [9, 9, 2, 6, 7, 7, 2]6[9, 8, 8, 7, 7, 8, 2]' + '\n' + \
        'Passive [7, 7, 8, 9, 9, 8, 8][7, 7, 8, 2, 9, 8, 8]'
        ]
        self.assertEqual(output, answer)

    def test_another_self_needed_to_transition(self):
        # 9922497 VS 9968897 TO 9968827
        # [9924792]6[9687982] active transition goes up 1 club (hijack)
        start_pattern = [9,7,9,9,2,8,4,9,7,9,9,6,2,8]
        target_pattern = [2,7,9,9,6,8,8]
        permitted_transition_throws = [2,4,6,8]
        output = programming.find_transitions(
        start_pattern, target_pattern, permitted_transition_throws
        )
        answer = [
        [9,7,9,9,2,8,4,9,7,9,9,6,2,8],
        [7,9,9,6,8,8,2,7,9,9,6,8,8,2],
        'Active [9, 9, 2, 4, 7, 9, 2]6[9, 6, 8, 7, 9, 8, 2]' + '\n' + \
        'Passive [7, 9, 8, 9, 9, 6, 8][7, 9, 8, 2, 9, 6, 8]'
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
