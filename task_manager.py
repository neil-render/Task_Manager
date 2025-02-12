#--------------------------------------------------------------FUNCTIONS-------------------------------------------------------------#

def reg_user():
  print("--------------REGISTER USER---------------\n")
  
  while True:  #  Repeat registration until unique username entered. 
    register = True  #  Provides a reslut to determing outcome after check.
    user_file = open('user.txt', 'r')  #  Open file for reading.
    new_username = input("Please enter your new username: ").strip()  #  Prompt user for username and remove any redundant spaces.
    for line in user_file:  #  Reads each line of file variable.
     user_data = line.split(",")  #  Separates username from password using ',' as delimiter.
     if user_data[0] == new_username:  #  Checks if 'new_username' already exists.
      register = False  #  If username aready exists 'register' is False.
      break  #  Breaks out of 'for loop'.
    if register == False:  #  If registration is False, message shown and user prompted to try again.
     print("Username taken, please try again: ")
     print("")
    if register == True:  #  If register remains True then break out of 'while True' loop.
     break
  user_file.close()
  user_file = open('user.txt', 'a+')  #  Opens file for appending/reading.
  psword = input("Please enter a password: ").strip()  
  psword_check = input("Please re-enter your password: ").strip()  
  #  If new password entries match, username and password written to file.
  if psword == psword_check:  
    user_file.write(new_username + ", " + psword + "\n")
    user_file.close()
    with open('tasks.txt', 'a+') as task_file:
      task_file.write(new_username + ", " + "No Tasks Assigned" + ", " + "n/a" + ", " + "n/a" + ", " + 
                      "n/a"  + ", " + "n/a" + "\n")  
  else:
    #  If new password entries do not match user returned to menu.
    print("\n_Passwords do not match_\n")
    input("                  - Press Enter to retun to MAIN MENU -")
  user_file.close()


def add_task():
  print("-----------------ADD TASK-----------------\n")
  user_check = False
  task_username = input("Please enter the username of person doing the task: ").strip()
  #  Reads each line of 'user.txt' file and splits username and password into elements of 'user_data' list.
  with open('user.txt', 'r') as user_file:  
    for line in user_file:
      user_data = line.split(", ")  
      if user_data[0].strip() == task_username:  #  If username exists opens 'tasks.txt' and appends task.
        user_check = True
        task_file = open('tasks.txt', 'a+')  
        #  Prompt user for new task data.
        task_title = input("Please enter the title of the assigned task: ").strip()
        task_description = input("Please enter a description of the task: ").strip()
        task_start_date = input("Please enter the start date (e.g. 21 Oct 2022): ").strip()
        task_due_date = input("Please enter the due date (e.g. 21 Oct 2022): ").strip()
        task_complete = "No"
        #  New task data wirtten to file with (", ") as delimiter.
        task_file.write(task_username + ", " + task_title + ", " + task_description + ", " + task_start_date + ", " + 
        task_due_date  + ", " + task_complete + "\n")  
        #  'input' used to hold dsiplay until user pressed enter and taken back to menu.
        print("\n_Task added_\n")
        input('                 - Press Enter to retun to MAIN MENU -')
    if user_check == False:  #  Informs user if username does not exist.
      print("\n_Username does not exist_\n")  
      input('                 - Press Enter to retun to MAIN MENU -')
        

        


def view_all():
  print("--------------ASSIGNED TASKS--------------\n")
  task_file = open('tasks.txt', 'r')
  #  Task data read from file and placed as items into list using (", ") as a delimiter.
  for line in task_file:  
    task_data = line.split(", ")
    task_data[5] = task_data[5].strip()  #  Removes any redundant space or escape characters.
    #  Task items displayed in prescribed order and layout.
    print(f"Task:                {task_data[1]}")  
    print(f"Assigned to:         {task_data[0]}")
    print(f"Date assigned:       {task_data[3]}")
    print(f"Due date:            {task_data[4]}")
    print(f"Task Complete?       {task_data[5]}")
    print(f"Task Description:  \n {task_data[2]}")
    print("")
  input('                  - Press Enter to retun to MAIN MENU -')  
  task_file.close()



def view_mine():
  print("-----------------MY TASKS-----------------\n")
  user_tasks = []
  user_task_list = []
  user_check = False
  task_num = 0 

  #  Opens 'tasks.txt' and splits each line into item of nested list 'user_tasks'.
  task_file = open('tasks.txt', 'r')
  for line in task_file:
    task_data = line.split(", ")
    user_tasks.append(task_data)
  task_file.close()

  #  Checks for tasks assigned to user, using 'user_name' entered at initial login.
  for task in range(len(user_tasks)):
    if user_tasks[task][0] == user_name:  #  If tasks assigned to user, data displayed in decipherable format.
      user_check = True
      user_task_list.append(task_num)  #  Appends number of task to 'user_task_list' for selection in edit menu. 
      print(f"Task Number:         {task}") 
      print(f"Task:                {user_tasks[task][1]}")
      print(f"Assigned to:         {user_tasks[task][0]}")
      print(f"Date assigned:       {user_tasks[task][3]}")
      print(f"Due date:            {user_tasks[task][4]}")
      print(f"Task Complete?       {user_tasks[task][5].strip()}")  #  Removes redundant space or escape characters.
      print(f"Task Description:\n  {user_tasks[task][2]}")
      print("")
    task_num += 1  #  'task_num' incremented for every task.
  if user_check == False:  #  If no task assigned to user, message displayed.
    print("\n_No Tasks Assigned_\n")
    input('                 - Press Enter to retun to MAIN MENU -')


  edit_option = input("\nChoose a task number to edit or enter '-1' to EXIT: ")
  if edit_option == '-1' or edit_option == '':  #  Takes user back to main menu if  '-1' or invalid entry.
    pass
  elif edit_option in str(user_task_list):  #  Displays task data if existing user task selected from 'user_task_list'.
    task = int(edit_option)  #  Displays correct data for task from 'user_tasks' list, using 'edit_option' integer.
    os.system('clear')
    print("")
    print(f"Task Number:         {task}")
    print(f"Task:                {user_tasks[task][1]}")
    print(f"Assigned to:         {user_tasks[task][0]}")
    print(f"Date assigned:       {user_tasks[task][3]}")
    print(f"Due date:            {user_tasks[task][4]}")
    print(f"Task Complete?       {user_tasks[task][5]}")
    print(f"Task Description:\n  {user_tasks[task][2]}")

    print("")
    print("---------------TASK_EDIT_MENU------------------")
    edit_option = input('''\nSelect one of the following options below:\n
c   -   Mark task complete/incomplete
r   -   Reassign task
d   -   Ammend due date
e   -   Exit\n
: ''').lower()
    #  If 'c' selected from edit menu (Mark task complete/incomplete).
    if edit_option == 'c':
      edit_option = input('\nWould you like to mark the task complete y/n? ')
      if edit_option.lower() == 'y':
        user_tasks[task][5] = 'Yes'
      elif edit_option.lower() == 'n':
        user_tasks[task][5] = 'No'
      else:
        print("\n_Not a valid option_\n")

    #  If 'r' selected from edit menu (Reassig task).
    elif edit_option == 'r':
      if 'Yes' not in user_tasks[task][5]:
        edit_option = input('\nPlease enter new assignee name: ')
        user_tasks[task][0] = edit_option
      else:
        print("\n_Task completed already_\n")
      
    #  If 'd' selected from edit menu (Ammend due date).
    elif edit_option == 'd':
      if 'Yes' not in user_tasks[task][5]:  #  Checks if task not completed already.
        edit_option = input('\nPlease enter new due date (eg. 25 Dec 2023): ')  
        user_tasks[task][4] = edit_option  #  Ammends new date list
      else:
        print("\n_Task completed already_\n")

    #  If 'e' selected from edit menu.
    elif edit_option == 'e':
      pass

    #  If invalid selection from edit menu returns to main menu.
    else:
      if edit_option not in 'crde':
        print('\n_Not a valid selection_\n')
        input('-                  Press Enter to retun to MAIN MENU -')
  #  If '-1' or invalid input returns user to main menu.
  else:
    print("\n_Not a valid selection_\n")
    input('-                  Press Enter to retun to MAIN MENU -')

  #  Formats nested list 'user_tasks' and writes to file 'tasks.txt'.
  with open('tasks.txt', 'w') as f:
    for sublist in user_tasks:
      line = "{}, {}, {}, {}, {}, {}".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4], sublist[5])
      f.write(line)




def gen_reports():
  import datetime  #  Imports 'datetime' module.
  from datetime import date  #  Imports 'date' funtion to check due dates for user tasks.
  today = date.today()  #  Gets today's date.
  date_data = today.strftime("%d/%m/%Y")  #  Sets format of the date to match data in 'tasks.txt'.
  today_date = date_data.split("/")  #  Date items appended to 'today_date' list.
  
  total_tasks = 0
  total_completed = 0
  total_incomplete = 0
  total_overdue = 0
  total_users = 0
  month_list = [
    '0', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'
    ]  #  List of months to convert month into a corresponding index integer value, '0' added so 'Jan' = 1. 
  users_dict = ({})
  #  Calculates total amount of tasks - if user assigned a task 'total_tasks' is incremented.
  with open('tasks.txt', 'r') as task_file:
    for task in task_file:
      task_data = task.split(", ")
      if task_data[1] != 'No Tasks Assigned':  #  String written when new user registered by admin. 
        total_tasks += 1
  # Iterates through each line of 'tasks.txt', using 'task-data' list to extract data for each task.
  with open('tasks.txt', 'r') as task_file:
    for task in task_file:
      task_data = task.split(", ")
      user = task_data[0]
      #  Adds each user to nested dictionary 'user_dict' with keys and values described.
      if user not in users_dict:
        users_dict[user] = {'Total User Tasks: ': 0, 
                            'Percentage Of Total Tasks: ': 0, 
                            'Percentage Of Tasks Complete: ': 0,
                            'Percentage Of Tasks Incomplete: ': 0, 
                            'Percentage Of Tasks Overdue: ': 0, 
                            'Total Tasks Complete: ': 0,
                            'Total Tasks Incomplete: ': 0, 
                            'Total Tasks Overdue: ': 0,
                            }
      #  If user has no tasks assigned 'users_dict' key values not updated.
      if task_data[1] == 'No Tasks Assigned':
        pass
      #  If user has tasks assigned 'users_dict' key values updated.
      else:
        users_dict[user]['Total User Tasks: '] += 1
        
        due_date = task_data[4].split(" ")  #  Splits due date into day, month and year within 'due_date' list.
        month = month_list.index(due_date[1])  #  Converts month into an integer value using 'month_list'.
        due_date[1] = month
        
        #  Sets format to compare due date with today's date.
        d1 = datetime.date(int(due_date[2]), int(due_date[1]), int(due_date[0]))
        d2 = datetime.date(int(today_date[2]), int(today_date[1]), int(today_date[0]))
        
        #  Checks if task completed and updates key value.
        if task_data[5].strip() == 'Yes':
          total_completed += 1
          users_dict[user]['Total Tasks Complete: '] += 1

        #  Checks if task incomplete and updates key value.
        if task_data[5].strip() == 'No':
          total_incomplete += 1
          users_dict[user]['Total Tasks Incomplete: '] += 1
          #  If task incomplete checks if task overdue and updates key value.
          if d1 < d2:
            total_overdue += 1
            users_dict[user]['Total Tasks Overdue: '] += 1
            

        users_dict[user]['Percentage Of Total Tasks: '] = round((users_dict[user]['Total User Tasks: ']
                                                          / total_tasks * 100), 2)
        users_dict[user]['Percentage Of Tasks Complete: '] = round((users_dict[user]['Total Tasks Complete: '] 
                                                            / users_dict[user]['Total User Tasks: '] * 100), 2)
        users_dict[user]['Percentage Of Tasks Incomplete: '] = round((users_dict[user]['Total Tasks Incomplete: '] 
                                                              / users_dict[user]['Total User Tasks: '] * 100), 2)
        users_dict[user]['Percentage Of Tasks Overdue: '] = round((users_dict[user]['Total Tasks Overdue: '] 
                                                            / users_dict[user]['Total Tasks Incomplete: '] * 100), 2)
        
    #  Calculates ratio values to add to 'task_overview' dictionary.
    ratio_incomplete = int(total_incomplete/total_tasks * 100)
    ratio_overdue = int(total_overdue/total_incomplete * 100)
  #  Caluclates total amount of users from 'user.txt' file.
  with open('user.txt', 'r') as user_file:
    for user in user_file:
      total_users += 1
  #  Creates 'task_overview' dictionary with relevant keys and values to write to file.
  task_overview = {'Total Tasks:' : total_tasks, 
                   'Total Tasks Completed: ' : total_completed, 
                   'Total Tasks Incomplete: ' :  total_incomplete, 
                   'Total Tasks Overdue: ' : total_overdue, 
                   'Percentage Of Incomplete Tasks: ' : ratio_incomplete, 
                   'Percentage Of Overdue Tasks: ' : ratio_overdue
		               }


  #  Writes dictionary to corresponding file.
  with open('task_overview.txt', 'w') as convert_file:
    convert_file.write(json.dumps(task_overview))
  #  Writes dictionary to corresponding file.
  with open('user_overview.txt', 'w') as convert_file:
    convert_file.write(json.dumps(users_dict))

  print("\n_Reports Generated_\n")
  input("\n                  - Press Enter to retun to MAIN MENU -")
  



def display_statistics():
  print("----------USER & TASK STATSISTICS---------\n\n")

  print("----------TASK OVERVIEW---------\n\n")

  
  with open('task_overview.txt', 'r') as overview_file:  # Reading the data from the file.
    data = overview_file.read()
    task_overview_dict = json.loads(data)  #  Reconstructs data from string into a dictionary.
    for key,value in task_overview_dict.items():  #  Prints each key and value.
      print(key, value)

  print("\n\n----------USER OVERVIEW---------\n")
  
  total_users = 0
  with open('user_overview.txt', 'r') as overview_file:  # Reading the data from the file.
    data = overview_file.read()
    users_overview_dict = json.loads(data)  #  Reconstucts data from string into a dictionary.
    #  Prints each users' corresponding keys and values from 'users_overview_dict'.
    for user, user_data in users_overview_dict.items(): 
      print("")
      print("User Name: ", user)
      total_users += 1
      for key in user_data:
        print(key + ':', user_data[key])
    
    

  #  Displays summary information to user.admin
  print(f"\n\nTotal Tasks Assigned To Users: {task_overview_dict['Total Tasks:']}\n")
  print(f"Total Users: {total_users}\n")
  input('\n\n                 - Press Enter to retun to MAIN MENU -')  



#------------------------------------------------------START-OF-PROGRAM-------------------------------------------------------------#

import os  #  Import 'os' module to use clear screen with os.system('clear').
import json  #  Imports 'json' module to write nested dictionary to file.

print("<--------------WELCOME_TO_TASK_MANAGER-------------->\n")
print("")

#  while loop repetitively prompts user for correct username and password.
while True:  
  login = False
  user_file = open('user.txt', 'r')
  #  strip() used to remove accidental space.
  user_name = input("Please enter your username: ").strip()  
  psword = input("Please enter your password: ").strip()
  for line in user_file: 
    user_check = False
    if user_name in line:
      if psword in line:
        user_check = True
    if user_check == True:
      break
  
  if user_check == True:
    break
  else:
    print("Invalid password or username, please try again: ")
    print("")
user_file.close()

#  while loop to continuously return to menu display. 
while True: 
    os.system('clear') 
    print("")
    #  Selection of main menu options in lower case.
    print("-------------------MAIN MENU-------------------\n")
    menu = input('''Select one of the following Options below:\n
r   -   Register a user (admin users only)
a   -   Add a task
va  -   View all tasks
vm  -   View my tasks
gr  -   Generate reports 
ds  -   Display statistics (admin users only) 
e   -   Exit\n
: ''').lower()  
    
    #  If admin user, menu option 'r' valid selection.
    if menu == 'r'and user_name == 'admin':  
        os.system('clear')
        reg_user()
          
    #  Menu option 'a' selected by user. 
    elif menu == 'a':  
      os.system('clear')
      add_task()

    #  Menu option 'va' selected by user.
    elif menu == 'va':   
      os.system('clear')
      view_all()

    #  Menu option 'vm' selected by user.
    elif menu == 'vm': 
      os.system('clear')
      view_mine()

    #  Menu option 'gr' selected by user.
    elif menu == 'gr':
      gen_reports()
      
    #  If admin user, menu option 's' valid selection.
    elif menu == 'ds' and user_name == 'admin':
      os.system('clear')
      display_statistics()
       
    #  Menu option 'e' selected by user.
    elif menu == 'e':
        print("")
        print("Live Long And Prosper!")
        #  Menu loop stopped and program ended.
        break
    #  Invalid menu selection, user requested to choose again. 
    else:
        print("")
        print("\n_Invalid selection_\n")
        input("\n                  - Press Enter to retun to MAIN MENU -")
        print("")





