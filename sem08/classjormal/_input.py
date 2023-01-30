import _output

def viewer():
    a = int(input('1 - добавление студента\n2 - добавление предмета\n3 - ввод оценки\n4 - вывод оценок ученика\n5 - общий список учеников\n6 - выход\n'))
    return a




def add_mark(a,b):
    _output.ShowStud(a)
    name = (input('Выберите студента: '))
    _output.ShowSubj(b)
    subj = (input('Выберите предмет: '))
    mark = list((input('Введите оценки: ')))
    return name, subj, mark

def st_name():
    name = input('Введите имя и фамилию: ')
    
    return name

def st_subjects():
    return input('Введите предмет: ')

def concret_student(a):
    _output.ShowStud(a)
    conc_stud = input('Введите имя ученика для показа его оценок: ')
    return conc_stud