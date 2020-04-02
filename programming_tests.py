import unittest
import programming


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
