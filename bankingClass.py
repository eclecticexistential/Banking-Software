import db
import sys
import login_info

def id_bank():
    try:
        bank_ID = int(input("What is your bank identification?"))
    except ValueError:
        print("That ID is invalid.")
        return id_bank()
    if bank_ID == bank_ID:
        return bank_ID
    else:
        print("Please contact admin.")
        sys.exit()

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


def bank_options(account):
    while True:
        answer = input(
            "Type Q to quit, AB for account balance, AD for account deposit, AW for account withdraw, or AI for account details.").upper()
        if answer == "AB":
            print(get_account_balance(account))
        elif answer == "AD":
            add_to_balance(account)
        elif answer == "AW":
            make_transaction(account)
        elif answer == "AI":
            print(get_info(account))
        elif answer == "Q":
            print("Have a nice day!")
            sys.exit()


def get_account_balance(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        return "Your balance is: %.2f" % account.balance

def add_to_balance(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        deposit = int(input("How much are you depositing?"))
        if deposit > 0:
            account.balance += deposit
    return account.balance

def make_transaction(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        withdraw = int(input("How much are you withdrawing?"))
        if account.balance > withdraw:
            account.balance -= withdraw
        elif account.balance < withdraw:
            print("Insufficient funds.")
    return account.balance

def get_info(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        info = account.account_info
        for i in info:
            data = "\nVirtual ID: {} \nAccount Number: {} \nName: {} \nSocial: {} \nAddress: {}\n".format(i,info[i][0],
                                                                ' '.join(info[i][1]),info[i][2],info[i][3])
            return data
    else:
        print("You do not have access to this information.")

def verify(data):
    question = "Is '{}' correct?".format(data)
    answer = str(input(question)).lower()
    while answer == 'no':
        data = str(input("Please provide the correct information."))
        verify(data)
        break
    if answer == 'yes':
        return data

def banker_options():
    bank_ID = id_bank()
    #set up pin...
    options = str(input("Do you want to add a new customer?")).lower()
    if options == 'yes':
        first_name = str(input("First Name?"))
        verify(first_name)
        last_name = str(input("Last Name?"))
        verify(last_name)
        address = str(input("Address?"))
        verify(address)
        social = str(input("Social?"))
        if len(social) < 7:
            print("Not enough numbers.")
            verify(social)
        if len(social) > 8:
            print("Numbers only, please.")
            verify(social)
        elif len(social) != 7:
            print("Invalid social. Contact Admin.")
            banker_options()
        new_person = Person(first_name,last_name,social,address)
        new_person.create_account(bank_ID)
        return bank_options(new_person)
    elif options == 'no':
        name = str(input("Account name?"))
        account = db.check_db(name)
        return bank_options(account)
    else:
        print("Sorry, didn't quite get that.")
        return banker_options()

def login():
    entry = "closed"
    try:
        username = str(input("What is your username?"))
        password = str(input("What is your password?"))
    except ValueError:
        print("Cannot use all numbers.")
        return login()
    while entry == "closed":
        entry = login_info.find_username(username,password)
        if entry == "closed":
            print("Invalid login information. Try again.")
            return login()
        elif entry == "open":
            print("Welcome!")
            return banker_options()

login()

def pin_number(account):
    tries = 0
    try:
        pin_number = int(input("What is your pin number?"))
    except ValueError:
        print("That pin is invalid.")
        tries += 1
        if tries < 4:
            return pin_number(account)
        else:
            print("Goodbye.")
            sys.exit()
    if pin_number == account.pin_number:
        return pin_number


def atm_options(account):
    entry = 0
    while entry == 0:
        pin_number(account)
        entry += 1
        break
    if entry > 0:
        while True:
            return bank_options(account)
            break