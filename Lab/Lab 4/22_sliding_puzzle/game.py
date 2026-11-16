import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self):
        self.size = self.choose_size()
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()

    def choose_size(self):
        while True:
            print("Choose puzzle size:")
            print("1. 3x3")
            print("2. 4x4")
            print("3. 5x5")

            choice = input("Enter choice (1-3): ").strip()

            if choice == "1":
                return 3
            if choice == "2":
                return 4
            if choice == "3":
                return 5

            print("Invalid choice. Please enter 1, 2, or 3.")

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        elapsed = int(time.monotonic() - self.started)

        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")

        while True:
            self.display()

            if self.puzzle.solved():
                print("Solved!")
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key not in "wasd":
                print("Use W/A/S/D.")
                continue

            if self.puzzle.move(key):
                self.moves += 1
                print("Moved.")
            else:
                print("That move is not possible.")