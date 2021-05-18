import threading


class GradeConstructor:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return  self.kor + self.eng +  self.math

    def avg(self):
        return self.sum() / 3

if __name__ == '__main__':
    g = GradeConstructor(80, 90, 100)
    print(g.sum())
    print(g.avg())
