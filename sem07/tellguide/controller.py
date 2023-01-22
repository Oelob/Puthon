import _input
import csv
import unicodedata
import output
import sorting

def Menu():
    a = int(input('Выберете действие: \n1 - создать новый контакт; \n2 - показать контакты; \n3 - сортировать контакты; \n4 - добавить контакт; \n0 - закончить работу \n'))
    return a

def GetNewCont():
    contact = list(_input.Create_New_Cont())

    
    with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'a') as a_file:
        head = ['ID', 'FirstName', 'LastName', 'PhoneNumber', 'Comments']
        contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
        contacts.writeheader()
        contacts.writerow({'ID':contact[0], 'FirstName':contact[1], 'LastName':contact[2], 'PhoneNumber':contact[3], 'Comments':contact[4]})   
        temp = int(input('Если хотите добавить еще один контакт, нажмите 1. Если хотите выйти нажмите 0. '))
        
    while temp == 1:
        contact = list(_input.Create_New_Cont())
        with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'a') as a_file:
            contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
            contacts.writerow({'ID':contact[0], 'FirstName':contact[1], 'LastName':contact[2], 'PhoneNumber':contact[3], 'Comments':contact[4]}) 
        temp = int(input('Если хотите добавить еще один контакт, нажмите 1. Если хотите выйти нажмите 0. '))
    
def MenuForShowingCont():
    choose = int(input('Выберете дейсвтие: \n1 - Показать всю информацию контакта; \n2 - Показать только Имя и Фамилию; \n0 - Возврат в предыдущее меню\n'))
    return choose

def MenuSorting():
    choose = int(input('Выберете действие: \n1 - сортировать контакты по Имени; \n2 - сортировать контакты по ID; \n0 - возврат в главное меню \n'))
    return choose

def AddCont():
    contact = list(_input.Create_New_Cont())
    with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'a') as a_file:
        head = ['ID', 'FirstName', 'LastName', 'PhoneNumber', 'Comments']
        contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r',fieldnames = head)
        contacts.writerow({'ID':contact[0], 'FirstName':contact[1], 'LastName':contact[2], 'PhoneNumber':contact[3], 'Comments':contact[4]})   
        temp = int(input('Если хотите добавить еще один контакт, нажмите 1. Если хотите выйти нажмите 0. '))
        
    while temp == 1:
        contact = list(_input.Create_New_Cont())
        with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'a') as a_file:
            contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
            contacts.writerow({'ID':contact[0], 'FirstName':contact[1], 'LastName':contact[2], 'PhoneNumber':contact[3], 'Comments':contact[4]}) 
        temp = int(input('Если хотите добавить еще один контакт, нажмите 1. Если хотите выйти нажмите 0. '))
    

def Start():    
    a = Menu()
    if a == 1:
        GetNewCont()
        print('\n Ваш запрос выполнен\n')
        Start()
    elif a == 2:
        temp = MenuForShowingCont()
        if temp == 1:
            output.ShowAllCont()
            print('\n Ваш запрос выполнен\n')
            Start()
        elif temp == 2:
            output.ShowNameAndLastName()
            print('\n Ваш запрос выполнен\n')
            Start()
        elif temp == 0:
            print()
            Start()
    elif a == 3:
        temp = MenuSorting()
        if temp == 1:
            sorting.SortingByName()
            print('\n Ваш запрос выполнен\n')
            Start()  
        elif temp == 2:
            sorting.SortingByID()
            print('\n Ваш запрос выполнен\n')
            Start()
        elif temp == 0:
            print()
            Start()
    elif a == 4:
        AddCont()
        print('\n Ваш запрос выполнен\n')
        Start()           
            
    elif a == 0:
        return
    
    
    # temp = int(input('Если хотите добавить еще один контакт, нажмите 1. Если хотите выйти нажмите 0. '))
    # if temp == 1:
    #     contact = list(_input.Create_New_Cont())
    #     with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'a') as a_file:
    #         contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
    #         contacts.writerow({'ID':contact[0], 'FirstName':contact[1], 'LastName':contact[2], 'PhoneNumber':contact[3]}) 
    # elif temp == 0:
    #     return
        

    
              
    

    
    
    

