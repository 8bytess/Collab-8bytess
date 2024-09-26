print("\n\tWelcome To Your Note Taking App")
list=[]

def to_do():
    

    while True:
        print('\nADD NOTE')
        note=input()
        print('\nADD MORE?? [Yes OR No]')
        ans=input()
        list.append(note)
        if ans=='yes' or ans=='Yes':
            continue
        elif ans=='no' or ans=='No':
            break 
        else:
            print('Enter a valid answer') 
    
    leng=len(list)   
    # i=0
    # print('\nYOUR TASKS ARE : ')
    # while i<leng:
    #     print(f"{i+1}. {list[i]}")
    #     i+=1
    # print('\n')
    
    while True:
        choice=int(input('''OPERATIONS :
        1. ADD TASK
        2. DELETE TASK
        3. VIEW
        4. SAVE 
        
        YOUR CHOICE : '''))

        if choice==1:
            print("---ADD TASK---")
            new_task=input()
            list.append(new_task)
            print('NEW TASK HAS BEEN ADDED')
    
        elif choice==2:
            remove=int(input('WHICH NUMBER TASK DO YOU WANT TO REMOVE??'))
            if remove>leng:
                print("VALID A NUMBER OF TASK TO REMOVE")
            else:
                list.pop(remove-1)
                print('the task has been succesfully removed ')
                
    
        elif choice==3:
            length=len(list)   
            i=0
            print('\nYOUR TASKS ARE : ')
            while i<length:        
                print(f"{i+1}. {list[i]}")
                i+=1
            print('\n')
    
    
        else:
            with open('tasks', 'w') as out_file:
             le=int(len(list))
             n=0
             while n<le:
                out_file.write(f"{n+1}. {list[n]}")
            break
    


to_do()       