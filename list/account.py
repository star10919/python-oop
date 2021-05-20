class Account(object):
    def __init__(self, depositor, accountnumber,balance):
        self.bankname = 'SC은행'
        self.depositor = depositor
        self.accountnumber = accountnumber
        self.balance = balance

    def get_account(self):
        return f'계좌번호 : 'randint(100,900)'-'randint(10,99)'-'randint(100000,999999)

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('입력하세요 0Exit 1입력 2계좌번호생성 ')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('예금주 : '), input('초기잔액 : ')))
            elif menu == '2':
                for i in ls:
                    print(i.get_account())
            elif menu == '3':
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

Account.main()