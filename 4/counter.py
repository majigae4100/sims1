from iteration import Iteration


class Counter(Iteration):
    def __init__(self, max_number: int, i: int):
        self.MaxNumber = max_number
        super().__init__(i)

    def __iter__(self):
        self.I = 0
        return self

    def __next__(self):
        self.I += 1
        if self.I > self.MaxNumber:
            raise StopIteration
        return self.I
