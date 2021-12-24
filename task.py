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
        # here identifier symbols are placed in between to simplify the process of parsing the data
        task.write("\n"+ '"' +main_input[3]+ '"' +':'+ ' with priority '+ main_input[2]+';')

def list_task():
    internal_count =0
    with open('task.txt','a+') as task:
        task.seek(0)
        task_list = task.read().split(";")
        for i in range(10):
            for j in range(len(task_list)-1):
                priority_num = int(task_list[j].split()[-1])
                if(i == priority_num):
                    internal_count = internal_count+1
                    print(f'{internal_count}. {task_list[j].split(":")[0][2:-1]} [{priority_num}]') # using list splitting & string slicing we print the output

    task.close()

def done_task(done_num):
    pass

### End of Functions ###

if(len(sys.argv)==1):
    help_func()

# here definer is the command which follows after ./task
definer = sys.argv[1] 

if(definer == "help") :
    help_func()

elif (definer=="add"):
    print('add-printed')
    add_task(sys.argv) # here sys.argv is taken in at function as main input
    # completed beta phase of the add function

elif (definer=="done"):
    print("removing the one with the present serial number")
    done_task(sys.argv[2])


elif (definer=="ls"):
    list_task()

elif (definer=="report"):
    print('report-printed')
