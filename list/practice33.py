import random

class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def to_string(self):
        return f'은행명 {self.BANK_NAME},' \
               f'이름 {self.name},' \
               f'계좌번호 {self.account_number},' \
               f'잔액 {self.money}'

    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append((str(random.randint(0, 9))))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account):
        for i, j in enumerate(ls):
            if j.account == account:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0종료 1계좌계설 2계좌목록 3입금 4출금 5계좌삭제')
            if menu == '0':
                print('종료')
                break
            elif menu == '1':
                ls.append(Account(input('이름'), Account.create_account_number(), input('잔액')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())
            elif menu == '3':
                account = input('입금할 계좌번호')
                money = input('입금액')
                for i, j in enumerate(ls):
                    if j.account == account:
                        replace = Account(j.name, j.account,
                                          int(j.money) + int(money))    #입금
                Account.del_account(ls, account)
                ls.append(replace)
            elif menu == '4':
                account = input('출금할 계좌번호')
                money = input('출금액')
                for i, j in enumerate(ls):
                    if j.account == account:
                        replace = Account(j.name, j.account,
                                      int(j.money) - int(money))    #출금
            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호'))
            else:
                print('wrong number')
                continue


Account.main()