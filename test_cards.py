from unittest.mock import MagicMock
from cards import *
import pytest


@pytest.mark.parametrize("card1Type,card2Type,Result",
                         [
                             ('A', '2', False),
                             ('5', '4', True),
                             ('2', 'A', True),
                             ('K', 'Q', True),
                             ('Jocker1', 'K', True),
                             ('K', 'Jocker2', False),
                             ('J', 'J', False),
                             ('Q', 'Q', False),
                             ('K', 'K', False)
                         ])
def test_CardGame_CompareCardTypes(card1Type, card2Type, Result):
    pickerMock = MagicMock()
    game = CardGame(pickerMock)

    res = game.CompareCardTypes(card1Type, card2Type)
    assert res == Result


@pytest.mark.parametrize("strongSign,cardOne,cardTwo,Result",
                         [
                             ('spades', 'A_clubs', '2_diamonds', False),
                             ('clubs', 'A_clubs', '2_diamonds', True),
                             ('diamonds', '5_diamonds', 'Jocker2', True),
                             ('spades', 'Jocker1', 'K_hearts', True),
                             ('hearts', 'Jocker1', 'A_hearts', False),
                         ])
def test_CardGame_IsBigger(strongSign, cardOne, cardTwo, Result):
    pickerMock = MagicMock()
    game = CardGame(pickerMock)
    game.StrongerSign = strongSign

    res = game.IsBigger(cardOne, cardTwo)
    assert res == Result


def test_CardGame_Play_WhenPlayerOnePicksBigger_GetsPoint():
    picker = CardPicker()
    picker.Pick = MagicMock()
    picker.Return = MagicMock()

    game = CardGame(picker)
    game.StrongerSign = 'clubs'
    game.TotalPointsNeeded = 10
    picker.Pick.side_effect = ['K_spades',
                               '5_hearts']  # first card, second card

    res = game.Play()

    assert res == ''  # We don't have winner yet since we set it to 10 points
    assert game.PlayerOnePoints == 1
    assert picker.Pick.call_count == 2
    picker.Return.assert_called_once()


def test_CardGame_Play_WhenPlayerPicksBigger_GetsPoint():
    picker = CardPicker()
    picker.Pick = MagicMock()
    picker.Return = MagicMock()

    game = CardGame(picker)
    game.StrongerSign = 'clubs'
    game.TotalPointsNeeded = 10
    picker.Pick.side_effect = ['Q_hearts',
                               'A_clubs']  # first card, second card

    res = game.Play()

    assert res == ''  # We don't have winner yet since we set it to 10 points
    assert game.PlayerTwoPoints == 1
    assert picker.Pick.call_count == 2
    picker.Return.assert_called_once()


def test_CardGame_Play_WhenPlayerOneWins_ReportWin():
    picker = CardPicker()
    picker.Pick = MagicMock()
    picker.Return = MagicMock()

    game = CardGame(picker)
    game.StrongerSign = 'clubs'
    game.TotalPointsNeeded = 2
    picker.Pick.side_effect = ['A_clubs',
                               'Q_hearts',
                               'K_diamonds',
                               '5_spades']  # 1 - first card, second card, 2 -  first card, second card

    res = game.Play()
    res = game.Play()

    assert res == 'Player One'
    assert game.PlayerOnePoints == 2
    assert picker.Pick.call_count == 4
    assert picker.Return.call_count == 2


def test_CardGame_Play_WhenPlayerTwoWins_ReportWin():
    picker = CardPicker()
    picker.Pick = MagicMock()
    picker.Return = MagicMock()

    game = CardGame(picker)
    game.StrongerSign = 'clubs'
    game.TotalPointsNeeded = 2
    picker.Pick.side_effect = ['Q_hearts',
                               'A_clubs',
                               '5_spades',
                               'K_diamonds']  # 1 - first card, second card, 2 -  first card, second card

    res = game.Play()
    res = game.Play()

    assert res == 'Player Two'
    assert game.PlayerTwoPoints == 2
    assert picker.Pick.call_count == 4
    assert picker.Return.call_count == 2
