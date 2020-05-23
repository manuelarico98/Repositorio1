p1=eval(input("ingrese la nota del primer parcial="))
p2=eval(input("ingrese la nota del segundo parcial="))
t=eval(input("ingrese la nota del taller="))
p=eval(input("ingrese la nora del proyecto="))

def nota(p1,p2,t,p):
    nota=((p1+p2)*0.25)+(0.2*t)
    print("Nota final=",nota)
    return

nota(p1,p2,t,p)
