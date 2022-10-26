import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

print("Inputkan variabel abcd dengan rumus y = ax^3 + bx^2 + cx + d")
a = int(input("masukan konstanta a: "))
b = int(input("masukan konstanta b: "))
c = int(input("masukan konstanta c: "))
d = int(input("masukan konstanta d: "))



xl = int(input("masukan batas bawah: ")) #input batas bawah
xu = int(input("masukan batas atas: "))  #input batas atas
xlist = np.linspace(-xu,xu,10)
ylist = f(xlist,a,b,c,d)
toleransi = float(input("masukan batas toleransi dalam persen: ")) #batas toleransi error dari perhitungan kita
error = 100 #kondisi error dari metode kita
i = 1 #iterator kita
print("iterasi  batas bawah \tbatas atas \tnilai akar \terror")

if(f(xl,a,b,c,d)*f(xu,a,b,c,d) < 0):
    while (error > toleransi):
        if(i > 1):
            xr_lama = xr
        else:
            xr_lama = xl
        xr = (xl + xu)/2    #xr adalah titik hasil bagi dua kita
        print(f"{i:<6d} \t{xl:10.6f} \t{xu:10.6f} \t{xr:10.6f} \t{error:10.6f}")
        error = np.abs((xr - xr_lama)/xr) * 100
        if(f(xr,a,b,c,d)*f(xu,a,b,c,d)< 0):
            xl = xr
        else:
            xu = xr

        i += 1
else:print("Nilai akar tidak ditemukan pada rentang batas nilai yang kamu masukan :(")
plt.plot(xlist,ylist)
plt.title("Grafik Fungsi")
ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()


