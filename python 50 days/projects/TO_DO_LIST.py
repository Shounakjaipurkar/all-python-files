tasklist=[]
while True:
 tasks=input("Enter the task for today: ")
 #tasklist=[] here i did one mistake 
 tasklist.append(tasks)
 print(tasklist)
 repeat=input("Do you want to repeat again: yes/no")
 if repeat!="yes":
    print("your tasks are:",tasklist)
    print("Thnak you")
    
    break
'''in forth line i did one mistake that is declaring the empty list inside the loop but it is wrong.
Why-->so it is taking an input and storing it in the task list but again when loop itrate the tasklist becomes empty as we declare it as an empty list
So the solution for this is to declare the tasklist outside the loop so that when loop itrate seconde time the task list will directly store the task  '''
