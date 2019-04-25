while(True):
  lista=[]
  maria=0
  joao=0
  n=int(input(""))
  if(n==0):
    break
  lista=input().split(" ")
  for i in range(0,n):
    if(lista[i]=="0"):
      maria+=1
    elif(lista[i]=="1"):
      joao+=1
  print("Mary won",maria,"times and John won",joao,"times")
