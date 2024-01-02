class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Example usage:
my_string = "Hello, World!"
string_iterator = StringIterator(my_string)
for char in string_iterator:
    print(char)
