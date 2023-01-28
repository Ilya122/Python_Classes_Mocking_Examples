import random
from time import sleep


class CardPicker:
    def __init__(self):
        self.__cardTypes = ['A', '2', '3', '4', '5', '6', '7', '8',
                            '9', '10', 'J', 'Q', 'K']
        self.__cardSymbols = ['clubs', 'diamonds', 'hearts', 'spades']
        self.AllCards = ['Jocker1', 'Jocker2']
        for type in self.__cardTypes:
            for symbol in self.__cardSymbols:
                self.AllCards.append(f'{type}_{symbol}')
        self.PickedIndicies = []

    def Pick(self):
        maxCards = len(self.AllCards)
        if len(self.PickedIndicies) == maxCards:
            raise RuntimeError('Deck is empty')
        pickedIndex = random.randint(0, maxCards-1)
        while pickedIndex in self.PickedIndicies:
            pickedIndex = random.randint(0, maxCards-1)
        self.PickedIndicies.append(pickedIndex)
        return self.AllCards[pickedIndex]

    def Return(self, card):
        if not card in self.AllCards:
            raise IndexError('Trying to put card which doesnt exist')
        index = self.AllCards.index(card)
        if index not in self.PickedIndicies:
            raise IndexError('Trying to put card that wasnt picked')
        self.PickedIndicies.remove(index)

    def IsEmpty(self):
        maxCards = len(self.AllCards)
        return len(self.PickedIndicies) == maxCards


class CardGame():
    def __init__(self, cardPicker):
        self.CardPicker = cardPicker
        self.StrongerSign = random.choice(
            ['clubs', 'diamonds', 'hearts', 'spades'])
        self.PlayerOnePoints = 0
        self.PlayerTwoPoints = 0
        self.TotalPointsNeeded = 10
        print(f'Stronger sign is {self.StrongerSign}')

    def Play(self):
        cardOne = self.CardPicker.Pick()
        cardTwo = self.CardPicker.Pick()

        if(self.IsBigger(cardOne, cardTwo)):
            self.PlayerOnePoints += 1
            self.CardPicker.Return(cardTwo)
            print(f"Player one won the round with {cardOne} over {cardTwo}")
        elif(self.IsBigger(cardTwo, cardOne)):
            self.PlayerTwoPoints += 1
            self.CardPicker.Return(cardOne)
            print(f"Player Two won the round with {cardTwo} over {cardOne}")

        if(self.PlayerOnePoints == self.TotalPointsNeeded):
            return 'Player One'
        elif(self.PlayerTwoPoints == self.TotalPointsNeeded):
            return 'Player Two'
        return ''  # No Winner

    def IsBigger(self, card, otherCard):
        firstStronger = self.StrongerSign in card and not self.StrongerSign in otherCard
        if(firstStronger):
            return True
        otherStronger = self.StrongerSign in otherCard and not self.StrongerSign in card
        if otherStronger:
            return False

        cardType = card.split('_')[0]
        otherCardType = otherCard.split('_')[0]
        return self.CompareCardTypes(cardType, otherCardType)

    def CompareCardTypes(self, type, otherType):
        if type == otherType:
            return False
        strength = {'A': 1, '2': 2, '3': 3,
                    '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                    'Jocker1': 14, 'Jocker2': 14}
        return strength[type] > strength[otherType]