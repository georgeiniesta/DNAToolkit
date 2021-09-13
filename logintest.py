import getpass

while(True):
    print ("Simple Python Login Tool ")
    print ("======================== ")
    username = input("Enter your username: ")
    password = getpass.getpass()

    with open('users.txt ') as file:
        for line in file:
            row = line.splitl('|')
            if ((username.lower()== row [2].lower and (password == row[3])):
                break
            else: 
                print("Incorrect password or username, Please try again... \n ")