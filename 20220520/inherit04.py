from inheritance import Demo3


class Demo5(Demo3):
    def __init__(self):
        self.k = 0


d3 = Demo5
print(d3.i, d3.j, d3.k)
