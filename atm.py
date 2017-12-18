import sys

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