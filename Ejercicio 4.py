class Inspeccion(object):
    def __init__(self):
        pass
    def inspec(self,num1,num2):
        if isinstance(num1,int)and isinstance(num2,int):
            return self.ins_aux(num1,num2,1)
        else:return "error"
    def ins_aux(self,num1,num2,divisor):
        if ((num2/divisor) + divisor) == num1:
            return ((num2/divisor),divisor)
        if ((num2/divisor) + divisor) != num1:
            if (num2%divisor) == 0:
                return self.ins_aux(num1,num2,divisor+1)
            else:
                return self.ins_aux(num1,num2,divisor+1)
        else: self.ins_aux(num1,num2,divisor)

i=Inspeccion()
num1 = 7
num2 = 12
print(i.inspec(num1,num2))
