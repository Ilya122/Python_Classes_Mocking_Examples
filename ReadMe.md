# Info

This repo contains some examples for mocking capabilities and test writing for a simple game of cards. 

[Cards](cards.py) has the rules and definitions

[Test Cards](test_cards.py) contains the test definitions using ``pytest``.  

# Cards

The card game is a simple card by card game where each player gets a card and they compare it.  
From the 4 signs you get a strong sign which controls which of the 4 signs is the strongest and beats the other 3.  

The game contains one deck of cards, each time a player wins the loser returns the card and the winner discards it - giving more chances for "weaker" cards to beat cards next time.  
The joker is stronger then all cards but the stronger symbol.  

# Tests
Tests are written only for the ``CardGame`` class and check the rules that we've set up.  


---

This is only example for learning purposes, you may use this code if you'd like to anywhere.  