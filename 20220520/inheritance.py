from os import name


class Demo3:
    i = 0

    def __init__(self):
        self.j = 0
        Demo3.i += 1


class Demo4(Demo3):
    pass


if __name__ == '__main__':
    d1 = Demo3()
    print(d1.i, d1.j)
    d2 = Demo4()
    print(d2.i, d2.j)  # i,j被繼承到demo4
