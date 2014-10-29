import unittest

from bopitbot import bopitbot


class BopItGameTestCase(unittest.TestCase):
    """Test cases for BopItGame."""
    def setUp(self):
        self.commands = ['bop', 'twist', 'pull', 'spin', 'flick']
        self.game = bopitbot.BopItGame(self.commands)

    def test_init(self):
        self.assertEqual(self.game.commands, self.commands)
        self.assertEqual(self.game.points, 0)
        self.assertEqual(self.game.players, [])
        self.assertEqual(self.game.follower, None)
        self.assertEqual(self.game.command, None)
        self.assertEqual(self.game.answer, None)

    # def test_establish_twitter_connection(self):
    #     pass

    def test_initialize_round(self):
        self.game.points = 100
        self.game.players = ['Alice', 'Bob', 'Carl']
        self.game.initialize_round()
        self.assertEqual(self.game.points, 0)
        self.assertEqual(self.game.players, [])

    # def test_turn_valid(self):
    #     pass

    # def test_turn_expire(self):
    #     pass

    # def test_turn_incorrect(self):
    #     pass

    # def test_turn_other_account_correct(self):
    #     pass

    # def test_turn_other_account_incorrect(self):
    #     pass

    # def test_play(self):
    #     pass
