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
    done_num = int(done_num) # Variable is passed as a string, and therefore needs to be converted to int
    internal_count =0
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split("\n") # splitting each line
        for i in range(0,11):
            for j in range(1,len(task_list)):
                priority_num = int(task_list[j].split()[0])
                if ( i == priority_num):
                    internal_count = internal_count +1
                    if(internal_count == done_num):
                        task_name = ' '.join(task_list[j].split()[1:]) # using string splitting we create task name
                        print("{0}. {1} [{2}]".format(internal_count,task_name,priority_num))
                        task_which_is_done = task_list[j]

    with open('completed.txt','a+') as completed:
        completed.write(task_which_is_done)
                    
    task.close()
    completed.close()

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
    done_task(sys.argv[2])

elif (definer=="del"):
    pass

elif (definer=="ls"):
    list_task()

elif (definer=="report"):
    print('report-printed')
