import unittest
import transition_grid


class TransitionGridTests(unittest.TestCase):


    def test_can_find_lisas_loop(self):
        start_pattern = [7, 8, 6, 7, 2, 7, 7, 8, 6, 2]
        permitted_throws = [2,6,7,8]
        transitions_found = transition_grid.find_network_of_hijacks(
        start_pattern,permitted_throws
        )
        self.assertEqual(transitions_found, 11)

    def test_can_find_six_club_why_not_loop(self):
        start_pattern = [7,8,6,2,7]
        permitted_throws = [2,6,7,8]
        transitions_found = transition_grid.find_network_of_hijacks(
        start_pattern,permitted_throws,True,'whynot.xlsx'
        )
        self.assertEqual(transitions_found, 45)
        # note that this test may need to be changed if I fix the fact that's it's writting the same transition multiple times.

    def test_can_find_period_7_loop(self):
        start_pattern = [9, 4, 9, 7, 4, 2, 7]
        permitted_throws = [2,6,7,8,9]
        transitions_found = transition_grid.find_network_of_hijacks(
        start_pattern,permitted_throws
        )
        self.assertEqual(transitions_found, 8) # some double counting going on



if __name__ == "__main__":
    unittest.main()
