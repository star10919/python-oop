#종목명, 종목코드 while문

class Stock(object):
    def __init__(self, stockname, stockcode):
        self.stockname = stockname
        self.stockcode = stockcode

    def get_stock(self):
        return f'종목명 : {self.stockname}, 종목코드 : {self.stockcode}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0Exit 1입력 2출력 ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('종목명 : '), input('종목코드 : ')))
            elif menu == '2':
                for i in ls:
                    print(f'{i.get_stock()})')
            elif menu == '3':
                del_name = input('삭제할 이름:')
                for i,j in enumerate(ls):
                    if j.name == del_name:
                        del ls(i)


Stock.main()