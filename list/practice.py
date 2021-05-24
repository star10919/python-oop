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
    def main():
        ls = []
        while 1:
            menu = input('0Exit 1입력 2출력 3삭제 4수정')
            if menu == '0':
                print('종료')
                break
            elif menu == '1':
                    ls.append(Stock(input('종목명 '), input('종목코드')))
            elif menu == '2':
                for i in ls:
                    print(i.get_stock())
            elif menu == '3':
                del_name = input('삭제할 종목명 ')
                # 입력받은 종목명이랑 리스트의 종목명이랑 같은 게 있는지 비교
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        #삭제

                        del ls[i]
            elif menu == '4':
                edit_name = input('수정할 종목명 ')
                edit_info = Stock(input('수정종목명 '), input('수정종목코드 '))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)
            else:
                print('잘못 입력하였습니다.')
                continue


Stock.main()