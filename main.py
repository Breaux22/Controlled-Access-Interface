#this is a controlled access entry system.


#check for correct username in database username_database.py
def get_username(uname):
    username_database = open("username_database.py", "r")
    read_username = username_database.read()
    if uname == '':
        print('Password or Username not recognized. Try again. \n'
              'If New User type "New User" in username slot. \n'
              'Enter Username below: ')
        get_username(input())
    elif uname == 'New User':
        print('Type New Username below: ')
        create_username(input())
    elif uname in read_username:
        print('Password: ')
        get_password(input())
    else :
        print('Password or Username not recognized. Try again. \n'
              'If New User type "New User" in username slot. \n'
              'Enter Username below: ')
        get_username(input())

#check for correct password in password_database.py
def get_password(pword):
    password_database = open("password_database.py", "r")
    read_password = password_database.read()
    if pword == '':
        print('Password or Username not recognized. Try again. \n'
              'If New User type "New User" in username slot. \n'
              'Enter Username below: ')
        get_username(input())
    if pword in read_password:
            access_granted()
    else:
        print('Password or Username not recognized. Try again. \n'
              'If New User type "New User" in username slot. \n'
              'Enter Username below: ')
        get_username(input())

#create new user password
def create_password(new_pword):
    with open("password_database.py", "w") as password_database:
        password_database.write('\n')
        password_database.write(new_pword)
    #password_database = open("password_database.py", "w")
    #password_database.write(new_pword)
    #password_database.close()
    print("Thank you for creating an account. \n"
          "Please enter your Username below: ")
    get_username(input())

#create new user username and saves to username_database.py
def create_username(new_uname):
    with open("username_database.py", "w") as username_database:
        username_database.write('\n')
        username_database.write(new_uname)
    #username_database = open("username_database.py", "w")
    #username_database.write(new_uname)
    #username_database.close()
    print("Type New Password below: ")
    create_password(input())

#final entry message
def access_granted():
    print("Access Granted. Please follow the link below. \n"
          "https://cat-bounce.com/")


print('Welcome, User. Please Enter your Username. \n'
      'If New User type "New User" in username slot. \n'
      'Username: ')
get_username(input())




