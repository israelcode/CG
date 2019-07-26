#coding=utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

#Чекушкин
#12. Анимация. Координата Y изменяется по закону Y = cos(t+Y)
try:
    # for Python2
    import Tkinter as tk
    import tkSimpleDialog as tksd
except:
    # for Python3
    import tkinter as tk
    import tkinter.simpledialog as tksd

#2-2-0
#global q
#global w
#global e

root = tk.Tk()
q = tksd.askfloat("Parametr 1 (Float)", "Введите параметр освещения(x):",
    parent=root, minvalue=0)
w = tksd.askfloat("Parametr 1 (Float)", "Введите параметр освещения(y):",
    parent=root, minvalue=0)
e = tksd.askfloat("Parametr 1 (Float)", "Введите параметр освещения(z):",
    parent=root, minvalue=0)

#Параметры освещения и отражающие свойства материала задаются пользователем в диалоговом режиме.
#print('Введите параметры освещение(x,y,z)')
#a=float(input())
#b=float(input())
#c=float(input())

a=q
b=w
c=e

# Объявляем все глобальные переменные
global xrot         # Величина вращения по оси x
global yrot         # Величина вращения по оси y
global ambient      # рассеянное освещение
global cylcolor    # Цвет цилиндра
global lightpos     # Положение источника освещения
global Y
Y = 0.1
# Процедура инициализации
def init():
    global xrot         # Величина вращения по оси x
    global yrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    global cylcolor    # Цвет цилиндра
    global lightpos     # Положение источника освещения

    xrot = 10.0                          # Величина вращения по оси x = 0
    yrot = 0.0                          # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)        # Первые три числа цвет в формате RGB, а последнее - яркость
    cylcolor = (0, 0, 1, 0.8)    # Коричневый цвет для ствола
    lightpos = (a, b, c)          # Положение источника освещения по осям xyz
    #lightpos = (2.0, -2.0, -1.0)

    glClearColor(0.5, 0.5, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)                # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 1.0, 0.0, 0.0)                   # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Определяем положение источника света


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки


# Процедура перерисовки
#def draw():
#    global xrot
#    global yrot
#    global lightpos
#    global greencolor
#    global cylcolor

    
#    glClear(GL_COLOR_BUFFER_BIT)                                # Очищаем экран и заливаем серым цветом
#    glPushMatrix()                                              # Сохраняем текущее положение "камеры"
#    glRotatef(xrot, 1.0, 0.0, 0.0)                              # Вращаем по оси X на величину xrot
#    glRotatef(yrot, 0.0, 1.0, 0.0)                              # Вращаем по оси Y на величину yrot
#    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                 # Источник света вращаем вместе с елкой

    # Рисуем цилиндр
    # Устанавливаем материал: рисовать с 2 сторон, рассеянное освещение, синий цвет
#    glMaterialfv(GL_FRONT, GL_DIFFUSE, cylcolor)
#    glTranslatef(0.0, 0.0, -0.7)                                # Сдвинемся по оси Z на -0.7
    # Рисуем цилиндр с радиусом 0.1, высотой 0.2
    # Последние два числа определяют количество полигонов
#    glutSolidCylinder(0.5, 1, 20, 20)
#    glPopMatrix()                                               # Возвращаем сохраненное положение "камеры"
#    glutSwapBuffers()                                           # Выводим все нарисованное в памяти на экран

def draw():
    global xrot, yrot, lightpos, greencolor, cylcolor, Y
    Y=1

    timeSinceStart = glutGet(GLUT_ELAPSED_TIME)

    glEnable(GL_DEPTH_TEST) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                               
   
    glPushMatrix()   
    
    Y=Y*math.cos(timeSinceStart*0.002+Y)                          
    glTranslatef(0.0, 0.5, Y)         #math.cos(timeSinceStart*0.002)         
    glRotatef(xrot, 1.0, 0.0, 0.0)                              
    glRotatef(yrot, 0.0, 1.0, 0.0)                          

    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                
    glMaterialfv(GL_FRONT, GL_DIFFUSE, cylcolor)                            
    glutSolidCylinder(0.5, 1, 20, 20)
    glPopMatrix()                                             

    glutSwapBuffers()
    glutPostRedisplay()



# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glEnable(GL_DEPTH_TEST) 
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(500, 500)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(50, 50)
# Инициализация OpenGl
glutInit(sys.argv)
glutCreateWindow(b"Chekushkin")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
# Запускаем основной цикл
glutMainLoop()
