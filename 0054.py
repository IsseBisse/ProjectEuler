from dataclasses import dataclass


class Card:
    SUITE_TO_SCORE = {"C": 0.1, "D": 0.2, "H": 0.3, "S": 0.4}
    VALUE_TO_SCORE = {str(num):num for num in range(2,11)}
    VALUE_TO_SCORE = {**VALUE_TO_SCORE, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, card_string):
        self.value = card_string[0]
        self.suite = card_string[1]

    def __str__(self):
        return f"{self.value}{self.suite}"

    def to_score(self):
        return self.VALUE_TO_SCORE[self.value] + self.SUITE_TO_SCORE[self.suite]

    def __gt__(self, other) -> bool:
        if not isinstance(other, Card):
            return NotImplemented

        return self.to_score() > other.to_score()

    def __lt__(self, other) -> bool:
        return not self.__gt__(other)

@dataclass
class Hand:
    def __init__(self, hand_string):
        self.cards = [Card(card_string) for card_string in hand_string.split(" ")]
        self.rank = self.rank_hand()

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def rand_hand(self):
        pass

    def __gt__(self, other) -> bool:
        

if __name__ == '__main__':
    h = Hand("5H 5C 6S 7S KD")
    print(h)