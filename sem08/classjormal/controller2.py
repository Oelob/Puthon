import _input
import _output

names = []
subjs = []
students = {}

def Button():
    while True:
        
        print()
        a = _input.viewer()
        print('==========================')
        
        if a == 1:
            name = _input.st_name()
            names.append(name)
            students[name] = {}
            if subjs:
                for subj in subjs:
                    students[name][subj] = None        
        if a == 2:
            subj = _input.st_subjects()
            subjs.append(subj)
            for key in students.keys():
                for subj in subjs:
                    if subj in students[key]:
                        continue
                    else:
                        students[key][subj] = None
                
        if a == 3:
            temp = list(_input.add_mark(names,subjs))
            if students[temp[0]][temp[1]] == None:
                students[temp[0]][temp[1]] = temp[2]
            else:
                for el in temp[2]:
                    students[temp[0]][temp[1]].append(el)
            
            
        if a == 4:
            name = _input.concret_student(names)
            print(students[name])
            
        if a == 5:
            for key in students.keys():
                print(f'Ученик {key} - {students[key]}')
        
        if a == 6:
            break

