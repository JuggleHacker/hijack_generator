import unittest
import siteswap_states


class SiteswapStatesTests(unittest.TestCase):

    def test_ground_state_three_object_patterns(self):
        ground_state_patterns = [[3],[4,4,1],[5,3,1],[4,2,3]]
        output = [siteswap_states.state(pattern) for pattern in ground_state_patterns]
        answer = [[1,1,1]]*len(ground_state_patterns)
        self.assertEqual(answer, output)

    def test_ground_state_five_object_patterns(self):
        ground_state_patterns = [[5],[6,4,5],[6,6,6,6,1],[6,4]]
        output = [siteswap_states.state(pattern) for pattern in ground_state_patterns]
        answer = [[1,1,1,1,1]]*len(ground_state_patterns)
        self.assertEqual(answer, output)

    def test_shower_states_before_high_throw(self):
        shower_patterns = [[5,1],[7,1],[9,1]]
        output = [siteswap_states.state(pattern) for pattern in shower_patterns]
        answer = [[1,1,0,1], [1,1,0,1,0,1],[1,1,0,1,0,1,0,1]] # according to jugglewiki
        self.assertEqual(answer, output)

    def test_shower_states_before_high_throw(self):
        shower_patterns = [[1,5],[1,7],[1,9]]
        output = [siteswap_states.state(pattern) for pattern in shower_patterns]
        answer = [[1,0,1,0,1], [1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,1]] # according to jugglewiki
        self.assertEqual(answer, output)

    def test_excited_siteswaps(self):
        excited_patterns = [[8,0,1], [5,6,1],[7,7,1]]
        output = [siteswap_states.state(pattern) for pattern in excited_patterns]
        answer = [[1,0,1,0,0,1],[1,1,1,0,1],[1,1,1,0,1,1]]
        self.assertEqual(output,answer)

class MakeAThrowTests(unittest.TestCase):

    def test_make_a_high_throw_in_shower(self):
        ground_state_patterns = [(5,[1,1,0,1]), (7,[1,1,0,1,0,1]),(9,[1,1,0,1,0,1,0,1])]
        output = [siteswap_states.make_a_throw(pattern[0],pattern[1]) for pattern in ground_state_patterns]
        answer = [[1,0,1,0,1], [1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,1]]
        self.assertEqual(answer, output)

    def test_throw_771(self):
        states_passed_through = [[1,1,1,0,1,1],[1,1,0,1,1,0,1],[1,0,1,1,0,1,1],[1,1,1,0,1,1]]
        first_state = siteswap_states.state([7,7,1])
        second_state = siteswap_states.make_a_throw(7,first_state)
        third_state = siteswap_states.make_a_throw(7,second_state)
        fourth_state = siteswap_states.make_a_throw(1,third_state)
        output_states = [first_state,second_state,third_state,fourth_state]
        self.assertEqual(states_passed_through,output_states)

if __name__ == "__main__":
    unittest.main()
