import unittest
import complete_the_siteswap


class ValidSoFarTests(unittest.TestCase):
    # Tests for the function complete_the_siteswap.valid_so_far

    def test_valid_partial_siteswaps_give_true(self):
        valid_partial_siteswaps = [[3,'?',5], [9,'?','?',3,1],
        [11,'?',7],['?','?','?',5],['?','?'],[5,6,'?'], [8,9,10]]
        output = [complete_the_siteswap.valid_so_far(i) for i in valid_partial_siteswaps]
        self.assertEqual(output, [True]*len(valid_partial_siteswaps))

    def test_valid_siteswaps_give_true(self):
        valid_siteswaps = [[3,4,5],[11,9,7,5,3,1],[11,0,1]]
        output = [complete_the_siteswap.valid_so_far(i) for i in valid_siteswaps]
        self.assertEqual(output, [True]*len(valid_siteswaps))

    def test_invalid_partial_siteswaps_give_false(self):
        invalid_partial_siteswaps = [[5,4,'?','?'], [8,'?','?','?',4], [3,'?',1], [2,'?','?',7]]
        output = [complete_the_siteswap.valid_so_far(i) for i in invalid_partial_siteswaps]
        self.assertEqual(output, [False]*len(invalid_partial_siteswaps))

    def test_invalid_siteswaps_give_False(self):
        invalid_siteswaps = [[4,3,2],[3,3,1],[8,5,6],[9,5,5,6],[2,3,3,7]]
        output = [complete_the_siteswap.valid_so_far(i) for i in invalid_siteswaps]
        self.assertEqual(output, [False]*len(invalid_siteswaps))


class FilterRatationsTests(unittest.TestCase):


    def test_remove_cycles_of_period_3(self):
        input = [[4,2,3],[2,3,4],[3,4,2]]
        output = complete_the_siteswap.filter_rotations(input)
        answer = [[4,2,3]]
        self.assertEqual(output, answer)

    def test_remove_cycles_of_period_5(self):
        siteswap = [9,7,5,3,1]
        input = [siteswap[i:]+siteswap[:i] for i in range(0,5)]
        output = complete_the_siteswap.filter_rotations(input)
        answer = [siteswap]
        self.assertEqual(output, answer)

    def test_remove_duplicates_but_not_anagrams(self):
        input = [[8,0,1],[7,2,3],[9,7,5],[1,8,0],[7,4,1],[7,1,4]]
        output = complete_the_siteswap.filter_rotations(input)
        answer = [[8,0,1],[7,2,3],[9,7,5],[7,4,1],[7,1,4]]
        self.assertEqual(output, answer)

class CompleteTests(unittest.TestCase):
    # Tests for the function complete_the_siteswap.complete

    def test_invalid_partial_siteswaps_gives_empty_list(self):
        invalid_partial_siteswaps = [[5,4,'?','?'], [8,'?','?','?',4], [3,'?',1], [2,'?','?',7]]
        output = [complete_the_siteswap.complete(i, list(range(10))) for i in invalid_partial_siteswaps]
        answer = [[] for i in invalid_partial_siteswaps]
        self.assertEqual(output, answer)

    def test_valid_siteswaps_give_one_solution(self):
        valid_siteswaps = [[3,4,5],[11,9,7,5,3,1],[11,0,1]]
        output = [complete_the_siteswap.complete(i, list(range(10))) for i in valid_siteswaps]
        answer = [[valid_siteswap] for valid_siteswap in valid_siteswaps]
        self.assertEqual(output, answer)

    def test_finds_all_ways_to_fill_one_gap(self):
        partial_siteswap = [5,'?',4]
        output = complete_the_siteswap.complete(partial_siteswap, list(range(10)))
        answer = [[5,i,4] for i in range(10) if i%3==0]
        self.assertEqual(output, answer)

    def test_finals_all_ways_to_fill_two_gaps(self):
        partial_siteswap = [4,4,'?','?']
        output = complete_the_siteswap.complete(partial_siteswap, list(range(10)))
        answer = [[4,4,i,j] for i in [0,4,8] for j in [0,4,8]] + \
                [[4,4,i,j] for i in [1,5,9] for j in [3,7]]
        output.sort()
        answer.sort()
        self.assertEqual(output,answer)

    def test_find_all_three_object_period_3_siteswaps_max_height_9(self):
        partial_siteswap = ['?']*3
        output = complete_the_siteswap.filter_rotations(
            complete_the_siteswap.complete(partial_siteswap, list(range(10)),3)
        )
        self.assertEqual(len(output),13)

    def test_find_all_three_object_period_5_siteswaps_max_height_9(self):
        partial_siteswap = ['?']*5
        output = complete_the_siteswap.filter_rotations(
            complete_the_siteswap.complete(partial_siteswap, list(range(8)),3)
        )
        # 89 according to juggling lab.
        self.assertEqual(len(output),89)
    def test_find_all_three_object_period_5_siteswaps_max_height_9_no_0s_or_2s(self):
        partial_siteswap = ['?']*5
        output = complete_the_siteswap.filter_rotations(
            complete_the_siteswap.complete(partial_siteswap, [1,3,4,5,6,7],3)
        )
        # 12 according to juggling lab.
        self.assertEqual(len(output),12)

    def test_find_all_seven_object_period_9_siteswaps_with_passes_selfs_and_heffs(self):
        partial_siteswap = ['?']*9
        output = complete_the_siteswap.filter_rotations(
            complete_the_siteswap.complete(partial_siteswap, [6,7,8],7)
        )
        # 10 according to juggling lab.
        self.assertEqual(len(output),10)

# print('Answer: {}'.format(answer))
# print('Output: {}'.format(output))


if __name__ == "__main__":
    unittest.main()
