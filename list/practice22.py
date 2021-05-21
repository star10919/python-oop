'''
종목명,종목코드를 입력받아서    종목명,종목코드 입력,출력,삭제,수정  완성
'''
class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'종목명 {self.name}, 종목코드 {self.code}'

    @staticmethod
    def del_element(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0Exit 1입력 2출력 3수정 4삭제')
            if menu == '0':
                print('종료')
                break
            elif menu == '1':
                    ls.append(Stock(input('종목명 '), input('종목코드')))
            elif menu == '2':
                for i in ls:
                    print(i.get_stock())
            elif menu == '3':
                code = input('수정할 종목코드: ')
                stock = Stock(input('수정 종목명: '), code)
                Stock.del_element(ls, code)
                ls.append(stock)

            elif menu == '4':
                stock = Stock(None, input('종목코드 '))
                stock.del_element(ls, stock.code)
            else:
                print('잘못 입력하였습니다.')
                continue


Stock.main()