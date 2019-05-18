class Matriz(object):
    def __init__(self):
        pass
    def multi_suma(self,matriz):
        if isinstance(matriz, list) and len(matriz)==len(matriz[0]):
            return (self.fila_aux(matriz,-1,0,-1,-3),self.col_aux(matriz,-1,-1,+1,+3),self.sum_aux(matriz,0,0,len(matriz)-1),
                    self.fila_aux(matriz,-1,0,-1,-3)+self.col_aux(matriz,-1,-1,+1,+3)+self.sum_aux(matriz,0,0,len(matriz)-1))
        else:return "Error"
    def fila_aux(self,matriz,fila,f2,col,suma):
        if col==len(matriz[0]):
            return suma
        else:
            return self.fila_aux(matriz,fila,f2,col+1,suma+matriz[fila][col])
    def col_aux(self,matriz,fila,col,col2,suma2):
        if fila==len(matriz): 
            return suma2
        else:
            return self.col_aux(matriz,fila+1,col,col2,suma2+matriz[fila][col])
    def sum_aux(self,matriz,resultado,f,c):
        if f==len(matriz):
            return resultado
        else: return self.sum_aux(matriz,resultado+matriz[f][c],f+1,c-1)
        
m=Matriz()
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(m.multi_suma(matriz))
