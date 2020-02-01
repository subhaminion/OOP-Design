from player import Player


class Cricket(object):
    def __init__(self, who_bats_first):
        self.who_bats_first = who_bats_first
        self.players = {
            "A": Player(0),
            "B": Player(0)
        }
        self.game_stat = {
            "A": 0,
            "B": 0
        }

    def update_game_stat(self):
        new_stat = {
            "A": self.game_stat.get("A") + self.players.get("A").strike,
            "B": self.game_stat.get("B") + self.players.get("B").strike
        }
        self.game_stat.update(new_stat)

    def reset_game_stat(self):
        self.game_stat.update({
            "A": 0,
            "B": 0
        })
        self.players.get("A").reset_player_score()
        self.players.get("B").reset_player_score()

    def innings(self, player):
        print(player + " is Batting.")

        for i in range(6):
            self.players.get("A").make_strike()
            self.players.get("B").make_strike()
            self.update_game_stat()
            if self.players.get("A").strike != self.players.get("B").strike:
                self.players.get(player).player_score_update(self.players.get(player).strike)
                print("A throws " + str(self.players.get("A").strike) + " B throws " + str(self.players.get("B").strike) + ". Player " + str(player) + " score is " + str(self.players.get(player).score))
            
            if self.players.get("A").strike == self.players.get("B").strike:
                print("A throws " + str(self.players.get("A").strike) + " B throws " + str(self.players.get("B").strike) + ". Player " + str(player) + " is Out!")
                self.reset_game_stat()
                break

    def declare_winner(self):
        if self.game_stat.get("A") > self.game_stat.get("B"):
            print("Game winner is A!")
        else:
            print("Game winner is B!")

    def game_start(self):
        number_of_games = 3
        for i in range(number_of_games):
            print("Game No:" + str(i + 1))
            self.innings(self.who_bats_first)
            if self.who_bats_first == "A":
                self.innings("B")
            else:
                self.innings("A")
        self.declare_winner()


ck = Cricket("B")
ck.game_start()
