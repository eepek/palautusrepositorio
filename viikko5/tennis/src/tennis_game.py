class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_for_player_1 = 0
        self.score_for_player_2 = 0
        self.point_difference, self.leader = self.get_point_difference_and_leader()
        self.deuce_points = ["Forty", "Fifty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.score_for_player_1 = self.score_for_player_1 + 1
        else:
            self.score_for_player_2 = self.score_for_player_2 + 1

    def get_string_value_for_score(self, score: int):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        else:
            return "Fifty"

    def is_game_at_tie(self):
        if self.score_for_player_1 == self.score_for_player_2:
            return True

        return False

    def is_there_winner(self):
        if self.is_leader_in_win_points():
            return self.point_difference >= 2

        return False

    def update_leader(self):
        self.point_difference, self.leader = self.get_point_difference_and_leader()

    def is_leader_in_win_points(self):
        return self.get_string_value_for_score(max(self.score_for_player_1, self.score_for_player_2)) == "Fifty"

    def are_players_in_deuce_points(self,  player1_points, player2_points):
        return player1_points in self.deuce_points and player2_points in self.deuce_points

    def get_point_difference_and_leader(self):
        return (abs(
            self.score_for_player_1 - self.score_for_player_2),
            "player1" if self.score_for_player_1 > self.score_for_player_2 else "player2")

    def get_score(self):
        player1_score = self.get_string_value_for_score(
            self.score_for_player_1)
        player2_score = self.get_string_value_for_score(
            self.score_for_player_2)
        self.update_leader()

        if self.is_game_at_tie():
            if self.are_players_in_deuce_points(player1_score, player2_score):
                return "Deuce"
            else:
                return f"{self.get_string_value_for_score(self.score_for_player_1)}-All"

        if self.are_players_in_deuce_points(player1_score, player2_score):
            if self.is_there_winner():
                return f"Win for {self.leader}"

            return f"Advantage {self.leader}"

        if self.is_there_winner():
            return f"Win for {self.leader}"

        return f"{player1_score}-{player2_score}"
