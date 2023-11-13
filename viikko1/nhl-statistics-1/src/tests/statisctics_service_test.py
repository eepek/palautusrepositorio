import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Niinimaa", "PHI", 1, 2),
            Player("Nummelin", "WPG", 6, 25),
            Player("Rantanen", "COL", 35, 45),
            Player("Aho", "CAR", 30, 60),
            Player("Selänne", "WPG", 76, 23)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_with_valid_player_returns_correct_player(self):
        search_result = self.stats.search("Selänne")
        player = Player("Selänne", "WPG", 76, 23)
        # Added __eq__ to player class for easy comparison
        self.assertTrue(search_result, player)

    def test_seach_with_unkown_player_returns_none(self):
        self.assertIsNone(self.stats.search("Kurri"))

    def test_team_returns_all_team_players(self):
        players = self.stats.team("WPG")
        correct_players = [Player("Nummelin", "WPG", 6, 25), Player(
            "Selänne", "WPG", 76, 23)]
        self.assertEqual(players, correct_players)

    def test_top_players_returned_correctly(self):
        top_scorers = self.stats.top(4)
        playerstub_top_scorers = [
            Player("Selänne", "WPG", 76, 23),
            Player("Aho", "CAR", 30, 60),
            Player("Rantanen", "COL", 35, 45),
            Player("Nummelin", "WPG", 6, 25),
            Player("Niinimaa", "PHI", 1, 2)]
        self.assertEqual(top_scorers, playerstub_top_scorers)
