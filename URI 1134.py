alcool = 0
gasolina = 0
diesel = 0

comb = int(input())
while(comb != 4):
    if(comb<4 and comb>0):
        if(comb==1):
            alcool+=1
        elif(comb==2):
            gasolina+=1
        else:
            diesel+=1
    comb = int(input())
    
print("MUITO OBRIGADO")
print("Alcool: %d" %alcool)
print("Gasolina: %d" %gasolina)
print("Diesel: %d" %diesel)