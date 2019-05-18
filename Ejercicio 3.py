class Cientifica(object):
    def __init__(self):
        pass
    def cien(self,num):
        if isinstance(num,int):
            return self.cien_aux(num,0)
        else:return "error"
    def cien_aux(self,num,exponente):
        if num < 1:
            return self.cien_aux(num*10,exponente-1)
        elif num > 10:
            return self.cien_aux(num//10,exponente+1)
        elif 1<=num<10:
            return(str(num)+"x10**"+str(exponente))

c=Cientifica()

num = 4000000

print(c.cien(num))
