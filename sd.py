
from datetime import datetime
today=[]

now = datetime.now()

datef= now.strftime("%m/%d")
print(now)
print(datef)

print(datef[2])

for i in range(0,5):
    if (i==0):
        if (datef[i])!='0':
            print(datef[i])
            today.append(datef[i])
    elif (i==3):
        if datef[i]!=0:
            today.append(datef[i])
    else:
        if datef[i]!="/":
            today.append(datef[i])
print(today)



