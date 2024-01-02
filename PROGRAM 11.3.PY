class PowerOfTwoIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = 2 ** self.current
            self.current += 1
            return result

# Example usage:
power_of_two_iter = PowerOfTwoIterator(0, 5)
for value in power_of_two_iter:
    print(value)
