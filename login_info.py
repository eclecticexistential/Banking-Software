
usernames = {"jones@hotmail.com":"12345"}

def find_username(current_user):
    for username in usernames:
        if current_user == username:
            return True
        else:
            return False

def find_password(current_user,password):
    for username in usernames:
        if current_user == username:
            counter = 1
            while counter <= 3:
                if password != usernames[username]:
                    if counter == 1:
                        print("{} attempts remaining.".format(3-counter))
                    if counter > 1:
                        print("{} attempt remaining.".format(3-counter))
                    password = str(input("What's your password?"))
                    counter += 1
                    if password == usernames[username]:
                        continue
                elif password == usernames[username]:
                    entry = "open"
                    return entry
            if counter > 3:
                print("Goodbye.")