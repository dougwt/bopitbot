import random
import time

from .models import *


class BopItGame:
    def __init__(self, commands):
        self.commands = commands
        self.followers = []

        # round variables
        self.initialize_round()

        # turn variables
        self.follower = None
        self.command = None
        self.answer = None

    def play(self, start=0, stop=24, turn=10, bonus=2):
        """Start the game."""
        self.establish_twitter_connection()
        self.initialize_round()

        while start < time.time() and stop > time.time():
            self.turn(turn, bonus)

    def establish_twitter_connection(self):
        """Start worker bots."""
        for commmand in self.commands:
            # launch worker
            pass

    def initialize_round(self):
        """Initialize round variables."""
        self.points = 0
        self.players = []

    def turn(self, limit_time, bonus_time):
        """Play a turn."""
        start_time = time.time()
        self.waiting = True

        # choose random follower
        self.follower = random.choice(self.followers)

        # choose random command
        self.command = random.choice(self.commands)

        elapsed_time = time.time() - start_time

        while self.waiting and elapsed_time < limit_time:
            if self.answer:
                if self.answer == self.command:
                    # correct answer

                    # add follower to players list
                    self.players.append(self.follower)

                    # add points
                    self.points += 1
                    if elapsed_time < bonus_time:
                        self.points += 1

                else:
                    # incorrect answer

                    # subtact points from follower leaderboard score

                    # add points to players' leaderboard scores

                    # reinitialize points and players list
                    self.initialize_round()

                    # tweet failure message
                    self.waiting = False

            elapsed_time = time.time() - start_time


def main():
    game = BopItGame(commands)
    game.play()
