import os

AllUsersPath = "/etc/passwd"
AllGroupsPath = "/etc/group"

def about():
    os.system("clear")
    print("""\nUSERs & GROUPs Maneger
          
          the options of this code are simple 
          
          @@ first ADD User 
          this option gives you some sub options like 
          to change user id , to change primary group id to an existing group 
          
          @@ secound modify user
          this has many sub options like
          1- change user id 
          2- adding the user as a member to existing group
          3- change the primary group to existing one 
          4- adding a comment to the user interface
          5- to change the shell and this option also have some options too like
                A) to know your shell
                B) change to nologin shell in /sbin/nologin
                C) change to login bash shell /bin/bash
          6- to exit modification
          
          @@ third delete user 
          this option delete existing user and give a warning if the primary group can't be changed
          
          @@ fourth list users
          lists all the names of the local users
          
          @@ fifth ADD a group
          this option have some sub options like and the group must not be existing
          if i want to change group ID while creating 
          
          @@ sixth Modify Group
          this option have some sub options like 
          1- change group ID must not exist befor 
          2- change group name must not exist befor too
          
          @@ seventh Delete Group 
          this option force group delete even if the group is a primary group of a user 
          
          @@ eighth List Groups  
          ths option list the names of all local existing groups
          
          @@ ninth Disable User 
          this option Disable the user from loging even if he writes the correct password
          
          @@ tenth Enable User 
          this option Enable the user to login if he was disabled
          
          @@ eleventh Password Change 
          this option changes the password of an existing user any password is okay
          
          @@ twelfth About 
          this option shows you this menu 
          
          @@ thirteenth EXIT
          this option exits the Application""")

def Modify_table_Group():
    print ("1)To change the group ID write                   1")
    print ("2)To change the group name write                 2")  

def shell_table ():
    print ("1)if you want to know your shell write           1")
    print ("2)if you want nologin shell write                2")
    print ("3)if you want bash shell write                   3")  

def Modify_table ():
    print("1) to change user ID [1000 - 60000] write        1")
    print("2) to add the user to a group write              2") 
    print("3) to change user primary group write            3") 
    print("4) to add a comment to the user write            4") 
    print("5) to change user shell write                    5") 
    print("6) to exit modification write                    6")

def get_input(prompt, default_value):
    user_input = input(prompt).strip()
    return user_input if user_input else default_value

def search(Item , Index , FilePath) :
    with open(FilePath, 'r') as file:
        Items = [line.split(':')[Index] for line in file]
        if Item in Items:
            return 'found'
        else :
            return 'not found'

def add_user():
    while True:
        user = get_input("\nPlease enter the new user name: ", 'N')
        if user.isalnum() and user != 'N': 
            SearchValue = search (user , 0 , AllUsersPath)
            if SearchValue == 'found':
                print("This user already exists. Try again.")
                continue
            else:
                command = "sudo useradd "
                while True :
                    print("\nFor default user ID press Enter")
                    UID = get_input ("Enter user ID [1000 - 60000]: " , 'N') 
                    if UID.isnumeric and UID != 'N' :  
                        SearchValue = search (UID , 2 , AllUsersPath)
                        if SearchValue == 'found' :
                            print("This user ID already exists. Try again.")
                            continue
                        else :
                            command = command + '-u ' + UID + ' '
                            break
                    elif UID == 'N' :
                            break
                    else:
                        print("You must enter a valid user ID.")
                        continue
                while True :
                    print("\nFor default group name press Enter")
                    GName = get_input ("Enter Group name must exists: " , 'N') 
                    if GName.isnumeric and GName != 'N' :  
                        SearchValue = search (GName , 0 , AllGroupsPath)
                        if SearchValue == 'not found' :
                            print("This Group do not exists. Try again.")
                            continue
                        else :
                            command = command + '-G ' + GName + ' '
                            break
                    elif GName == 'N' :
                            break
                    else:
                        print("You must enter a valid group name.")
                        continue
                command += user
                os.system(command)
                print(f"User {user} added successfully.")
                break
        else:
            print("You must enter a valid username.")
            continue

def modify_user():
    while True:
        user = get_input("\nPlease enter the user name: ", 'N')
        SearchValue = search(user, 0, AllUsersPath)
        if user.isalnum() and user != 'N' and SearchValue == "found":
            while True:
                Modify_table()
                mod = input("Enter your option here: ").strip()
                if mod.isnumeric() and 1 <= int(mod) <= 6:
                    mod = int(mod)
                    command = "sudo usermod "

                    if mod == 1:
                        while True:
                            UID = get_input("\nEnter user ID [1000 - 60000]: ", 'N')
                            if UID.isdigit() and 1000 <= int(UID) <= 60000:
                                SearchValue = search(UID, 2, AllUsersPath)
                                if SearchValue == 'found':
                                    print("This user ID already exists. Try again.")
                                else:
                                    command += f'-u {UID} '
                                    command += user
                                    os.system(command)
                                    print(f"User {user} modified successfully.")
                                    break
                            else:
                                print("You must enter a valid user ID (1000-60000).")
                    elif mod == 2:
                        while True:
                            GName = get_input("\nEnter group name (must exist): ", 'N')
                            SearchValue = search(GName, 0, AllGroupsPath)
                            if SearchValue == 'not found':
                                print("This group does not exist. Try again.")
                            else:
                                command += f'-aG {GName} '
                                command += user
                                os.system(command)
                                print(f"User {user} modified successfully.")
                                break
                    elif mod == 3:
                        while True:
                            GName = get_input("\nEnter group name (must exist): ", 'N')
                            SearchValue = search(GName, 0, AllGroupsPath)
                            if SearchValue == 'not found':
                                print("This group does not exist. Try again.")
                            else:
                                command += f'-g {GName} '
                                command += user
                                os.system(command)
                                print(f"User {user} modified successfully.")
                                break
                    elif mod == 4:
                        comment = input("Please enter your comment: ")
                        command = command + ' -c ' + f"'{comment}'" + ' '
                        command += user
                        os.system(command)
                        print(f"User {user} modified successfully.")
                    elif mod == 5:
                        while True:
                            shell_table()
                            shell = input("\nPlease enter your option: ").strip()
                            if shell.isnumeric() and 1 <= int(shell) <= 3:
                                shell = int(shell)
                                if shell == 1:
                                    with open(AllUsersPath, 'r') as file:
                                        for line in file:
                                            if line.startswith(user + ":"):
                                                current_shell = line.split(':')[-1].strip()
                                                print(f"Current shell for {user}: {current_shell}")
                                                break
                                elif shell == 2:
                                    command += ' -s /sbin/nologin '
                                    command += user
                                    os.system(command)
                                    print(f"User {user} modified successfully.")
                                elif shell == 3:
                                    command += ' -s /bin/bash '
                                    command += user
                                    os.system(command)
                                    print(f"User {user} modified successfully.")
                                break
                            else:
                                print("Invalid input. Please enter a number (1-3).")

                    elif mod == 6:
                        break
                else:
                    print("Invalid input. Please enter a number (1-6).")
            break
        else:
            print(f"You must enter a valid username. '{user}' is not a local user. Try again.")

def delete_user ():
    while True:
        user = get_input("\nPlease enter the user name: ", 'N')
        SearchValue = search(user, 0, AllUsersPath)
        if user.isalnum() and user != 'N' and SearchValue == "found":
            os.system(f"sudo userdel -r {user}")
            print(f"User {user} has been deleted successfuly")
            break
        else:
            print(f"You must enter a valid username. '{user}' is not a local user. Try again.")

def list_users ():
    os.system(f"cut -d : -f 1 {AllUsersPath}")

def add_group ():
    while True:
        GName = get_input("\nEnter new group name (must not exist): ", 'N')
        SearchValue = search(GName, 0, AllGroupsPath)
        if SearchValue == 'not found':
            command = "sudo groupadd "
            while True :
                print("\nFor default group ID press Enter")
                GID = get_input ("Enter group ID [1000 - 60000]: " , 'N') 
                if GID.isnumeric and GID != 'N' :  
                    SearchValue = search (GID , 2 , AllGroupsPath)
                    if SearchValue == 'found' :
                        print("This group ID already exists. Try again.")
                    else :
                        command = command + '-g ' + GID + ' '
                        break
                elif GID == 'N' :
                        break
                else:
                    print("You must enter a valid group ID.")
            command += GName
            os.system(command)
            print(f"User {GName} added successfully.")
            break
        else:
            print("This group already exist. Try again.")

def modify_group():
    while True:
        GName = get_input("\nPlease enter the group name: ", 'N')
        SearchValue = search(GName, 0, AllGroupsPath)
        if GName.isalnum() and GName != 'N' and SearchValue == "found":
            while True:
                Modify_table_Group()
                mod = input("Enter your option here: ").strip()
                if mod.isnumeric() and 1 <= int(mod) <= 6:
                    mod = int(mod)
                    command = "sudo groupmod "
                    if mod == 1:
                        while True:
                            GID = get_input("\nEnter group ID [1000 - 60000]: ", 'N')
                            if GID.isdigit() and 1000 <= int(GID) <= 60000:
                                SearchValue = search(GID, 2, AllGroupsPath)
                                if SearchValue == 'found':
                                    print("This group ID already exists. Try again.")
                                else:
                                    command += f'-g {GID} '
                                    command += GName
                                    os.system(command)
                                    print(f"Group {GName} modified successfully.")
                                    break
                            else:
                                print("You must enter a valid group ID (1000-60000).")
                    elif mod == 2:
                        while True:
                            newName = get_input("\nEnter group new name (must not exist): ", 'N')
                            SearchValue = search(newName, 0, AllGroupsPath)
                            if SearchValue == 'found':
                                print("This group name already exist. Try again.")
                            else:
                                command += f'-n {newName} '
                                command += GName
                                os.system(command)
                                print(f"group {GName} changed to {newName} successfully.")
                                break
                    break
                else:
                    print("Invalid input. Please enter a number (1-2).")
            break
        else:
            print(f"You must enter a valid group name. '{GName}' is not a local group. Try again.")

def delete_group ():
    while True:
        GName = get_input("\nPlease enter the group name: ", 'N')
        SearchValue = search(GName, 0, AllGroupsPath)
        if GName.isalnum() and GName != 'N' and SearchValue == "found":
            os.system(f"sudo groupdel -f {GName}")
            print(f"group {GName} has been deleted successfuly")
            break
        else:
            print(f"You must enter a valid group name. '{GName}' is not a local group. Try again.")

def list_groups ():
    os.system(f"cut -d : -f 1 {AllGroupsPath}")

def disable_user():
    while True:
        user = get_input("\nPlease enter the user name: ", 'N')
        SearchValue = search(user, 0, AllUsersPath)
        if user.isalnum() and user != 'N' and SearchValue == "found":
            os.system(f"sudo usermod -L {user}")
            print(f"User {user} has been Disabled successfuly")
            break
        else:
            print(f"You must enter a valid username. '{user}' is not a local user. Try again.")

def enable_user():
    while True:
        user = get_input("\nPlease enter the user name: ", 'N')
        SearchValue = search(user, 0, AllUsersPath)
        if user.isalnum() and user != 'N' and SearchValue == "found":
            os.system(f"sudo usermod -U {user}")
            print(f"User {user} has been Enabled successfuly")
            break
        else:
            print(f"You must enter a valid username. '{user}' is not a local user. Try again.")

def change_password():
    while True:
        user = get_input("\nPlease enter the user name: ", 'N')
        SearchValue = search(user, 0, AllUsersPath)
        if user.isalnum() and user != 'N' and SearchValue == "found":
            while True :
                passwd = get_input("Enter the new password: " , 'N')
                if passwd != 'N':
                    os.system(f'echo "{user}:{passwd}"  | sudo chpasswd')
                    print(f"the password of user {user} has changed to {passwd} successfuly")
                    break
                else:
                    print("please Enter the password don't skip") 
            break
        else:
            print(f"You must enter a valid username. '{user}' is not a local user. Try again.")

while True:
    print("Welcome to our app")
    print("1) To add a user, write                        1")
    print("2) To modify a user, write                     2")
    print("3) To delete a user, write                     3")
    print("4) To list users, write                        4")
    print("5) To add a group, write                       5")
    print("6) To modify a group, write                    6")
    print("7) To delete a group, write                    7")
    print("8) To list groups, write                       8")
    print("9) To disable a user, write                    9")
    print("10) To enable a user, write                    10")
    print("11) To change password of a user, write        11")
    print("12) To see about program, write                12")
    print("13) To exit, write                             13")

    try:
        Entry = int(input("Enter your option here: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if Entry == 1:
        add_user()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break
    elif Entry == 2:
        modify_user()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 3:
        delete_user()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break
    
    elif Entry == 4:
        list_users()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 5:
        add_group()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 6:
        modify_group()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 7:
        delete_group()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 8:
        list_groups()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 9:
        disable_user()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 10:
        enable_user()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 11:
        change_password()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break

    elif Entry == 12:
        about()
        while(1):
            ask = input("To quit, enter Q\nTo resume, enter R\n: ").strip().upper()
            if ask == 'R':
                break
            elif ask == 'Q':
                break
            else:
                print("Please enter a valid option (Q or R).")
        if ask == 'R':
            continue
        elif ask == 'Q':
            break
    
    elif Entry == 13:
        break

    else:
        print("Option not implemented yet.") 

    