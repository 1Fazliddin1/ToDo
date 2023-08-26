import curses
import random

# To'g'ri yo'nalishlarni aniqlash
def togri_yunalish(x, y, tam):
    if tam[0][0] == x and tam[0][1] == y:
        return True
    return False

# O'yin boshlandi
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Ilk o'yin holatini aniqlash
tam = [[4, 10], [4, 9], [4, 8]]
yem = [10, 20]
win.addch(yem[0], yem[1], '*')
score = 0

# O'yin davom etadi
while True:
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' Snake ')
    win.timeout(150 - (len(tam)//5 + len(tam)//10)%120)

    # Yangi yemni qo'yish
    if yem == tam[0]:
        tam.append([0,0])
        yem = []
        score += 1
        while yem == []:
            yem = [random.randint(1, 18),random.randint(1, 58)]
            if yem in tam:
                yem = []
        win.addch(yem[0], yem[1], '*')

    # To'g'ri yo'nalishni aniqlash
    eski_kurs = win.getch()
    yonalish = eski_kurs if eski_kurs != -1 else last_kurs
    if yonalish == curses.KEY_DOWN:
        next_tam = [tam[0][0] + 1, tam[0][1]]
    elif yonalish == curses.KEY_UP:
        next_tam = [tam[0][0] - 1, tam[0][1]]
    elif yonalish == curses.KEY_RIGHT:
        next_tam = [tam[0][0], tam[0][1] + 1]
    elif yonalish == curses.KEY_LEFT:
        next_tam = [tam[0][0], tam[0][1] - 1]
    else:
        next_tam = [tam[0][0], tam[0][1]]

    # Tamni yangilash
    last_kurs = yonalish
    if next_tam in tam or next_tam[0] == 0 or next_tam[0] == 19 or next_tam[1] == 0 or next_tam[1] == 59:
        curses.endwin()
        quit()
    tam.insert(0, next_tam)
    if togri_yunalish(yem[0], yem[1], tam):
        yem = []
        while yem == []:
            yem = [random.randint(1, 18),random.randint(1, 58)]
            if yem in tam:
                yem = []
        win.addch(yem[0], yem[1], '*')
    else:
        eski_tam = tam.pop()
        win.addch(eski_tam[0], eski_tam[1], ' ')
    win.addch(tam[0][0], tam[0][1], '#')