import db

class Person(object):
    def __init__(self,first_name,last_name,social,address,balance=0,activity="",pin_number=0000):
        self.first_name = first_name
        self.last_name = last_name
        self.social = social
        self.address = address
        self.balance = balance
        self.activity = activity
        self.pin_number = pin_number

    def create_account(self,bank_ID):
        virtID = db.get_virtual_ID()
        account_num = db.get_account()
        self.full_name = self.first_name, self.last_name
        self.account_info = db.get_accounts(virtID, account_num, self.full_name, self.social, self.address,self.balance,bank_ID)
        print("Account saved.")