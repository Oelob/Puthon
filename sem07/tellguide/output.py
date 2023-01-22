import _input
import controller
import csv

def ShowAllCont():
    with open (r'sem07\tellguide\contacts.csv', encoding='utf-8') as contacts:
        contacts_reader = csv.reader(contacts)
        for string in contacts_reader:
            string = string[0].replace(';',' ')
            print(''.join(string))
            
        
            
def ShowNameAndLastName():
    new_list = []

    with open (r'sem07\tellguide\contacts.csv', newline = '', encoding='utf-8') as contacts:
        contacts_reader = csv.reader(contacts)
        for string in contacts_reader:
            string = string[0].split(';')
            del string[0]
            del string[2]
            del string[-1]
            print(' '.join(string))
 
            