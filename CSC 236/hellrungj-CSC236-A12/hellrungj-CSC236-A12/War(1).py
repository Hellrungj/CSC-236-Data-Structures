#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hellrungj
#
# Created:     02/10/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from Stack import Stack
from MyQueue import Queue
##random.shuffle(cardset) # might be useful to the dealer

class War:
    def __inti__(self):
        """possibly useful instance variables"""
        self.myCurrent_Card = 0        # my currently displayed card
        self.otherCurrent_Card = 0        # other currently displayed card
        self.currentState_TurnTracker = 0        # keeps track of the state of play
        self.dealingPile = Stack()
        self.myPayingPile = Stack()
        self.myStoragePile = Stack()
        self.otherPlayingPile = Stack()
        self.otherStoragePile = Stack()
        self.lootPile = Queue()
        self.otherlootpile = Queue()
    def add_dealingPile(self):
        """adds the shuffled decks of cards to the dealer's pile"""
        card = 0
        i = 0
        while i != 4:
            while card != 10:
                card = 0
                self.dealingPile.push(card)
                card +=1
            i + 1

    def deal(self):
        """deals out 25 cards from to each player's playing pile from shuffled dealers pile"""
        self.add_dealingPile()
        Dealing_Deck = self.dealingPile()
        while Dealing_Deck.size() != 25:
            self.myPayingPile.push(Dealing_Deck.top())
            self.Dealing_Deck.pop()
        while Dealing_Deck.size() != 0:
            self.otherPlayingPile.push(Dealing_Deck.top())
            self.Dealing_Deck.pop()

    def make_move(self):
        """initiates a round of play and communicates play-by-play during the round
    returns true when the game is still in play
    returns false when the game is over
    Communicates an appropriate message about whether the user beat the computer"""
        round = 0
        self.deal()
        self.move_my_loot()
        self.move_other_loot()
        self.move_my_storage()
        self.move_other_storage()
        while self.myPayingPile.size() != None and self.myStoragePile.size() != None and self.lootPile.size() != None:
            round += 1
            self.myCurrent_Card = self.myPayingPile.top()
            self.otherCurrent_Card = self.otherPlayingPile.top()


    def remove_my_card(self):
        """Precondition: myPlayingPile is not empty
    If it is not empty, the function removes a card from myPlayingPile,
    returning the stored value"""
        if self.myPayingPile.size() != None:
            self.myPayingPile.pop()

    def remove_other_card(self):
        """Precondition: otherPlayingPile is not empty
    If it is not empty, the function removes a card from otherPlayingPile,
    returning the stored value"""
        if self.otherPlayingPile.size() != None:
            self.otherPlayingPile.pop()

    def display_card(self):
        """displays a card on the screen and returns the value"""
        display = []
        usercard=self.myCurrent_Card.top()
        display.append(usercard)
        computercard=self.otherCurrent_Card.top()
        display.append(computercard)
        print display
        return display

    def I_declair_War(self):
        """If two cards are the same ir does this step to find to wins and if not does it again until someone wins"""
        myC_one = self.myCurrent_Card()
        self.remove_my_card()
        self.myCurrent_Card = self.myPayingPile.top()
        myC_Two = self.myCurrent_Card()
        self.remove_my_card()
        self.myCurrent_Card = self.myPayingPile.top()
        myC_Three= self.myCurrent_Card()
        self.remove_my_card()
        self.myCurrent_Card = self.myPayingPile.top()
        myC_Four = self.myCurrent_Card()
        self.remove_my_card()
        #----------------------------
        otherC_one = self.remove_my_card()
        self.remove_other_card()
        self.otherCurrent_Card = self.otherPlayingPile.top()
        otherC_Two = self.remove_my_card()
        self.remove_other_card()
        self.otherCurrent_Card = self.otherPlayingPile.top()
        otherC_Three = self.remove_my_card()
        self.remove_other_card()
        self.otherCurrent_Card = self.otherPlayingPile.top()
        otherC_Four = self.remove_my_card()
        self.remove_other_card()

        Mytotal = myC_one + myC_Two + myC_Three + myC_Four
        othertotal = otherC_one + otherC_Two + otherC_three + otherC_Four

        if Mytotal == othertotal:
            print "War!"
            self.I_declair_War()
        elif Mytotal > othertotal:
            print "Human Win!"
        else:
            print "Computer Win!"
    def compare_cards(self):
        """compares myCurrent to otherCurrent and behaves appropriately"""
        if self.myCurrent_Card() == self.otherCurrent_Card():
            print "War"
            self.I_declair_War()
        elif self.myCurrent_Card() < self.otherCurrent_Card():
            print "Computer Win!"
            self.otherlootpile.enqueue(self.myCurrent_Card)
        else:
            print "Human Win!"
            self.lootPile.enqueue(self.otherCurrent_Card)
    def move_my_loot(self):
        """moves everything from lootPile to myStoragePile"""
        while self.lootPile.size() == None:
            self.myStoragePile.push(self.lootPile.dequeue())

    def move_other_loot(self):
        """moves everything from lootPile to otherStoragePile"""
        while self.otherlootpile.size() == None:
            self.otherStoragePile.push(self.otherlootpile.dequeue())
    def move_my_storage(self):
        """moves everything from myStoragePile to myPlayingPile"""
        while self.myStoragePile.size() == None:
            self.myPayingPile.push(self.myStoragePile.top())
            self.myPayingPile.pop()

    def move_other_storage(self):
        """moves everything from otherStoragePile to otherPlayingPile"""
        while self.otherStoragePile.size() == None:
            self.otherPlayingPile.push(self.otherStoragePile.top())
            self.otherStoragePile.pop()
