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
        task.write('\n'+main_input[2] +' '+ main_input[3])
        
        print("Added Task :" +' "' +main_input[3]+ '"' +' with priority '+ main_input[2]) # main_input[2] --> priority, main_input[3] --> message

def list_task():
    internal_count =0
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n") # splitting each line
        for i in range(0,11):
            for j in range(1,len(task_list)):
                priority_num = int(task_list[j].split()[0])
                if ( i == priority_num):
                    internal_count = internal_count +1
                    task_name = ' '.join(task_list[j].split()[1:]) # using string splitting we create task name
                    print("{0}. {1} [{2}]".format(internal_count,task_name,priority_num))

    task.close()

def done_task(done_num):
    
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
                if(i<len(lines)): # to fix list index going out of range due to newline character
                    task.write("\n")
        task.truncate()
    
    task.close()
    return task_which_is_done

def task_complete_add(task_which_is_done):
   
    # Function adds the completed tasks to the completed.txt file
    with open('completed.txt','a+') as completed:
        completed.seek(0)
        completed.write("\n"+task_which_is_done)
        print('Marked item as done.')

    completed.close()

def report_func():
    
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n")
    
    task.close()
    print("Pendind: {0}".format(len(task_list)-1))
    
    list_task()

    
    


### End of Functions ###

if(len(sys.argv)==1):
    help_func()

# here definer is the command which follows after ./task
definer = sys.argv[1] 

if(definer == "help") :
    help_func()

elif (definer=="add"):
    add_task(sys.argv) # here sys.argv is taken in at function as main input

elif (definer=="done"):
    task_which_is_done = done_task(sys.argv[2])
    task_complete_add(task_which_is_done)

elif (definer=="del"):
    task_which_is_done = done_task(sys.argv[2])
    # here for the delete command, we use the same function used for "done" but we dont parse the 
    # received data to the task_complete_add() function which adds the data to the completed.txt file

elif (definer=="ls"):
    list_task()

elif (definer=="report"):
    report_func()
