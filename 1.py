def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
def show(f):
    print("\n \nФормат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца \n")
    print("      . 1 . 2 . 3 . ")
    print("      ------------- ")
    for row, i in zip(f, "a- b- c-".split()):
        print("   "f"{i} | {' | '.join(str(j) for j in row)} |")
        print("      ------------- ")
def users_input(f, user):
    while True:
        us_in = input(f"\n  Ходит игрок - {user} \nВведите координаты:") \
            .replace('1', '0').replace('2', '1') \
            .replace('3', '2').replace('a', '0') \
            .replace('b', '1').replace('c', '2').split()
        if len(us_in) != 2:
            print('Введите две координаты')
            continue
        if not(us_in[0].isdigit() and us_in[1].isdigit()):
            print('Координаты некорректно введены')
            continue
        x, y = map(int, us_in)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вышли из диапазона')
            continue
        if f[x][y] != ' ':
            print('Клетка занята-')
            continue
        break
    return x, y
def win_position(f, user):
    f_list = []
    for h in f:
        f_list += h
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False
greet()
def start(field):
    count = 0
    while True:
        show(field)
        if count % 2 == 0:
            user = 'X'
        else:
            user = 'O'
        if count < 9:
            x, y = users_input(field, user)
            field[x][y] = user
        elif count == 9:
            print('          Ничья')
            break
        if win_position(field, user):
            show(field)
            print(f'        Выйграл {user}')
            break
        count += 1

field = [[' '] * 3 for v in range(3)]
start(field)
