import math
import matplotlib.pyplot as plt

def Runge_Kutta_4(x_0, y_0, step, dots_quantity):
    lstx = [x_0]
    lsty = [y_0]
    def func_de_1(x, y):                    # функция дифференциального уравнения 1-го порядка в виде y' = f(x, y)
        return (2*x*y)/(1+x**2)+1/(1+x**2)
    
    for i in range(dots_quantity - 1): #так как у нас уже есть точки x_0 и y_0
        k_1 = func_de_1(lstx[i], lsty[i])
        k_2 = func_de_1(lstx[i]+step/2, lsty[i]+step/2*k_1)
        k_3 = func_de_1(lstx[i]+step/2, lsty[i]+step/2*k_2)
        k_4 = func_de_1(lstx[i]+step, lsty[i]+step*k_3)

        lstx.append(round(lstx[i]+step, int(math.log(1/step, 10) + 1))) 
        lsty.append(round(lsty[i]+step/6*(k_1+2*k_2+2*k_3+k_4), 3))
    
    return lstx, lsty 


x, y = Runge_Kutta_4(1, 3, 0.01, 101)

fig1 = plt.subplot()
fig1.plot(x, y)
plt.title("Решение краевой задачи Коши")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()