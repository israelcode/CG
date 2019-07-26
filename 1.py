import matplotlib.pyplot 
import numpy

fig = matplotlib.pyplot.figure()




print("rho=a*sin(2*phi)")
print("Please enter 'a':")
a=input()

Title = "rho="+str(a)+"*sin(2*phi)"

phi = numpy.arange(-2*numpy.pi, 2*numpy.pi, 0.001) 
rho = a * numpy.sin(2*phi)

ax = fig.add_subplot(111, projection='polar')
ax.plot(rho, phi)

matplotlib.pyplot.title(Title,fontsize=20)
fig.canvas.set_window_title('Chekushkin')


matplotlib.pyplot.show()

