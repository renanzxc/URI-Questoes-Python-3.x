linhas = int(input())
x = (linhas*4)+1
pum = 4
for i in range(1,x):
    if(i==pum):
        print('PUM')
        pum+=4
    else:
        print(i,"", end="")