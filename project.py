import json

def create_account():
    for i in range(1):
        try:
            accounts = {}

            file = open('Accounts.json','r+')
            accounts = json.load(file)
            file.close

            username = input('please enter your username(0. return): ')
            if username == '0':
                return 'return'
            if username == '0':
                break
            
            if username in accounts:
                print('username is already used.\n')
                return 'return'
            if username in accounts:
                break
            
            else:
                name = input('please create your name(0. return): ')
                if name == '0':
                    return 'return'
                if name == '0':
                    break
                
                password = input('please create your password(0. return): ') 
                if password == '0':
                    return 'return'
                if password == '0':
                    break
                accounts[username] = { 'name' : name , 'password' : password}

            file = open('Accounts.json','w')
            json.dump(accounts,file,indent=4)
            file.close
            return name

        except FileNotFoundError:
            accounts = {}

            username = input('please create your username(0. return): ')
            if username == '0':
                return 'return'
            if username == '0':
                break
            
            name = input('please enter your name(0. return): ')
            if name == '0':
                return 'return'
            if name == '0':
                break
            
            password = input('please create your password(0. return): ') 
            if password == '0':
                return 'return'
            if password == '0':
                break
            
            accounts[username] = { 'name' : name , 'password' : password}

            file = open('Accounts.json','w')
            json.dump(accounts,file,indent=4)
            file.close
            return name

def log_in():
    for i in range(1):
        try:
            accounts = {}

            file = open('Accounts.json','r+')
            accounts = json.load(file)
            file.close

            while True:

                username = input('please enter your username(0. return): ')
                if username =='0':
                    return 'return'
                if username == '0':
                    break

                password = input('please enter your password(0. return): ') 
                if password =='0':
                    return 'return'
                if password == '0':
                    break

                if username in list(accounts.keys()) and password == accounts[username]['password']:
                    print(f'welcome {accounts[username]['name']}.')
                    return accounts[username]['name']
                if username in list(accounts.keys()) and password == accounts[username]['password']:
                    break

                else:
                    print('wrong username or password!\n')

        except FileNotFoundError:
            return False



def Data_base(DICT,name):
    try:    
        file = open(f'{name}.json','r+')
        DICT = json.load(file)
        file.close
        return DICT
    except FileNotFoundError:
        file = open(f'{name}.json','w')
        json.dump(DICT,file,indent=4)
        file.close
        return DICT

def saving(DICT,name):
    file = open(f'{name}.json','w')
    json.dump(DICT,file,indent=4)
    file.close

def save(func):
    def wrap(DICT,name):
        func(DICT,name)
        saving(DICT,name)
    return wrap

@save
def add_task(DICT,name):
    try:
        task = input("please enter your task's name: ")
        details = input("please enter your task's details: ")

        respond  = int(input ('how important is this task?\n1. important and emergency\n2. important and none-emergency\n3. unimportant and emergency\n4. uniportant and none-emergency\n'))
        
        if respond == 1:
            priority = "important and emergency"

        elif respond == 2:
            priority = "important and none-emergency"

        elif respond == 3:
            priority = "unimportant and emergency"

        elif respond == 4:
            priority = "unimportant and none-emergency"
        else:
            print('wrong entry! please choose one of options.\n')
        
        DICT['undone'][priority][task] = {"details" : details}
        print('successfully added.\n')

    except TypeError:
        print('wrong entery! please enter a number.\n')
    except Exception:
        print('Error\n')
    
    print('Done!')

@save
def remove_task(DICT,name):
    while True:
        try:
            respond = int(input('where do you want to remove from?\n1. tasks\n2. finished tasks\n3. clear fininshed tasks\n0. return\n '))

            if respond == 0:
                break

            elif respond == 1:
                while True:
                        
                    tasks_list = list(DICT['undone']['important and emergency'].keys())+list(DICT['undone']['important and none-emergency'].keys())+list(DICT['undone']['unimportant and emergency'].keys())+list(DICT['undone']['unimportant and none-emergency'].keys())
                    
                    for i in range(len(tasks_list)):
                        print(f'{i+1}. {tasks_list[i]}')
                    print('0. return')

                    select_task = int(input('which task do you want to remove?\n'))

                    if select_task == 0:
                        break

                    for j in list(DICT['undone'].keys()):  
                        if tasks_list[select_task-1] in DICT['undone'][j]:    
                            DICT['undone'][j].pop(tasks_list[select_task-1])
                        else:
                            pass

                    print('the task successfully removed.\n')

            elif respond == 2:
                while True:
                    tasks_list = list(DICT['done']['important and emergency'].keys())+list(DICT['done']['important and none-emergency'].keys())+list(DICT['done']['unimportant and emergency'].keys())+list(DICT['done']['unimportant and none-emergency'].keys())
                    
                    for i in range(len(tasks_list)):
                        print(f'{i+1}. {tasks_list[i]}')
                    print('0. return')

                    select_task = int(input('which task do you want to remove?\n'))

                    if select_task == 0:
                        break

                    for j in list(DICT['done'].keys()):
                        if tasks_list[select_task-1] in DICT['done'][j]:    
                            DICT['done'][j].pop(tasks_list[select_task-1])
                        else:
                            pass

                    print('the task successfully removed.\n')
                
            elif respond == 3:
                for i in DICT['done']:
                    DICT['done'][i].clear()
                print('finished tasks cleared.\n')
            
        except TypeError:
            print('wrong entery! please enter a number.\n')
        except IndexError:
            print('wrong entry! please choose one of options.\n')
        except Exception:
            print('Error\n')

    print('Done!')

@save
def finish_task(DICT,name):
    while True:
        try:
            tasks_list = list(DICT['undone']['important and emergency'].keys())+list(DICT['undone']['important and none-emergency'].keys())+list(DICT['undone']['unimportant and emergency'].keys())+list(DICT['undone']['unimportant and none-emergency'].keys())
            for i in range(len(tasks_list)):
                print(f'{i+1}. {tasks_list[i]}')
            print('0. return')
            select_task = int(input('which task do you want to finish?\n'))

            if select_task == 0:
                break

            for j in list(DICT['undone'].keys()):
                    
                    if tasks_list[select_task-1] in DICT['undone'][j]:    
                        DICT['done'][j][tasks_list[select_task-1]] = DICT['undone'][j][tasks_list[select_task-1]]
                    else:
                        pass

            for n in list(DICT['undone'].keys()):

                if tasks_list[select_task-1] in DICT['undone'][n]:
                    DICT['undone'][n].pop(tasks_list[select_task-1])
                else:
                    pass

            print('good job!\n')

        except TypeError:
            print('wrong entery! please enter a number.\n')
        except IndexError:
            print('wrong entry! please choose one of options.\n')
        except Exception:
            print('Error\n')
        
    print('Done.')
        
@save
def undo_task(DICT,name):
    while True:
        try:
            tasks_list = list(DICT['done']['important and emergency'].keys())+list(DICT['done']['important and none-emergency'].keys())+list(DICT['done']['unimportant and emergency'].keys())+list(DICT['done']['unimportant and none-emergency'].keys())
            for i in range(len(tasks_list)):
                print(f'{i+1}. {tasks_list[i]}')
            print('0. return')
            select_task = int(input('which task do you want to finish?\n'))

            if select_task == 0:
                break

            for j in list(DICT['done'].keys()):
                if tasks_list[select_task-1] in DICT['done'][j]:    
                    DICT['undone'][j][tasks_list[select_task-1]] = DICT['done'][j][tasks_list[select_task-1]]
                else:
                    pass

            for n in list(DICT['done'].keys()):

                if tasks_list[select_task-1] in DICT['done'][n]:
                        DICT['done'][n].pop(tasks_list[select_task-1])
                else:
                    pass
                    
        except TypeError:
            print('wrong entery! please enter a number.\n')
        except IndexError:
            print('wrong entery! please choose one of the options.\n')
        except Exception:
            print('Error\n')

    print('Done.')
    
@save
def edit_task(DICT,name):
    while True:
        try:
            tasks_list = list(DICT['undone']['important and emergency'].keys())+list(DICT['undone']['important and none-emergency'].keys())+list(DICT['undone']['unimportant and emergency'].keys())+list(DICT['undone']['unimportant and none-emergency'].keys())
            
            for i in range(len(tasks_list)):
                print(f'{i+1}. {tasks_list[i]}')
            print('0. return')
            select_task = int(input('which task do you want to edit?\n'))

            if len(tasks_list) < select_task:
                raise IndexError

            if select_task == 0:
                break

            respond = int(input('what do you want to change?\n1. Name\n2. Details\n0. return\n'))

            if respond == 0:
                    break
                    
            elif respond == 1:


                for j in list(DICT['undone'].keys()):
                    if tasks_list[select_task-1] in DICT['undone'][j]:
                        new_name = input('please enter the new name: ')
                        detail = DICT['undone'][j][tasks_list[select_task-1]]
                        DICT['undone'][j][new_name] = detail
                        DICT['undone'][j].pop(tasks_list[select_task-1])
                        print(f'task\'s name successfully changed to {new_name}\n')
                    else:
                        pass

            elif respond == 2:
                            

                for j in list(DICT['undone'].keys()):
                    if tasks_list[select_task-1] in DICT['undone'][j]:
                        new_details = input('please enter your task\'s new details: ')
                        DICT['undone'][j][tasks_list[select_task-1]] = {'details':new_details}
                        print('task\'s detail successfully changed.\n')
                    else:
                            pass

            else:
                print('wrong entery! please choose one of the options.\n')

        except IndexError:
            print('wrong entery! please choose one of the options.\n')
        except TypeError:
            print('wrong entery! please enter a number.\n')
        except Exception:
            print('Error\n')

    print('Done!')

def task_manager(name):

    manager = {'undone':{'important and emergency':{},'important and none-emergency':{},'unimportant and emergency':{},'unimportant and none-emergency':{}},
               'done':{'important and emergency':{},'important and none-emergency':{},'unimportant and emergency':{},'unimportant and none-emergency':{}}}
    
    show_finished_tasks = True
    
    process = True
    while process:
        manager = Data_base(manager,name)
        
        print('*********** TASKS ***********\n')
        for i in manager['undone']:
            print(f'*** {i} *** \n\n')
            for j in list(manager['undone'][i].keys()):
                print(f'<< Task:{j} >>\n    Details: {manager['undone'][i][j]['details']}\n\n')

        if show_finished_tasks:
            print('*********** FINISHED TASKS ***********\n')
            for n in manager['done']:
                print(f'*** {n} *** \n\n')
                for m in list(manager['done'][n].keys()):
                    print(f'<< Task:{m} >>\n    Details: {manager['done'][n][m]['details']}\n\n')
        

        respond = input(f'what do you want to do?\n1. add task\n2. remove task\n3. finish task\n4. undo task\n5. edit tasks\n6. hide finished tasks\n7. show finished tasks\n0. log out\n00.Exit\n')
        if respond == '1':
            add_task(manager,name)
        elif respond == '2':
            remove_task(manager,name)
        elif respond == '3':
            finish_task(manager,name)
        elif respond =='4':
            undo_task(manager,name)
        elif respond =='5':
            edit_task(manager,name)
        elif respond == '6':
            if show_finished_tasks == False:
                print("It's already hide.\n")
            elif show_finished_tasks == True:
                show_finished_tasks = False
                print('finished tasks got hidden.\n')
        elif respond == '7':
            if show_finished_tasks == True:
                print("It's already shown.\n")
            elif show_finished_tasks == False:
                show_finished_tasks = True
                print('finished tasks got unhidden.\n')
        elif respond == '0':
            process = False
            return False
        elif respond == '00':
            process = False
            return True
        else:
            print('wrong entry! please try again.')

def main():

    while True:

        start = input('what do you want to do?\n1. create account\n2. log in\n0. Exit\n')

        if start == '1':
            name = create_account()
            if name == 'return':
                pass
            else:  
                exit = task_manager(name)
                if not exit:
                    pass
                elif exit:
                    print('Goodbye')
                    break

        elif start == '2':
            name = log_in()
            if name == 'return':
                pass
            else:
                if name == False:
                    print('there\'s no account! please log in and create your first account.\n')
                else:
                    exit = task_manager(name)
                    if not exit:
                        pass
                    elif exit:
                        print('Goodbye!')
                        break
        
        elif start == '0':
            print('Goodbye!')
            break

        else:
            print('wrong entry! please choose one of options.\n')
            
main()