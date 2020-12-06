import unittest
from app.src.player import *


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Player 1")
        self.player_2 = Player("Player 2")



    def test_player_has_name(self):
        self.assertEqual("Player 1", self.player_1.name)

    def test_player_has_default_blank_choice(self):
        self.assertEqual("blank_choice", self.player_1.choice)

    def test_player_makes_choice(self):
        player_make_choice(self.player_1, "rock")
        self.assertEqual("rock", self.player_1.choice)

    def test_play_janken_p1rock_p2scissors(self):
        player_make_choice(self.player_1, "rock")
        player_make_choice(self.player_2, "scissors")
        self.assertEqual("Player 1 has defeated Player 2!", play_janken(self.player_1, self.player_2))

    def test_play_janken_p1rock_p2rock(self):
        player_make_choice(self.player_1, "rock")
        player_make_choice(self.player_2, "rock")
        self.assertEqual('It\'s a draw! Play again.' , play_janken(self.player_1, self.player_2))

    def test_play_janken_p2scissors_p1paper(self):
        player_make_choice(self.player_1, "paper")
        player_make_choice(self.player_2, "scissors")
        self.assertEqual("Player 2 has defeated Player 1!", play_janken(self.player_1, self.player_2))

    def test_return_error_message(self):
        player_make_choice(self.player_1, "nonsense")
        player_make_choice(self.player_2, "I like chocolate")
        self.assertEqual("Error. Please only enter /'rock/', \'paper\' or \'scissors\'.", play_janken(self.player_1, self.player_2))