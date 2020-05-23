import numpy as np


def factura():
    num = 0
    total = 0
    articulos=np.array([" "])
    precios=np.array([" "])
    iva=np.array([" "])
    q4=str(input("¿Desea generar su factura?(si/no):"))
    while (q4=="si"):
        num+=1
        [a1,p1,i1]=preguntas(num)
        precios=np.append(precios,p1)
        articulos=np.append(articulos,a1)
        iva=np.append(iva,i1)
        q4=str(input("¿Lleva más artículos?(si/no):"))
        total = total + p1 +i1
    return articulos,precios,iva,total


def preguntas(num):
    a1=str(input("Artículo:"))
    p1=int(input("Precio:"))
    i1=p1*0.08
    return a1,p1,i1

def imprimir(articulos,precios,iva,total):
    precios=np.append(precios,total)
    print('{:^15}{:^15}{:^15}'.format('Articulos','Iva','precios'))
    for i in range(len(articulos)):
        print('{:^15}{:^15}{:^15}'.format(articulos[i],iva[i], precios[i]))
    print('{:^15}{:^15}{:^15}'.format(' ',' ',' '))
    print('{:^15}{:^15}{:^15}'.format("Total",' ',total))

[articulos,precios,iva,total]=factura()
imprimir(articulos,precios,iva,total) 
    

