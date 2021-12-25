import sys

task_id=0
# This is the default function, which is used for printing the help when the help
# or a command is passed without any arguments
def help_func(): 
    print('Usage :-')
    print('$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list')
    print('$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order')
    print('$ ./task del INDEX            # Delete the incomplete item with the given index')
    print('$ ./task done INDEX           # Mark the incomplete item with the given index as complete')
    print('$ ./task help                 # Show usage')
    print('$ ./task report               # Statistics')

def add_task(main_input):
    with open('task.txt','a+') as task:
        msg = '\n'+main_input[2] +' '+ main_input[3]
        
        current_len = count_tasks('task.txt')
        if(current_len == 1):
            task.write(msg.lstrip())
        else:
            task.write(msg)
        
        print("Added Task:" +' "' +main_input[3]+ '"' +' with priority '+ main_input[2]) # main_input[2] --> priority, main_input[3] --> message
        
def list_task():
    # This function lists out all the tasks which are present in the tasks.txt file
    internal_count =0
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n") # splitting each line
        if(task_list[1]==""): # empty lines are considered here
            print('There are no pending tasks!')
        for i in range(0,11):
            for j in range(1,len(task_list)):
                priority_num = int(task_list[j].split()[0])
                if ( i == priority_num):
                    internal_count = internal_count +1
                    task_name = ' '.join(task_list[j].split()[1:]) # using string splitting we create task name
                    print("{0}. {1} [{2}]".format(internal_count,task_name,priority_num))

    return(len(task_list))
    task.close()

def list_task_completed():

    # This function lists out all the tasks which are present in the completed.txt file
    internal_count =0
    with open('completed.txt','a+') as completed:
        completed.seek(0)
        completed_list = completed.read().split("\n") # splitting each line
        for i in range(0,11):
            for j in range(1,len(completed_list)):
                priority_num = int(completed_list[j].split()[0])
                if ( i == priority_num):
                    internal_count = internal_count +1
                    task_name = ' '.join(completed_list[j].split()[1:]) # using string splitting we create task name
                    print("{0}. {1} [{2}]".format(internal_count,task_name,priority_num))

    completed.close()

def done_task(done_num):
    
    # This function removes the tasks which are mentioned to be completed by the user
    internal_count =0
    
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n") # splitting each line
    
        for i in range(0,11):
            for j in range(1,len(task_list)):
    
                priority_num = int(task_list[j].split()[0])
    
                if ( i == priority_num):
    
                    internal_count = internal_count +1
                    if(internal_count == int(done_num)):
                        task_which_is_done = task_list[j]
    
    with open('task.txt','r+') as task:
    
        i=0
        lines = task.readlines()
        task.seek(0)
    
        for line in lines:
            i =i+1
            main_clause = line.split("\n")[0]
            if main_clause != task_which_is_done: 
                task.write(main_clause)
                if(i==2 and (len(lines)-1)== 2): # used this pass statement to fix newline character problem
                    pass
                elif(i<=len(lines)-1):
                    task.write("\n")
        task.truncate()
    
    task.close()
    return task_which_is_done

def task_complete_add(task_which_is_done):
   
    # Function adds the output of the done_task() function to the completed.txt file
    with open('completed.txt','a+') as completed:
        completed.seek(0)
        completed.write("\n"+task_which_is_done)
        print('Marked item as done.')

    completed.close()

def count_tasks(f_name):
    # This function counts the no of tasks present either in tasks.txt file or completed.txt file based on the inputs
    with open(f_name,'r') as file:
        file.seek(0)
        file_len = len(file.read().split("\n"))-1
    file.close()
    return file_len

def report_func():

    # This function returns the report of the overall To-Do CLI coagulating all the required functions
    
    no_of_tasks = count_tasks('task.txt')
    # print("Pending: {0}".format(no_of_tasks))
    internal_count =0
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n") # splitting each line
        # if(task_list[1]==""): # empty lines are considered here
        #     print('There are no pending tasks!')
        if(len(task_list)==2):
            print("Pending: 0")
        else:
            print("Pending: {0}".format(no_of_tasks))
        for i in range(0,11):
            for j in range(1,len(task_list)):
                priority_num = int(task_list[j].split()[0])
                if ( i == priority_num):
                    internal_count = internal_count +1
                    task_name = ' '.join(task_list[j].split()[1:]) # using string splitting we create task name
                    print("{0}. {1} [{2}]".format(internal_count,task_name,priority_num))
    
    print("\n")
    
    
    no_of_tasks = count_tasks('completed.txt')
    print("Completed: {0}".format(no_of_tasks))
    list_task_completed()
    print("\n")

### End of Functions ###



if(len(sys.argv)==1):
    help_func()


try:
    # The other part is used in a try: indent because, when no arguments are passed, the interpretor returns a error message

    definer = sys.argv[1] 
    # a definer varibale is used to understand the function given by the user

    if(definer == "help") :
        help_func()

    elif (definer=="add"):
        if(len(sys.argv)<=3):
            print("Error: Missing tasks string. Nothing added!")
        else:
            add_task(sys.argv) # here sys.argv is taken in at function as main input

    elif (definer=="done"):
        try:
            if(len(sys.argv)==2):
                print('Error: Missing NUMBER for marking tasks as done.')
            else:
                task_which_is_done = done_task(sys.argv[2])
                task_complete_add(task_which_is_done)
        except:
            print(f'Error: no incomplete item with index {sys.argv[2]} exists.')
            pass

    elif (definer=="del"):
        try:
            if(len(sys.argv)==2):
                print('Error: Missing NUMBER for deleting tasks.')
            else:    
                task_which_is_done = done_task(sys.argv[2])
                print(f'Deleted task #{sys.argv[2]}')
        except:
            print('Error: task with index {0} does not exist. Nothing deleted.'.format(sys.argv[2]))
        # here for the delete command, we use the same function used for "done" but we dont parse the 
        # received data to the task_complete_add() function which adds the data to the completed.txt file

    elif (definer=="ls"):
        list_task()

    elif (definer=="report"):
        report_func()
    
    # elif(definer == "tester"):
    #     count_val = count_tasks('task.txt')
    #     print(count_val)
except:
    pass