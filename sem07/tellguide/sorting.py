import csv
import _input

def SortingByID():
    new_list = []
    with open (r'sem07\tellguide\contacts.csv', newline = '', encoding='utf-8') as contacts:
        contacts_reader = csv.reader(contacts)
        for string in contacts_reader:
            string = string[0].split(';')
            new_list.append(string)
    del new_list[0]
    for el in new_list:
        el[0] = int(el[0])
    new_list.sort()
    
    with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'w') as a_file:
        head = ['ID', 'FirstName', 'LastName', 'PhoneNumber', 'Comments']
        contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
        contacts.writeheader()
        for element in new_list:
            contacts.writerow({'ID':element[0], 'FirstName':element[1], 'LastName':element[2], 'PhoneNumber':element[3], 'Comments':element[4]})   

def SortingByName():
    new_list = []
    with open (r'sem07\tellguide\contacts.csv', newline = '', encoding='utf-8') as contacts:
        contacts_reader = csv.reader(contacts)
        for string in contacts_reader:
            string = string[0].split(';')
            new_list.append(string)
    del new_list[0]
    new_list = sorted(new_list, key = lambda x: x[1])

    with open (r'sem07\tellguide\contacts.csv', encoding='utf-8', mode = 'w') as a_file:
        head = ['ID', 'FirstName', 'LastName', 'PhoneNumber', 'Comments']
        contacts = csv.DictWriter(a_file, delimiter=';', lineterminator = '\r', fieldnames=head)
        contacts.writeheader()
        for element in new_list:
            contacts.writerow({'ID':element[0], 'FirstName':element[1], 'LastName':element[2], 'PhoneNumber':element[3], 'Comments':element[4]})
