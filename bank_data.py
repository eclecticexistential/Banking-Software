import sys
import login_info
import bankingClass
import db

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
        return "Your balance is: %.2f" % account[4]

def add_to_balance(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        try:
            deposit = float(input("How much are you depositing?"))
        except ValueError:
            print("Use numbers only.")
            return add_to_balance(account)
        account[4] += deposit
        return account[4]

    else:
        sys.exit()

def make_transaction(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        try:
            withdraw = float(input("How much are you withdrawing?"))
        except ValueError:
            print("Use numbers only.")
            return make_transaction(account)
        if account[4] >= withdraw:
            account[4] -= withdraw
            return account[4]
        elif account[4] < withdraw:
            print("Insufficient funds.")

def get_info(account):
    bank_ID = id_bank()
    if bank_ID == 9999:
        data = "Account Number: {} \nName: {} \nSocial: {} \nAddress: {}\n".format(account[0],account[1],account[2],account[3])
        return data
    else:
        print("You do not have access to this information.")

def verify(data):
    while True:
        question = "Is '{}' correct? ".format(data)
        answer = str(input(question)).lower()
        if answer == 'no':
            data = str(input("Please provide the correct information."))
        elif answer == 'yes':
            new_info = data
            return new_info
            break



def check_soc(social):
    while True:
        social = str(social)
        if len(social) == 9:
            return social
            break
        elif len(social) >= 9:
            print("Social too long.")
            try:
                social = int(input("Social?"))
            except ValueError:
                print("Use only numbers.")
        elif len(social) < 9:
            print("A number or two is missing.")
            try:
                social = int(input("Social?"))
            except ValueError:
                print("Use numbers only.")

def banker_options():
    bank_ID = 9999
    #set up pin...
    options = str(input("Do you want to add a new customer?")).lower()
    if options == 'yes':
        first_name = verify(str(input("First Name?")))
        last_name = verify(str(input("Last Name?")))
        address = verify(str(input("Street Address?")))
        social = verify(check_soc(str(input("Social?"))))
        new_person = bankingClass.Person(first_name,last_name,social,address)
        new_account = new_person.create_account(bank_ID)
        return bank_options(new_account)
    elif options == 'no':
        name = str(input("Account name?"))
        account = db.check_db(name)
        return bank_options(account)
    else:
        print("Sorry, didn't quite get that.")
        return banker_options()

def login():
    entry = "closed"
    username = str(input("What is your username?"))
    if login_info.find_username(username) == True:
        try:
            password = str(input("What is your password?"))
        except ValueError:
            print("Cannot use all numbers.")
            return login()
        while entry == "closed":
            entry = login_info.find_password(username,password)
            if entry == "closed":
                print("Invalid login information. Try again.")
                return login()
            elif entry == "open":
                print("Welcome!")
                return banker_options()
    else:
        print("User not found. Try again.")
        counter = 0
        if counter < 3:
            return login()
        else:
            print("User does not exist. Contact Admin.")
            sys.exit()

login()