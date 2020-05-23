import numpy as np

def inventario():
    nomsf=np.array(" ")
    cantf=np.array(" ")
    rr="si"
    maxi=-1
    while (rr=="si"):
        nom=str(input("Nombre de producto:"))
        can=int(input("Cantidad de unidades:"))
        if maxi==-1:
            maxi=1
            noms=np.array(nom)
            cant=np.array(can)
        else:
            noms=np.append(noms,nom)
            cant=np.append(cant,can)
        rr=str(input("¿Desea agregar más productos?"))
    for k in range(len(noms)):
        maxi=max(cant)
        for r in range(len(noms)):
            if cant[r]==maxi:
                nomsf=np.append(noms[r],nomsf)
                cantf=np.append(cant[r],cantf)
                cant[r]=-1
                
    print("-----Inventario-----")
    print('{:^15}{:^15}'.format('Producto','Cantidad'))
    for i in range(len(nomsf)):
        print('{:^15}{:^15}'.format(nomsf[i],cantf[i]))
    print("---------------------")
    return


inventario()

