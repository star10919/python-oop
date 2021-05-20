class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        self.kor + self.eng + self.math

    def avg(self):
        self.sum() / 3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        else:
            grade = 'F학점'

        return grade

if __name__ == '__main__':
    g = Grade(int(input('국어점수 : ')), int(input('영어점수 : ')), int(input('수학점수 : ')))
    print(f'합계 : {g.sum()}')
    print(f'평군 : {g.avg()}')
    print(f'학점 : {g.get_grade()}')
