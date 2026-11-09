"""Print the Collatz sequence starting at 27 and the number of steps to reach 1."""


def collatz_sequence(start):
    """Return the Collatz sequence from start down to 1, inclusive."""
    sequence = [start]
    n = start
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(27)
    for number in sequence:
        print(number)
    # Steps are transitions between numbers, so one fewer than the entries.
    steps = len(sequence) - 1
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
