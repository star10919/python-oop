class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'종목명 : {self.name} 종목코드 : {self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0Exit 1.create 2.read 3.update 4.delete ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('name '), input('종목코드 : ')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                code = input('수정할 종목코드: ')
                stock = Stock(input('수정 종목명: '), code)
                stock.del_element(ls, code)
                ls.append(stock)

            elif menu == '4':
                stock = Stock(None, input('종목코드 '))
                stock.del_element(ls, stock.code)
            else:
                print('wrong number')
                continue

Stock.main()