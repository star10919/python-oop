class Bmi(object):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmiindex(self):
        return self.weight / self.height ** 2 / 10000

    def bmiindex(self):
        score = int(self.bmiindex())
        index = ''
        if score >= 35:
            index = '초고도비만'
        elif score >= 30:
            index = '고도비만'
        elif score >= 25:
            index = '비만'
        elif score >= 23:
            index = '과체중'
        elif score >= 18.5:
            index = '정상'
        else:
            index = '저체중'

        return index

    @staticmethod
    def main():
        b = Bmi(int(input('키를 입력하세요')), int(input('체중을 입력하세요')))
        print(f'체지방 지수 : {b.bmiindex()}')


Bmi.main()