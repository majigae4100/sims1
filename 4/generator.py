from iteration import Iteration

class Generator(Iteration):
    def __init__(self, i: int):
        super(Generator, self).__init__(i)

    def raise_to_the_degrees_F(self, number: int, max_degree: int):
        for i in range(max_degree):
            yield number ** self.I
            self.I += 1