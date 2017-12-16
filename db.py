import random
import sys

num_words = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m',0,1,2,3,4,5,6,7,8,9,'n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
num_only = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

def get_virtual_ID():
    iter = 11
    accountComp = ""
    while iter > 0:
        digitComp = random.choice(num_words)
        accountComp += str(digitComp)
        iter -= 1
    return accountComp

def get_account():
    iter = 11
    accountHuman = ""
    while iter > 0:
        digitHuman = random.choice(num_only)
        accountHuman += str(digitHuman)
        iter -= 1
    return accountHuman

def get_accounts(virtID,account_num,full_name,social,address,balance, bank_ID):
    issues = 0
    account_info = dict()
    bank_accounts = dict()
    if bank_ID == 9999:
        for i in bank_accounts:
            if i == virtID:
                while i == virtID:
                    try:
                        virtID = get_virtual_ID()
                    finally:
                        if i == virtID:
                            print("Unable to create new Virtual ID. Contact admin.")
                            issues += 1
                            break
            if bank_accounts[i][0] == account_num:
                while bank_accounts[i][0] == account_num:
                    try:
                        account_num = get_account()
                    finally:
                        if bank_accounts[i][0] == account_num:
                            print("Unable to create new Account Number. Contact Admin.")
                            issues += 1
                            break
        if issues == 0:
            account_info[0] = account_num
            account_info[1] = full_name
            account_info[2] = social
            account_info[3] = address
            account_info[4] = balance
            bank_accounts[virtID] = account_info
            return bank_accounts
    else:
        print("You do not have access to this information.")
        sys.exit()