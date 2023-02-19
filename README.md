# Capstone 3: task_manager extended
## Description
 - Extending the functionality of Capstone 2 using functions

## Installation
  - Download task_manger.py, tasks.txt and user.txt
  - Run task_manager.py
  
## Usage
- Log into program using the username and password in user.txt
- The following menu will appear:

  ![image](https://user-images.githubusercontent.com/91968539/219957910-1c927be6-55f8-40bb-97b2-7ec4b8bbfe63.png)
  
  - If not logged in as 'admin': 'r  - Register a user' and 'ds  - Display statistics' will not be visable or accessible
- r  - Register a user
  - Input new username and password, these will be appended to user.txt
  - Will not allow duplicates of usernames
- ds  - Display statistics
  - Will run the 'Generate reports' function if not already done
  - Display the data from task_overview.txt and user_overview.txt
- a  - Add a task
  - Input the username, title, description and due date for the task
  - These will be appended to tasks.txt (along with 'assigned_date' - todays date and 'No' - i.e. the task is not complete
- va - View all tasks
  - Displays all tasks in easy to read format
- vm - View my task
  - Displays tasks assigned to the logged in user in easy to read format
  - User is able to mark their tasks as complete or the task can be edited (username or due date) if task is not complete
- gr - Generate reports
  - Will generate two txt files, task_overview.txt and user_overview.txt
  - These will display statistics about tasks and users respectively
- e  - Exit
  - Exits the program
