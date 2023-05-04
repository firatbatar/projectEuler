from time import time
start = time()


def find_value(card):
    values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return values[card]


def divide_hands(hands):
    hand1 = hands[0:14]
    hand1 = hand1.split(' ')
    hand2 = hands[15:]
    hand2 = hand2.split(' ')
    return [hand1, hand2]


def compare(hand1, hand2):
    if hand1.rank > hand2.rank:
        return 1
    elif hand1.rank < hand2.rank:
        return 2
    else:
        if hand1.rankCard > hand2.rankCard:
            return 1
        elif hand1.rankCard < hand2.rankCard:
            return 2
        else:
            while True:
                high1 = hand1.highest_card()
                high2 = hand2.highest_card()
                if high1.value > high2.value:
                    return 1
                elif high1.value < high2.value:
                    return 2
                else:
                    continue


class Card:
    def __init__(self, card):
        self.value = find_value(card[0])
        self.suit = card[1]

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.value != other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __le__(self, other):
        if self.value <= other.value:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        else:
            return False

    def __str__(self):
        return "{}{}".format(self.value, self.suit)


class Hand:
    def __init__(self, cards):
        self.cards = []
        for card in cards:
            self.cards.append(Card(card))
        self.cards.sort()
        self.cardsCopy = self.cards.copy()
        self.rank = None
        self.rankCard = None
        self.pairCards = None

        self.calculate_rank()

    def __str__(self):
        for card in self.cards:
            print(card, end=", ")
        print("\nRank:", self.rank, sep="")
        print("Rank card: ", self.rankCard, sep="")
        print("Pair cards: ", self.pairCards, sep="")
        return ""

    def calculate_rank(self):
        # Flush
        flush = True
        for i in range(0, 4):
            if self.cards[i].suit != self.cards[i+1].suit:
                flush = False

        # Pair
        close = False
        for i in range(0, 5):
            for j in range(0, 5):
                if i != j:
                    if self.cards[i].value == self.cards[j].value:
                        self.pairCards = [self.cards[i].value]
                        close = True
                        break
            if close:
                break
        # Royal Flush - 9
        royal = True
        for i in range(0, 5):
            if self.cards[i].value != i + 8:
                royal = False
                break
        if royal and flush:
            self.rank = 9
            self.rankCard = 12
            return

        # Straight Flush - 8
        straight = True
        for i in range(0, 4):
            if self.cards[i].value - self.cards[i+1].value != -1:
                straight = False
                break
        if straight and flush:
            self.rank = 8
            self.rankCard = self.cards[-1].value
            return

        # Four of a Kind - 7
        for i in range(0, 5):
            count = 0
            for j in range(0, 5):
                if i != j:
                    if self.cards[i].value == self.cards[j].value:
                        count += 1
            if count == 3:
                self.rank = 7
                self.rankCard = self.cards[i].value
                self.pairCards = None
                return

        # Full House - 6
        if self.pairCards:
            for i in range(0, 5):
                count = 0
                for j in range(0, 5):
                    if i != j:
                        if self.cards[i].value == self.cards[j].value:
                            count += 1
                if count == 2:
                    try:
                        self.pairCards.remove(self.cards[i].value)
                    except ValueError:
                        pass
                    if len(self.pairCards) == 1:
                        self.rank = 6
                        self.rankCard = self.cards[i].value
                        return

        # Flush - 5
        if flush:
            self.rank = 5
            self.rankCard = self.cards[-1].value
            return

        # Straight - 4
        if straight:
            self.rank = 4
            self.rankCard = self.cards[-1].value
            return

        # Three of a Kind - 3
        for i in range(0, 5):
            count = 0
            for j in range(0, 5):
                if i != j:
                    if self.cards[i].value == self.cards[j].value:
                        count += 1
            if count == 2:
                self.rank = 3
                self.rankCard = self.cards[i].value
                self.pairCards = None
                return

        # Pair Two - 2
        close = False
        if self.pairCards:
            for i in range(0, 5):
                for j in range(0, 5):
                    if self.cards[i].value == self.pairCards[0]:
                        break
                    else:
                        if i != j:
                            if self.cards[i].value == self.cards[j].value:
                                self.pairCards.append(self.cards[i].value)
                                self.pairCards.sort()
                                close = True
                                break
                if close:
                    break
            if len(self.pairCards) == 2:
                self.rank = 2
                self.rankCard = self.pairCards[1]
                return

        # One pair - 1
        if self.pairCards and len(self.pairCards) == 1:
            self.rank = 1
            self.rankCard = self.pairCards[0]
            return

        # High Card - 0
        self.rank = 0
        self.rankCard = self.cards[-1].value
        return

    def highest_card(self):
        # if self.cardsCopy[-1].value != self.rankCard:
        #     hc = self.cardsCopy.pop()
        #     return hc
        # else:
        #     self.cardsCopy.pop()
        #     hc = self.cardsCopy.pop()
        #     return hc
        hc = self.cardsCopy.pop()
        return hc


with open('../txt/p054_poker.txt', 'r') as file:
    hands1 = file.read()
    hands2 = hands1.split('\n')
hands3 = []
for i in hands2:
    hands3.append(divide_hands(i))
hands4 = []
for [i, j] in hands3:
    handi = Hand(i)
    handj = Hand(j)
    hands4.append([handi, handj])

answer = 0
for i, j in hands4:
    if compare(i, j) == 1:
        # if i.rank == j.rank:
            # print(i)
            # print(j)
        answer += 1
print(answer)


print("Time {:.2f}".format(time() - start))
