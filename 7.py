#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

#Чекушкин М8О-304Б
# 12 вариант, B-сплайн. n = 6, k = 4. Узловой вектор равномерный.


# cv = массив контрольных точек
# n = количество точек кривой 
# d = степень кривой d=k-1, где k - порядок 
# closed = кривая замкнута или открыта (TRUE/FALSE) 
def bspline(cv, n=100, d=3, closed=False):

    # Массив промежутков u
    count = len(cv)
    knots = None
    u = None

    if not closed:
        u = np.arange(0,n,dtype='float')/(n-1) * (count-d)
	print(len(u))	
	print(u)
        knots = np.array([0]*d + range(count-d+1) + [count-d]*d,dtype='int')
	print(knots)

    else:
        u = ((np.arange(0,n,dtype='float')/(n-1) * count) - (0.5 * (d-1))) % count 
	print(len(u))	
	print(u)
        knots = np.arange(0-d,count+d+d-1,dtype='int')
	print(knots)


    # Рекурсивный аогоритм Кокса - де Бура 
    def coxDeBoor(u, k, d):

        # Входит ли точка в данный промежуток?
        if (d == 0):
            if (knots[k] <= u and u < knots[k+1]):
                return 1
            return 0

        Den1 = knots[k+d] - knots[k]
        Den2 = knots[k+d+1] - knots[k+1]
        Eq1  = 0;
        Eq2  = 0;

        if Den1 > 0:
            Eq1 = ((u-knots[k]) / Den1) * coxDeBoor(u,k,(d-1))
        if Den2 > 0:
            Eq2 = ((knots[k+d+1]-u) / Den2) * coxDeBoor(u,(k+1),(d-1))

        return Eq1 + Eq2


    # Значение кривой для каждого промежутка u
    samples = np.zeros((n,3))
    for i in xrange(n):
        if not closed:
            if u[i] == count-d:
                samples[i] = np.array(cv[-1])
            else:
                for k in xrange(count):
                    samples[i] += coxDeBoor(u[i],k,d) * cv[k]

        else:
            for k in xrange(count+d):
                samples[i] += coxDeBoor(u[i],k,d) * cv[k%count]


    return samples




#Массив контрольных точек
cv = np.array([[ 50.,  25.,  -0.],
[ 55.,  20.,  -0.],
[ 50.,  15.,   0.],
[ 42.95,   15.,   0.],
[ 42.95,   7.95,   0.],
[ 50.,   7.95,  -0.]])
 

q=0
#while q<5:
a = np.asarray(input())
print(a)


p = bspline(cv)
x,y,z = p.T
cv = cv.T
plt.plot(cv[0],cv[1], 'o-', label='Control Points')
plt.plot(x,y,'k-',label='B-SPLINE')
plt.minorticks_on()
Title = "B-SPLINE(k=4,n=6)"
plt.title(Title,fontsize=20)	
plt.gcf().canvas.set_window_title("Chekushkin")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(35, 70)
plt.ylim(0, 30)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


