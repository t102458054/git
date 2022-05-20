from inheritance import Demo3


class Demo6(Demo3):
    def __init__(self):  # 子層__init__初始化函數覆寫掉父層的__init__
        super().__init__()  # 用超越函數在父層執行初始化
        self.k = 0


d4 = Demo6()
print(d4.i, d4.j, d4.k)
