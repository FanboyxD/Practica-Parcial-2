class Promedio(object):
    def __init__(self):
        pass
    def prom_med(self,matriz):
        if isinstance(matriz,list):
            return self.pro(matriz,0,0,0,0),self.med(matriz,(self.unifi(matriz,[],0,0)),0)
        else: return "Error"
    def pro(self,matriz,fila,col,result,contador):
        if fila == len(matriz):
            return result//contador
        else:
            return self.pro(matriz,fila+1,col+1,result+matriz[fila][col],contador+1)
    def med(self,matriz,lista,mediana):
        if mediana > 0:
            return mediana
        par =((lista[len(lista)//2])+(lista[len(lista)//2+1])//2)
        impar = (lista[(len(lista)+1)]//2)
        if (len(lista))%10%2 == 0:
            return self.mediana(matriz,lista,mediana+par)
        else:
            return self.mediana(matriz,lista,mediana+impar)
    def unifi(self,matriz,lista,fila,col):
        if fila == len(matriz):
            return lista
        if col == 1:
            return self.unifi(matriz,lista,fila+1,0)
        else:
            return self.unifi(matriz,lista+matriz[fila],fila,col+1)

p = Promedio()
matriz = ([[8, 12, 16],
           [20, 24, 28],
           [32, 36, 40]]) 
print(p.prom_med(matriz))
