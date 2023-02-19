#=====importing libraries===========
from datetime import datetime
from os.path import exists

# Function to allow a new user to registered by admin
def reg_user():
    while True:
            while True:
                # Take new username
                new_user = input("Please enter the new username: ")
                with open("user.txt", 'r', encoding='utf-8') as f:
                    # Create list of existing usernames
                    users = []
                    for line in f.readlines():
                        users.append(line.split(',')[0])
                    # Check if username is already used, print error message if already used
                    if new_user in users:
                        print("This user name is already in use, please try a different username.")
                    else:
                        break
            new_pass = input("Please enter the new password: ")
            confirm_pass = input("Please confirm the new password: ")

            # If the passwords match append user.txt with the new name and password
            if new_pass == confirm_pass:
                with open("user.txt", 'a', encoding='utf-8') as f:
                    f.write(f"\n{new_user}, {new_pass}")
                    # Prints successful registration message and a line break
                    print(f"{break_line}\nRegistration successful.\n{break_line}")
                    break

            # If the passwords do not match ask the user if they would like to exit or try again
            else:
                again = input('''The new password and confirmation password did not match. 
Please enter 'e' to exit this section or any key to try again: ''').lower()
                if again == 'e':
                    break
                else:
                    pass
    return


# Function to display stats from user.txt and tasks.txt
def disp_stats():
    # If the reports haven't been generated, generate the reports
    if exists('user_overview') == False:
        gen_rep()
    # open user_overview.txt and task_overview.txt and store the entries
    with open("user_overview.txt", "r", encoding='utf-8') as f:
        user_stats = f.read()
    with open("task_overview.txt", "r", encoding='utf-8') as f:
        task_stats = f.read()
    # Print the number of contents of each txt file with title and break lines
    return print(f'''{break_line[:40]}[Task statistics]{break_line[:40]}
{task_stats}
{break_line[:40]}[User statistics]{break_line[:40]}
{user_stats}
''')

# Function to add a new task for a user
def add_task():
    # Take user's inputs
        task_user = input("Please enter the username of the person the task is assigned to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter a description of the task: ")
        task_due_date = input("Please enter the due date of the task in the format dd mmm yyyy: ")

        # Find today's date and store in dd,mmm,yyyy format
        today_date = datetime.today()
        assigned_date = today_date.strftime("%d %b %Y")

        # Write user input's, assigned date and 'No' to tasks.txt
        with open("tasks.txt","a", encoding='utf-8') as f:
            f.write(f"\n{task_user}, {task_title}, {task_description}, {assigned_date}, {task_due_date}, No")

        # Confirm to user the task has been added
        return print(f"\nTask successfully added.\n{break_line}")


# Function to view all tasks in tasks.txt
def view_all():
    # Open tasks.txt and reads each line
    with open("tasks.txt","r", encoding='utf-8') as f:
        data = f.readlines()

    # Splits each item in line of the tasks.txt and prints the data in an easy to read format
    output = ""
    for line in data:
        split_data = line.split(", ")
        # split_data[5].strip() used as some entries had '\n' at the end
        output += f'''{break_line}
Assigned to:     {split_data[0]}
Task:            {split_data[1]}
Date assigned:   {split_data[3]}
Due date:        {split_data[4]}
Task complete:   {split_data[5].strip()}
Task description: 
 {split_data[2]} 
'''
    # Add dividing line to last task and print the tasks
    output += break_line
    return print(output)


# Funtion to view and edit tasks assigned to person logged in
def view_mine():
    # Open tasks.txt and reads each line
    with open("tasks.txt", "r", encoding='utf-8') as f:
        data = f.readlines()

    # Splits each item in line of the tasks.txt and prints the data in an easy to read format with a unique task number, starting from 1
    output = ""
    # enumerate to start from 1 rather than 0
    for pos, line in enumerate(data, 1):
        split_data = line.split(", ")
        # Checks if the task is assigned to the logged in username
        if split_data[0] == username:
            # split_data[5].strip() used as some entries had '\n' at the end
            output += f'''{break_line[:40]}[Unique task number: {pos}]{break_line[:40]}
Assigned to:     {split_data[0]}
Task:            {split_data[1]}
Date assigned:   {split_data[3]}
Due date:        {split_data[4]}
Task complete:   {split_data[5].strip()}
Task description: 
{split_data[2]} 
'''
    # If there are no tasks assigned to the username a message is printed, otherwise the assigned tasks are printed
    if len(output) == 0:
        print(f"{break_line}\nNo tasks are assigned to your username.\n{break_line}")
        return
    else:
        # Add dividing line to last task and print the task(s)
        output += break_line
        print(output)
    
    # Allow the user to choose to amend a task or return to the main menu
    while True:
        task_num = int(input("Please enter the unique task number you would like to amend or enter -1 to return to the main menu: "))
        # print error message if task_num  is less than -1 or greater than lenght of data
        if task_num  < -1 or task_num  > len(data):
            print('Invalid option selected. Please try again')
            continue
        # Exit to main menu if -1 is entered
        elif task_num  == -1:
            return
        # -1 from task_num to give position of task (enumerate starts from 1 for user ease), store the data to be edited in a variable
        else:
            task_pos = task_num - 1
            edit_data = data[task_pos]

            # Allow the user to choose to mark the task complete, edit the task or return to the previous menu 
            while True:
                choice = int(input('''Enter 1 to mark this task complete
Enter 2 to edit this task
Enter -1 to return to the previous menu
: '''))
                
                # Return to previous menu
                if choice == -1:
                    break

                # Mark task complete
                elif choice == 1:
                    # Split the task
                    split_task = edit_data.split(', ')
                    # Check if task already marked complete and print message if so
                    if split_task[-1].strip().lower() == 'yes':
                        print(f'{break_line}\nThis task has already been marked as complete.\n{break_line}')
                        break
                    # If task not completed, change last entry to 'Yes', update data variable with joined task elements, write to tasks.txt, print success message
                    else:
                        split_task[-1] = 'Yes'
                        data[task_pos] = ', '.join(split_task)
                        with open("tasks.txt","w", encoding='utf-8') as f:
                            [f.write(line) for line in data]
                        print(f'{break_line}\nTask successfully marked as complete.\n{break_line}')
                        break
                # Edit a task if it's not complete
                elif choice == 2:
                    # Split the task 
                    split_task = edit_data.split(', ')

                    # If task already completed return to menu above
                    if split_task[-1].strip().lower() == 'yes':
                        print(f'{break_line}\nThis task has been completed and can no longer be edited.\n{break_line}')
                        continue
                    # Otherwise, User selects what to edit
                    else:
                        edit_choice = int(input('''Enter 1 to amend "Assigned to" for this task
Enter 2 to amend "Due date" for this task
Enter -1 to return to the previous menu
: '''))
                        # If 1 is entered - update 'Assigned to' with user input, update data variable with joined task elements, write to tasks.txt, print success message
                        if edit_choice == 1:
                            edit_assigned = input('Please enter the username to whom this task is to be assigned: ')
                            split_task[0] = edit_assigned
                            data[task_pos] = ', '.join(split_task)
                            with open("tasks.txt","w", encoding='utf-8') as f:
                                [f.write(line) for line in data]
                            print(f'{break_line}\nTask successfully edited.\n{break_line}')
                            break

                        # If 2 is entered - update 'Due date' with user input, update data variable with joined task elements, write to tasks.txt, print success message 
                        elif edit_choice == 2:
                            edit_assigned = input('Please enter the new due date (dd mmm yyyy): ')
                            split_task[4] = edit_assigned
                            data[task_pos] = ', '.join(split_task)
                            with open("tasks.txt","w", encoding='utf-8') as f:
                                [f.write(line) for line in data]
                            print(f'{break_line}\nTask successfully edited.\n{break_line}')
                            break

                        # Return to previous menu if -1 entered
                        elif edit_choice == -1:
                            break
                        # print error message and ask for input again
                        else:
                            print('Invalid input, please try again')
                            continue
                # print error message and ask for input again 
                else:
                    print('Invalid input, please try again')
                    continue


# Function to generate task and user overview reports
def gen_rep():
    # Generate task report
    # open and store tasks.txt in task_data
    with open("tasks.txt","r", encoding='utf-8') as f:
        task_data = f.readlines()
    
    # Total number of tasks
    total_tasks = len(task_data)
    
    # Create 'total' counters and empty dictionary
    total_completed = 0
    total_uncompleted = 0
    total_overdue = 0
    user_dict = {}
    # Loop through task data and split each line
    for line in task_data:
        split_line = line.split(', ')
        
        # Create dictionary key (username the task is assigned to '-total'), if it doesn't already exist and add 1 to the value (initalising with 0)
        user_dict[f'{split_line[0]}-total'] = user_dict.get(f'{split_line[0]}-total', 0) + 1
        
        # If task completed add one to total_completed
        if split_line[-1].strip().lower() == 'yes':
            total_completed += 1
            # Create dictionary key (username the task is assigned to '-completed'), if it doesn't already exist and add 1 to the value (initalising with 0)
            user_dict[f'{split_line[0]}-completed'] = user_dict.get(f'{split_line[0]}-completed', 0) + 1
        
        else:
            # Otherwise add one to total uncomlpleted
            total_uncompleted += 1
            # Create dictionary key (username the task is assigned to '-uncompleted'), if it doesn't already exist and add 1 to the value (initalising with 0)
            user_dict[f'{split_line[0]}-uncompleted'] = user_dict.get(f'{split_line[0]}-uncompleted', 0) + 1

            # Check if the task is overdue and add one to total_overdue
            if (datetime.today().date()) > (datetime.strptime(split_line[4], "%d %b %Y").date()):
                total_overdue += 1
                # Create dictionary key (username the task is assigned to '-overdue'), if it doesn't already exist and add 1 to the value (initalising with 0)
                user_dict[f'{split_line[0]}-overdue'] = user_dict.get(f'{split_line[0]}-overdue', 0) + 1

    
    # Calculate percentage of incomplete tasks
    per_incomplete = (total_uncompleted/total_tasks) * 100

    # Calculate percentage of overdue tasks
    per_overdue = (total_overdue/total_tasks) * 100

    # write task information to task_overview.txt
    with open("task_overview.txt", "w", encoding="utf-8") as f:
        f.write(f'''Total number of tasks: {total_tasks} 
Total number of completed tasks: {total_completed}
Total number of uncompleted tasks: {total_uncompleted}
Total number of overdue tasks: {total_overdue}
Percentage of incomplete tasks: {per_incomplete:.2f}%
Percentage of overdue tasks: {per_overdue:.2f}%''')
    
    
    # Generate user report
    # open and store user.txt in user_data
    with open("user.txt", "r", encoding='utf-8') as f:
        user_data = f.readlines()
    
    # Total number of users
    total_users = len(user_data)

    # Generate list of each username from user_dict
    list_users = []
    for key in user_dict:
        if 'total' in key:
            list_users.append((key.split('-'))[0])
    
    # Generate stats for each user from user_dict in easy to read format, if key doesn't exist initialise key at 0 
    user_stats = ''
    for user in list_users:
        user_stats += f'''{break_line[:40]}[User: {user}]{break_line[:40]}
Total number of tasks assigned to user: {user_dict[f'{user}-total']}
Percentage of the total tasks that have been assigned to user: {(user_dict.get(f'{user}-total', 0) / total_tasks) * 100:.2f}%
Percentage of user's tasks which have been completed: {(user_dict.get(f'{user}-completed', 0) / user_dict[f'{user}-total']) * 100:.2f}%
Percentage of user's tasks which are uncompleted: {(user_dict.get(f'{user}-uncompleted', 0) / user_dict[f'{user}-total']) * 100:.2f}%
Percentage of user's tasks which are overdue: {(user_dict.get(f'{user}-overdue', 0) / user_dict[f'{user}-total']) * 100:.2f}%
'''

    # write user information to user_overview.txt
    with open("user_overview.txt", "w", encoding="utf-8") as f:
        f.write(f'''Total number of users: {total_users}
Total number of tasks: {total_tasks}
{user_stats}''')

    # print message to show reports have been generated
    return print(f'{break_line}\nReports successfully generated\n{break_line}')


#====Login Section====
while True:
    # Take user inputs
    username = input("Username: ")
    password = input("Password: ")

    # Opens user.txt file and creates a dictionary of each username and password
    with open("user.txt", 'r', encoding='utf-8') as f:
        user_data = f.readlines()
        logins = {}
        for line in user_data:
            split_user = line.split(', ')
            # .strip() to remove '\n' added when new user registered
            logins.update({split_user[0]: split_user[1].strip()})

        # Checks if username is a key in logins and checks if password is the associated value
        if username in logins.keys() and password == logins[username]:
            break
        else:
            # Error message if either the username or password are incorrect
            print("Username or password incorrect, please enter a valid username and password")

#====Menu Section====
while True:
    # To display extra menu options if user is admin, otherwise display norm_menu
    norm_menu = '''
a  - Add a task
va - View all tasks
vm - View my task
gr - Generate reports
e  - Exit
: '''
    admin_menu = '''
r  - Register a user
ds - Display statistics'''

    if username == 'admin':
        user_menu = admin_menu + norm_menu
    else:
        user_menu = norm_menu

    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input("Select one of the following options:" + user_menu).lower()

    # Creating a break line variable which can be used throughout the program
    break_line = "—" * 100

#====Register new user====
    # If the user is admin run reg_user function
    if menu == 'r' and username == 'admin':
        reg_user()


#====Display statistics====
    # If the user is 'admin' run stats function
    elif menu == 'ds' and username == 'admin':
        disp_stats()
        

#====Add new task====
    elif menu == 'a':
        add_task()
        

#====View all tasks====
    elif menu == 'va':
        view_all()


#====View my tasks====
    elif menu == 'vm':
        view_mine()

#====Generate reports====
    elif menu == 'gr':
        gen_rep()
        

#====Exit====
    elif menu == 'e':
        print(f'{break_line}\nGoodbye!!!\n{break_line}')
        exit()

#====Error message====
    else:
        print(f"{break_line}\nYou have made an incorrect choice, please try again\n{break_line}")