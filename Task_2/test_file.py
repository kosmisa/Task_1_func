#Cases
# 1 - Beggining of the match
# 2 - Exact match
# 3 - closest match that is less than offset
# 4 - when offset is beyond range
# 5 - Negative offset
# 6 - Single entry
# 7 - Empty list

import unittest
from Task_1.game_score import get_score

class TestGetScore(unittest.TestCase):

    def setUp(self):
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 3, "score": {"home": 1, "away": 0}},
            {"offset": 6, "score": {"home": 1, "away": 1}},
            {"offset": 10, "score": {"home": 2, "away": 1}},
            {"offset": 15, "score": {"home": 2, "away": 2}},
            {"offset": 20, "score": {"home": 3, "away": 5}},
        ]

    def test_offset_at_beginning(self):
        home, away = get_score(self.game_stamps, 0)
        self.assertEqual((home, away), (0, 0))
        
    def test_exact_match(self):
        home, away = get_score(self.game_stamps, 10)
        self.assertEqual((home, away), (2, 1))

    def test_closest_match_less_than_offset(self):
        home, away = get_score(self.game_stamps, 7)
        self.assertEqual((home, away), (1, 1))

    def test_offset_beyond_range(self):
        home, away = get_score(self.game_stamps, 20)
        self.assertEqual((home, away), (3, 5))

    def test_negative_offset(self):
        with self.assertRaises(ValueError):
            get_score(self.game_stamps, -1)

    def test_single_entry(self):
        single_stamp = [{"offset": 0, "score": {"home": 0, "away": 0}}]
        home, away = get_score(single_stamp, 5)
        self.assertEqual((home, away), (0, 0))

    def test_empty_list(self):
        empty_stamps = []
        with self.assertRaises(IndexError):
            get_score(empty_stamps, 5)

if __name__ == '__main__':
    unittest.main()
    