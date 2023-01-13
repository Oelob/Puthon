from termcolor import colored, cprint

dict_draw = {1:'___|', 2:'___|',3:'___ ',
             4:'___|', 5:'___|',6:'___ ',
             7:' _ |', 8:' _ |',9:' _  '}
dict_game = {1:'___|', 2:'___|',3:'___ ',
             4:'___|', 5:'___|',6:'___ ',
             7:'   |', 8:'   |',9:'    '}
dict_cell = {1:'_1_|', 2:'_2_|',3:'_3_',
             4:'_4_|', 5:'_5_|',6:'_6_',
             7:' 7 |', 8:' 8 |',9:' 9 '}
def PrintPole(pole):
    str_1= ''
    for key, value in pole.items():
        if key % 3 == 0:
            str_1 = f'{str_1}{value}\n'
        else:
            str_1 = str_1 + value
    print(str_1)


def Hod_x():
    PrintPole(dict_cell)
    a = int(input('Укажите номер клетки, где хотите поставить свой знак: '))
    for key, value in dict_game.items():
        if key == a:
            for i in range(len(dict_game[key])):
                if i == 1:
                    dict_game[key] = f'{value[:i]}x{value[i+1:]}'
                    dict_cell[key] = f'{value[:i]}_{value[i+1:]}'
            break
    PrintPole(dict_game)

def Hod_o():
    PrintPole(dict_cell)

    a = int(input('Укажите номер клетки, где хотите поставить свой знак: '))
    for key, value in dict_game.items():
        if key == a:
            for i in range(len(dict_game[key])):
                if i == 1:
                    dict_game[key] = f'{value[:i]}o{value[i+1:]}'
                    dict_cell[key] = f'{value[:i]}_{value[i+1:]}'
            break
    PrintPole(dict_game)
def Check_X(pole):
    if 'x' in pole[1] and 'x' in pole[2] and 'x' in pole[3]:
        return True
    elif 'x' in pole[4] and 'x' in pole[5] and 'x' in pole[6]:
        return True
    elif 'x' in pole[7] and 'x' in pole[8] and 'x' in pole[9]:
        return True    
    elif 'x' in pole[1] and 'x' in pole[5] and 'x' in pole[9]:
        return True
    elif 'x' in pole[3] and 'x' in pole[5] and 'x' in pole[7]:
        return True
    elif 'x' in pole[1] and 'x' in pole[4] and 'x' in pole[7]:
        return True
    elif 'x' in pole[2] and 'x' in pole[5] and 'x' in pole[8]:
        return True    
    elif 'x' in pole[3] and 'x' in pole[6] and 'x' in pole[9]:
        return True    

def Check_O(pole):
    if 'o' in pole[1] and 'o' in pole[2] and 'o' in pole[3]:
        return True
    elif 'o' in pole[4] and 'o' in pole[5] and 'o' in pole[6]:
        return True
    elif 'o' in pole[7] and 'o' in pole[8] and 'o' in pole[9]:
        return True    
    elif 'o' in pole[1] and 'o' in pole[5] and 'o' in pole[9]:
        return True
    elif 'o' in pole[3] and 'o' in pole[5] and 'o' in pole[7]:
        return True
    elif 'o' in pole[1] and 'o' in pole[4] and 'o' in pole[7]:
        return True
    elif 'o' in pole[2] and 'o' in pole[5] and 'o' in pole[8]:
        return True    
    elif 'o' in pole[3] and 'o' in pole[6] and 'o' in pole[9]:
        return True    

def X_Move():
    cprint('ХОД КРЕСТИКОВ\n','red')
    Hod_x()
def O_Move():
    cprint('ХОД НОЛИКОВ\n','red')
    Hod_o()

def Game():
    X_Move()
    Check_X(dict_game)
    if Check_X(dict_game) == True:
        cprint('КРЕСТИКИ ПОБЕДИЛИ', 'green','on_yellow',['bold','blink'])
        return
    if dict_cell == dict_draw:
        cprint('ЭТО НИЧЬЯ!!!','green','on_yellow',['bold','blink'])
        return
    O_Move()
    Check_O(dict_game)
    if Check_O(dict_game) == True:
        cprint('НОЛИКИ ПОБЕДИЛИ','green','on_yellow',['bold','blink'])
        return
    if dict_cell == dict_draw:
        cprint('ЭТО НИЧЬЯ!!!','green','on_yellow',['bold','blink'])
        return
    Game()
    
Game()


