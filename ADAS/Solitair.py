import tkinter as tk
from tkinter import messagebox
import random
from enum import Enum
class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"
class Card:
    def __init__(self, value, suit):
        self.value = value  # 2-10, 11=Jack, 12=Queen, 13=King, 14=Ace
        self.suit = suit
    def to_string(self):
        val = {11: "J", 12: "Q", 13: "K", 14: "A"}.get(self.value, str(self.value))
        return f"{val}{self.suit.value}"
    def get_color(self):
        return "red" if self.suit in [Suit.HEARTS, Suit.DIAMONDS] else "black"
class WarGame:
    def __init__(self, root):
        self.root = root
        self.root.title("War Card Game")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="green")
        self.canvas.pack(fill="both", expand=True)
        # Game state
        self.deck = []
        self.player1_deck = []
        self.player2_deck = []
        self.player1_pile = []
        self.player2_pile = []
        self.initialize_deck()
        self.deal_cards()
        # UI elements
        self.player1_label = self.canvas.create_text(150, 50, text="Player 1: 26 cards", font=("Arial", 12))
        self.player2_label = self.canvas.create_text(450, 50, text="Computer: 26 cards", font=("Arial", 12))
        self.player1_card = None
        self.player2_card = None
        self.result_text = self.canvas.create_text(300, 300, text="Click 'Play Round' to start!", font=("Arial", 12))
        self.play_button = tk.Button(root, text="Play Round", command=self.play_round)
        self.play_button.pack(pady=10)
        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)
    def initialize_deck(self):
        self.deck = [Card(value, suit) for suit in Suit for value in range(2, 15)]
        random.shuffle(self.deck)
    def deal_cards(self):
        self.player1_deck = self.deck[:26]
        self.player2_deck = self.deck[26:]
        self.player1_pile = []
        self.player2_pile = []
    def play_round(self):
        if not self.player1_deck or not self.player2_deck:
            self.end_game()
            return
        # Draw cards
        p1_card = self.player1_deck.pop(0)
        p2_card = self.player2_deck.pop(0)
        self.player1_pile.append(p1_card)
        self.player2_pile.append(p2_card)
        # Update UI
        self.canvas.delete(self.player1_card, self.player2_card)
        self.player1_card = self.canvas.create_text(150, 200, text=p1_card.to_string(), font=("Arial", 16), fill=p1_card.get_color())
        self.player2_card = self.canvas.create_text(450, 200, text=p2_card.to_string(), font=("Arial", 16), fill=p2_card.get_color())
        self.canvas.itemconfig(self.player1_label, text=f"Player 1: {len(self.player1_deck) + len(self.player1_pile)} cards")
        self.canvas.itemconfig(self.player2_label, text=f"Computer: {len(self.player2_deck) + len(self.player2_pile)} cards")
        # Compare cards
        if p1_card.value > p2_card.value:
            self.canvas.itemconfig(self.result_text, text="Player 1 wins the round!")
            self.player1_deck.extend(self.player1_pile + self.player2_pile)
            self.player1_pile = []
            self.player2_pile = []
        elif p2_card.value > p1_card.value:
            self.canvas.itemconfig(self.result_text, text="Computer wins the round!")
            self.player2_deck.extend(self.player1_pile + self.player2_pile)
            self.player1_pile = []
            self.player2_pile = []
        else:
            self.canvas.itemconfig(self.result_text, text="War!")
            self.handle_war()
        # Shuffle decks if empty
        if not self.player1_deck and self.player1_pile:
            random.shuffle(self.player1_pile)
            self.player1_deck = self.player1_pile
            self.player1_pile = []
        if not self.player2_deck and self.player2_pile:
            random.shuffle(self.player2_pile)
            self.player2_deck = self.player2_pile
            self.player2_pile = []
        if not self.player1_deck or not self.player2_deck:
            self.end_game()
    def handle_war(self):
        if len(self.player1_deck) < 3 or len(self.player2_deck) < 3:
            self.end_game()
            return
        for _ in range(3):
            if self.player1_deck:
                self.player1_pile.append(self.player1_deck.pop(0))
            if self.player2_deck:
                self.player2_pile.append(self.player2_deck.pop(0))
        self.play_round()
    def end_game(self):
        p1_count = len(self.player1_deck) + len(self.player1_pile)
        p2_count = len(self.player2_deck) + len(self.player2_pile)
        if p1_count > p2_count:
            messagebox.showinfo("Game Over", "Player 1 wins the game!")
        elif p2_count > p1_count:
            messagebox.showinfo("Game Over", "Computer wins the game!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.play_button.config(state="disabled")
    def new_game(self):
        self.canvas.delete("all")
        self.initialize_deck()
        self.deal_cards()
        self.player1_label = self.canvas.create_text(150, 50, text="Player 1: 26 cards", font=("Arial", 12))
        self.player2_label = self.canvas.create_text(450, 50, text="Computer: 26 cards", font=("Arial", 12))
        self.result_text = self.canvas.create_text(300, 300, text="Click 'Play Round' to start!", font=("Arial", 12))
        self.play_button.config(state="normal")
        self.player1_card = None
        self.player2_card = None
if __name__ == "__main__":
    root = tk.Tk()
    game = WarGame(root)
    root.mainloop()
