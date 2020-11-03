class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def to_dict(self):
        return {
          "firts_name": self.first_name,
          "last_name": self.last_name,
          "height_cm": self.weight_kg,
          "weight_hg": self.weight_kg,
        }

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def to_dict(self):
        player = super().to_dict()
        return player.update({
            "points": self.points,
            "rebounds": self.rebounds,
            "assists": self.assists,
        })


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def to_dict(self):
        player = super().to_dict()
        return player.update({
            "goals": self.goals,
            "yelow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
        })