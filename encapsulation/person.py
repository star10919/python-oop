class Person():
    def __init__(self, name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address

    def age(self):
        return 2021 - self.birth

    @staticmethod
    def main():
        p=Person(input('이름 : '), int(input('출생년도 : ')), input('주소 : '))
        print(f'이름 : {p.name}', f'나이 : {p.age()}', f'주소 : {p.address}')

Person.main()