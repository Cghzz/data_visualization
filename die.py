from random import randint
class Die():
    '''标识一个骰子的类'''
    def __init__(self,sides=6):
        #骰子默认6面
        self.num_sides=sides

    def roll(self):
        #返回一个位于1和筛子面数之间的随机值
        return  randint(1,self.num_sides)
