from aoc import helper
import numpy as np

data = ["3,4,3,1,2"]
data = helper.get_puzzle_input(d=6, y=2021)
data = [int(x) for x in data[0].split(",")]

# Here I am changing the data format to an array with 9 items.
# The array indices represent a fish state.
# The array values are the number of fishes in that state.
# Counting the fishes is much easier this way,
# because we don't have to deal with an ever expanding gigantic list/array.
# It's just about increasing numbers in a fixed size array.
states_and_fishes = [0] * 9
for fish in data:
    fishes = data.count(fish)
    states_and_fishes[fish] = fishes

states_and_fishes = np.array(states_and_fishes)

days = 256

for d in range(1, days + 1):
    # Keep track of zero state fishes
    remember = states_and_fishes[0]
    # Clear zero state
    states_and_fishes[0] = 0
    # Shift the whole array to the left to decrease each fishes state by one.
    states_and_fishes = np.roll(states_and_fishes, -1)
    if remember:
        # Fishes that were in state zero previously will change to state 6
        states_and_fishes[6] += remember
        # All the fishes that have changed to state six will spawn new
        # fishes with state 8
        states_and_fishes[8] += remember
    print(f"Day {d}: {np.sum(states_and_fishes)} fishes.")

print(f"Puzzle answer: {np.sum(states_and_fishes)}")
