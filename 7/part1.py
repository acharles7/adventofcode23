from pathlib import Path
from collections import Counter

def find_winnings(data: list[str]) -> int:

    kinds = {
        (5, ): 7,
        (1, 4): 6,
        (2, 3): 5,
        (1, 1, 3): 4,
        (1, 2, 2): 3,
        (1, 1, 1, 2): 2,
        (1, 1, 1, 1, 1): 1,
    }
    cards = "AKQJT98765432"
    cards_strength = {card: strength for card, strength in zip(cards, range(len(cards), 0, -1))}

    def evaluate_hand(hand: list[str]):
        kind = kinds[tuple(sorted(Counter(hand[0]).values()))]
        return [(kind, cards_strength[card]) for card in hand[0]]

    hands = [hand.split() for hand in data]
    sorted_hands = sorted(hands, key=evaluate_hand)
    return sum(int(bid)*rank for (hand, bid), rank in zip(sorted_hands, range(1, len(hands)+1)))


if __name__ == '__main__':
    input_path = Path(__file__).parent / "data"
    input_data = input_path.read_text().splitlines()
    print(find_winnings(input_data))  # 248217452
