import random


class CardDeck(object):

    def __init__(self, cards=False, size=24, take_card=[]):
        self.cards = cards
        self.size = size
        self.take_card = take_card

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, __cards):
        self.__cards = ['As Pik', 'As Karo', 'As Trefl', 'As Kier', 'Król Pik', 'Król Karo', 'Król Trefl', 'Król Kier',
                        'Dama Pik',
                        'Dama Karo', 'Dama Trefl', 'Dama Kier', 'Jopek Pik', 'Jopek Karo', 'Jopek Trefl', 'Jopek Kier',
                        'Dziesiątka Pik', 'Dziesiątka Karo', 'Dziesiątka Trefl', 'Dziesiątka Kier', 'Dziewiątka Pik',
                        'Dziewiątka Karo', 'Dziewiątka Trefl', 'Dziewiątka Kier']
        return self.__cards

    def shuffle_cards(self, cards):
        return random.sample(self.__cards, len(cards))

    def draw_cards(self, cards, size=24, take_card=[]):
        if size > 0:
            take_card.append(cards[0])
            cards.pop(0)
            size = size - 1
        if len(take_card) > 2:
            return print(f'Twoje karty: {take_card}')

    def deal_out(self):
        cards_1 = player1.cards
        cards_1 = player1.shuffle_cards(cards_1)
        player1.draw_cards(cards_1)
        player1.draw_cards(cards_1)
        player1.draw_cards(cards_1)


player1 = CardDeck()
# cards_1 = player1.cards
# cards_1 = player1.shuffle_cards(cards_1)
# player1.draw_cards(cards_1)
player1.deal_out()
