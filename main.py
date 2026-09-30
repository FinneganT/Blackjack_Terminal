import random

RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
SUIT = ["Spades", "Hearts", "Clubs", "Diamonds"]
STARTING_BALANCE = 100
def build_deck():
    deck = [(ranks, suit) for ranks in RANKS for suit in SUIT]
    random.shuffle(deck)
    return deck

def card_value(rank):
    if rank in ("J", "Q", "K"):
        return 10
    if rank == "A":
        return 11
    return int(rank)
def hand_value(hand):
    total = sum(card_value(rank) for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
def show(hand, hide_first = False):
    if hide_first:
        return "[hidden], " + ", ".join(f"{r} of {s}" for r, s in hand[1:])
    return ", ".join(f"{r} of {s}" for r, s in hand)

def ask_bet(balance):
    while True:
        raw = input(f"Place your bet (1-{balance})").strip()
        if raw.isdigit() and 1 <= int(raw) <= balance:
            return int(raw)
        print("Invalid bet. Enter a whole number within your balance")

def play_round(balance):
    bet = ask_bet(balance)
    deck = build_deck()

    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

def main():
    build_deck()

if __name__ == "__main__":
    main()