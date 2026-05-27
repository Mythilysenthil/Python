ele = [] #without list comprension
for x in range (5):
   ele.append(x**2)
print(ele)   

ele1 = [x**2 for x in range(5)] # with list comprension
print(ele1)